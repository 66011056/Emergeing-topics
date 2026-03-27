import streamlit as st
import pandas as pd

from src.data_loader import load_csv
from src.preprocess import preprocess_dataframe
from src.utils import get_docs, get_timestamps
from src.topic_model import train_topic_model, get_topic_info_table
from src.trend_analysis import compute_topics_over_time, calculate_emerging_topics
from src.visualization import (
    plot_top_topics_bar,
    plot_topics_over_time_simple,
    plot_topics_over_time_ema,
    plot_emerging_topics_bar
)

st.set_page_config(page_title="BERTopic Dashboard", layout="wide")

st.title("BERTopic Emerging Topic Dashboard")
st.write(
    "Upload a CSV dataset to discover topics, analyze topic trends over time, "
    "and detect emerging topics."
)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])


def detect_text_columns(df):
    return [col for col in df.columns if df[col].dtype == "object"]


def detect_time_columns(df):
    time_cols = []
    for col in df.columns:
        converted = pd.to_datetime(df[col], errors="coerce")
        if converted.notna().sum() > 0:
            time_cols.append(col)
    return time_cols


@st.cache_data
def preprocess_cached(df, text_col, time_col):
    return preprocess_dataframe(df, text_col, time_col)


@st.cache_resource
def train_cached(docs):
    return train_topic_model(list(docs))


if uploaded_file is not None:
    df = load_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    text_candidates = detect_text_columns(df)
    time_candidates = detect_time_columns(df)

    if not text_candidates:
        st.error("No usable text column was detected.")
        st.stop()

    text_col = st.selectbox("Select text column", text_candidates)

    other_text_candidates = [c for c in text_candidates if c != text_col]
    use_extra_text = False
    extra_text_col = None

    if other_text_candidates:
        use_extra_text = st.checkbox("Combine with another text column")
        if use_extra_text:
            extra_text_col = st.selectbox("Select extra text column", other_text_candidates)

    valid_time_candidates = [c for c in time_candidates if c != text_col and c != extra_text_col]

    if not valid_time_candidates:
        st.error("No valid time/date column was detected.")
        st.stop()

    time_col = st.selectbox("Select time column", valid_time_candidates)

    sample_size = st.slider("Sample size for faster training", 500, 5000, 2000, 500)
    ema_span = st.slider("EMA smoothing span", 2, 20, 5, 1)
    top_n_topics = st.slider("Number of topics to display in trend charts", 3, 12, 6, 1)

    if st.button("Run Analysis"):
        try:
            working_df = df.copy()

            if use_extra_text and extra_text_col is not None:
                working_df[text_col] = (
                    working_df[text_col].fillna("").astype(str).str.strip() + " " +
                    working_df[extra_text_col].fillna("").astype(str).str.strip()
                )

            working_df = preprocess_cached(working_df, text_col, time_col)

            # Sample for faster training
            if len(working_df) > sample_size:
                working_df = working_df.sample(sample_size, random_state=42)

            docs = get_docs(working_df, text_col)
            timestamps = get_timestamps(working_df, time_col)

            if not docs:
                st.error("No valid text documents remain after preprocessing.")
                st.stop()

            if len(docs) != len(timestamps):
                st.error("The number of documents and timestamps does not match.")
                st.stop()

            if not all(isinstance(doc, str) and doc.strip() != "" for doc in docs):
                st.error("BERTopic input is invalid. The text iterable must contain only non-empty strings.")
                st.stop()

            with st.spinner("Training BERTopic model..."):
                topic_model, topics, probs = train_cached(tuple(docs))

            with st.spinner("Generating topic summary..."):
                topic_info = get_topic_info_table(topic_model)

            with st.spinner("Analyzing topics over time..."):
                topics_over_time = compute_topics_over_time(topic_model, docs, timestamps, nr_bins=50)
                emerging = calculate_emerging_topics(topics_over_time, topic_model)

            st.subheader("Topic Summary")
            st.dataframe(topic_info)

            st.subheader("Emerging Topics Chart")
            fig_emerging = plot_emerging_topics_bar(emerging, top_n=10)
            st.plotly_chart(fig_emerging, use_container_width=True)

            st.subheader("Emerging Topics")
            st.dataframe(emerging)

            st.subheader("Top Topics by Count")
            fig_bar = plot_top_topics_bar(topic_info, top_n=10)
            st.plotly_chart(fig_bar, use_container_width=True)

            st.subheader("Topics Over Time")
            fig_time = plot_topics_over_time_simple(
                topics_over_time,
                topic_info=topic_info,
                top_n=top_n_topics
            )
            st.plotly_chart(fig_time, use_container_width=True)

            st.subheader("Smoothed Topic Trends")
            fig_ema = plot_topics_over_time_ema(
                topics_over_time,
                topic_info=topic_info,
                span=ema_span,
                top_n=top_n_topics
            )
            st.plotly_chart(fig_ema, use_container_width=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")