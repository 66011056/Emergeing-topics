import pandas as pd
import plotly.express as px


def _build_topic_label_map(topic_info):
    info = topic_info.copy()
    info = info[info["Topic"] != -1]

    name_map = {}
    words_map = {}

    for _, row in info.iterrows():
        topic_id = row["Topic"]
        short_words = str(row.get("Representation", "")).split(",")[:3]
        short_words = ", ".join([w.strip() for w in short_words if w.strip()])
        short_name = f"Topic {topic_id}: {short_words}" if short_words else f"Topic {topic_id}"

        name_map[topic_id] = short_name
        words_map[topic_id] = str(row.get("Representation", ""))

    return name_map, words_map


def _get_top_topics(topic_info, top_n=8):
    df = topic_info.copy()
    df = df[df["Topic"] != -1]
    return df.nlargest(top_n, "Count")["Topic"].tolist()


def plot_top_topics_bar(topic_info, top_n=10):
    df = topic_info.copy()
    df = df[df["Topic"] != -1].head(top_n)

    fig = px.bar(
        df,
        x="Name",
        y="Count",
        hover_data=["Topic", "Representation"],
        title=f"Top {top_n} Topics by Count"
    )
    fig.update_layout(xaxis_title="Topic", yaxis_title="Document Count")
    return fig


def plot_topics_over_time_simple(topics_over_time, topic_info, top_n=8):
    df = topics_over_time.copy()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df[df["Topic"] != -1]

    top_topics = _get_top_topics(topic_info, top_n=top_n)
    df = df[df["Topic"].isin(top_topics)]

    name_map, words_map = _build_topic_label_map(topic_info)
    df["Topic_Name"] = df["Topic"].map(name_map)
    df["Topic_Words"] = df["Topic"].map(words_map)

    fig = px.line(
        df,
        x="Timestamp",
        y="Frequency",
        color="Topic_Name",
        hover_data={
            "Topic": True,
            "Timestamp": True,
            "Frequency": True,
            "Topic_Words": True,
            "Topic_Name": False
        },
        title=f"Topics Over Time (Top {top_n})"
    )

    fig.update_traces(mode="lines+markers")
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Frequency",
        legend_title="Topics"
    )
    return fig


def plot_topics_over_time_ema(topics_over_time, topic_info, span=5, top_n=8):
    df = topics_over_time.copy()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df[df["Topic"] != -1]

    top_topics = _get_top_topics(topic_info, top_n=top_n)
    df = df[df["Topic"].isin(top_topics)]

    name_map, words_map = _build_topic_label_map(topic_info)
    df["Topic_Name"] = df["Topic"].map(name_map)
    df["Topic_Words"] = df["Topic"].map(words_map)

    df = df.sort_values(["Topic", "Timestamp"])
    df["EMA_Frequency"] = df.groupby("Topic")["Frequency"].transform(
        lambda s: s.ewm(span=span, adjust=False).mean()
    )

    fig = px.line(
        df,
        x="Timestamp",
        y="EMA_Frequency",
        color="Topic_Name",
        hover_data={
            "Topic": True,
            "Timestamp": True,
            "Frequency": True,
            "EMA_Frequency": ':.2f',
            "Topic_Words": True,
            "Topic_Name": False
        },
        title=f"Smoothed Topic Trends (Top {top_n}, EMA span={span})"
    )

    fig.update_traces(mode="lines+markers")
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Smoothed Frequency",
        legend_title="Topics"
    )
    return fig


def plot_emerging_topics_bar(emerging, top_n=10):
    df = emerging.copy().head(top_n)

    fig = px.bar(
        df,
        x="top_words",
        y="emerging_score",
        hover_data=["Topic", "recent", "previous"],
        title=f"Top {top_n} Emerging Topics"
    )
    fig.update_layout(xaxis_title="Topic Keywords", yaxis_title="Emerging Score")
    return fig