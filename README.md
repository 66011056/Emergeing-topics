# BERTopic Emerging Topic Dashboard

## Overview
This project is an interactive text analytics dashboard built with **Streamlit** and **BERTopic**.  
It allows a user to upload a CSV dataset, choose a text column and a time column, and then run topic modeling to discover major themes in the data.

The dashboard is designed to answer three practical questions:

1. What are the main topics in the dataset?
2. How do those topics change over time?
3. Which topics are emerging more quickly than others?

This version of the project focuses on **clear topic interpretation** and **simpler trend visualization**.  
Instead of using a complex hierarchical topic chart, the dashboard emphasizes:

- topic summary
- emerging topics chart
- emerging topics table
- top topics by count
- topics over time
- smoothed topic trends

---

## Project Goal
The main goal of this project is to demonstrate practical **data science and NLP skills** by combining:

- text preprocessing
- transformer-based topic modeling
- time-based trend analysis
- data visualization
- dashboard design

The project is especially useful for datasets such as:

- news headlines
- article descriptions
- research abstracts
- short text records with timestamps

---

## Why BERTopic
BERTopic was chosen because it can generate topics from text using semantic embeddings rather than only word counts. This makes it more suitable for short text data such as headlines and descriptions.

Compared with traditional topic modeling methods, BERTopic provides:

- more meaningful topic grouping
- interpretable keyword-based topic labels
- integration with time-based topic analysis

This makes it a strong choice for discovering patterns in unlabeled text data.

---

## Why Time-Based Trend Analysis
Topic modeling alone only tells us what themes exist in the dataset.  
However, many real-world text datasets also contain time information, which allows us to study how those themes change.

This project adds:

- **Topics Over Time** to show raw topic frequency changes
- **Smoothed Topic Trends** using exponential moving average (EMA)
- **Emerging Topic Detection** to identify fast-growing topics

These additions make the dashboard more useful for understanding trends, not just topic clusters.

---

## Main Features
- Upload a CSV dataset
- Automatically detect text and time columns
- Select one main text column
- Optionally combine it with another text column
- Sample the dataset for faster training
- Train a BERTopic model
- Display topic summary results
- Show top topics by count
- Show topics over time
- Show smoothed topic trends
- Detect emerging topics with a growth score

---

## Dashboard Workflow
The dashboard follows this process:

1. Load the dataset from CSV
2. Detect text columns and possible time columns
3. Clean and preprocess the selected text
4. Convert timestamps into usable time format
5. Train BERTopic on the processed documents
6. Generate topic summary information
7. Compute topics over time
8. Calculate emerging-topic scores
9. Visualize the results in the dashboard

---

## Visual Outputs

### Topic Summary
This table shows the discovered topics, how many documents belong to each topic, and the representative keywords for each topic.

### Emerging Topics Chart
This chart ranks the topics with the highest emerging scores, helping identify which topics are growing most rapidly.

### Emerging Topics Table
This table compares recent topic frequency with previous topic frequency and calculates the emerging score.

### Top Topics by Count
This bar chart highlights the most frequent topics in the selected dataset sample.

### Topics Over Time
This chart shows the raw frequency of the most important topics across time.

### Smoothed Topic Trends
This chart applies **exponential moving average (EMA)** smoothing to reduce short-term noise and make long-term topic patterns easier to interpret.

---

## Why the Hierarchy Chart Was Removed
An earlier version included hierarchical topic visualization. However, that chart was difficult to interpret clearly, especially for short-text datasets such as news headlines. To improve usability and make the results easier to explain, this version replaces the hierarchy view with simpler and more practical charts focused on topic counts and temporal trends.

---

## Why Sampling Is Used
BERTopic can be computationally expensive because it performs several processing steps, including:

- text embedding
- dimensionality reduction
- clustering
- topic representation

To improve speed and make the dashboard easier to use, this version allows the user to choose a sample size before training.

---

## Recommended Dataset Format
The dashboard works best with a CSV file containing:

- one text column such as `headline`, `description`, `abstract`, or `title`
- one valid date/time column

Example:

```csv
Time,Headlines,Description
2020-01-01,"Market falls sharply","Stocks dropped after new trade concerns."
2020-01-02,"Oil prices rise","Energy markets reacted to supply expectations."
2020-01-03,"Tech firms announce earnings","Several companies released quarterly reports."
