import pandas as pd


def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def validate_columns(df, text_col, time_col=None):
    """Validate that required columns exist in the DataFrame."""
    if text_col not in df.columns:
        raise ValueError(f"Text column '{text_col}' not found in dataset.")
    if time_col is not None and time_col not in df.columns:
        raise ValueError(f"Time column '{time_col}' not found in dataset.")
    return True
