import re
import pandas as pd


def clean_text(text):
    """
    Convert value to clean string for BERTopic.
    """
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_dataframe(df, text_col, time_col=None):
    """
    Preprocess dataset:
    - clean text column
    - remove empty text rows
    - convert time column to datetime if provided
    - remove invalid time rows
    """
    df = df.copy()

    # Clean text column
    df[text_col] = df[text_col].apply(clean_text)
    df = df[df[text_col] != ""]

    # Clean time column if provided
    if time_col is not None:
        df[time_col] = pd.to_datetime(df[time_col], errors="coerce")
        df = df.dropna(subset=[time_col])

    return df