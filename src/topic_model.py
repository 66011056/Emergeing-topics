from bertopic import BERTopic
from sentence_transformers import SentenceTransformer


def train_topic_model(docs):
    """
    Train a BERTopic model on the given documents.
    Returns:
        topic_model, topics, probs
    """
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    topic_model = BERTopic(
        embedding_model=embedding_model,
        calculate_probabilities=False,
        verbose=True
    )

    topics, probs = topic_model.fit_transform(docs)
    return topic_model, topics, probs


def get_topic_info_table(topic_model):
    """Return topic summary information."""
    return topic_model.get_topic_info()


def save_topic_model(topic_model, save_path):
    """Save the trained BERTopic model."""
    topic_model.save(save_path)
