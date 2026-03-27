import pandas as pd


def compute_topics_over_time(topic_model, docs, timestamps, nr_bins=50):
    """
    Compute topic frequencies over time using a smaller number of time bins
    to improve speed and readability.
    """
    return topic_model.topics_over_time(docs, timestamps, nr_bins=nr_bins)


def calculate_emerging_topics(topics_over_time, topic_model, window_days=30):
    """
    Calculate emerging topics by comparing recent frequency
    against previous frequency.
    """
    tot = topics_over_time.copy()
    tot["Timestamp"] = pd.to_datetime(tot["Timestamp"])

    max_t = tot["Timestamp"].max()
    recent_start = max_t - pd.Timedelta(days=window_days)
    prev_start = max_t - pd.Timedelta(days=2 * window_days)

    recent = tot[tot["Timestamp"] >= recent_start]
    prev = tot[(tot["Timestamp"] >= prev_start) & (tot["Timestamp"] < recent_start)]

    recent_counts = recent.groupby("Topic")["Frequency"].sum()
    prev_counts = prev.groupby("Topic")["Frequency"].sum()

    emerging = pd.DataFrame({
        "recent": recent_counts,
        "previous": prev_counts
    }).fillna(0)

    emerging["emerging_score"] = (emerging["recent"] + 1) / (emerging["previous"] + 1)
    emerging = emerging.drop(index=-1, errors="ignore")

    def topic_name(topic_id):
        words = topic_model.get_topic(topic_id)
        if not words:
            return "(no words)"
        return ", ".join([word for word, _ in words[:5]])

    emerging["top_words"] = [topic_name(topic_id) for topic_id in emerging.index]
    emerging = emerging.sort_values("emerging_score", ascending=False)

    return emerging.reset_index().rename(columns={"index": "Topic"})
