# BERTopic Emerging Topic Dashboard

## Overview
This project is an interactive text analytics dashboard built with **Streamlit** and **BERTopic**. It allows users to upload a CSV dataset, select a text column and a time column, and run topic modeling to discover the main themes in the data.

The dashboard is designed to answer three practical questions:

1. **What are the main topics in the dataset?**
2. **How do those topics change over time?**
3. **Which topics are emerging faster than others?**

This version of the project focuses on **clear topic interpretation** and **simple trend visualization**. Instead of using a more complex hierarchical topic chart, the dashboard emphasizes:

- Topic Summary
- Emerging Topics Chart
- Emerging Topics Table
- Top Topics by Count
- Topics Over Time
- Smoothed Topic Trends

---

## Features

- Upload your own CSV dataset
- Select a text column for topic modeling
- Select a time column for trend analysis
- Generate interpretable topics using **BERTopic**
- View topic frequency over time
- Detect fast-growing or emerging topics
- Use **EMA smoothing** to better understand long-term trends
- Adjust sample size for faster performance

---

## Why BERTopic

BERTopic was chosen because it can generate topics from text using **semantic embeddings**, rather than relying only on word counts. This makes it especially useful for short text data such as:

- news headlines
- article titles
- short descriptions
- abstracts

Compared with traditional topic modeling methods, BERTopic provides:

- more meaningful topic grouping
- interpretable keyword-based topic labels
- integration with time-based topic analysis

---

## Why Time-Based Trend Analysis

Topic modeling alone tells us what themes exist in the dataset. However, many real-world text datasets also contain time information, which allows us to study how those themes change.

This project adds:

- **Topics Over Time** to show raw topic frequency changes
- **Smoothed Topic Trends** using **Exponential Moving Average (EMA)**
- **Emerging Topic Detection** to identify fast-growing topics

These additions make the dashboard more useful for understanding trends, not just topic clusters.

---

## Visual Outputs

### Topic Summary
Displays the discovered topics, the number of documents assigned to each topic, and representative keywords for interpretation.

### Emerging Topics Chart
Ranks topics with the highest emerging scores, making it easier to identify which topics are growing most rapidly.

### Emerging Topics Table
Compares recent topic frequency with previous topic frequency and calculates an emerging score for each topic.

### Top Topics by Count
Shows the most frequent topics in the dataset sample.

### Topics Over Time
Visualizes the raw frequency of important topics across time.

### Smoothed Topic Trends
Applies **EMA smoothing** to reduce short-term noise and make long-term topic patterns easier to interpret.

---

## Why Sampling Is Used

BERTopic can be computationally expensive because it performs several processing steps, including:

- text embedding
- dimensionality reduction
- clustering
- topic representation

To improve speed and make the dashboard easier to use, this project allows the user to choose a sample size before training.

---

## Recommended Dataset Format

The dashboard works best with a CSV file containing:

- one text column such as `headline`, `description`, `abstract`, or `title`
- one valid date/time column

### Example

```csv
Time,Headlines,Description
2020-01-01,"Market falls sharply","Stocks dropped after new trade concerns."
2020-01-02,"Oil prices rise","Energy markets reacted to supply expectations."
2020-01-03,"Tech firms announce earnings","Several companies released quarterly reports."
