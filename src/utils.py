import pandas as pd


def get_docs(df, text_col):
    """
    Return BERTopic-safe list of strings.
    """
    docs = (
        df[text_col]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    docs = docs[docs != ""]
    return docs.tolist()


def get_timestamps(df, time_col):
    """
    Return timestamps as strings for BERTopic topics_over_time.
    """
    return pd.to_datetime(df[time_col], errors="coerce").dt.strftime("%Y-%m-%d").tolist()