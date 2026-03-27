# BERTopic Emerging Topic Dashboard

## Project Overview
This project develops an interactive dashboard for discovering hidden themes in text datasets using BERTopic. The system allows users to upload a CSV dataset, choose text and time columns, and run topic modeling to identify major topics, track how they change over time, and detect emerging trends.

The main goal of the project is to demonstrate practical data science skills in text preprocessing, topic modeling, trend analysis, data visualization, and dashboard design.

---

## Project Objectives
The dashboard was designed to answer three main questions:

1. What are the main topics present in the dataset?
2. How do these topics change over time?
3. Which topics appear to be emerging more rapidly than others?

By combining topic modeling with temporal analysis, the system moves beyond static clustering and provides more interpretable trend-based insights.

---

## Main Features
- Upload CSV datasets for analysis
- Select a main text column and optionally combine it with a second text column
- Select a valid time column for temporal trend analysis
- Run BERTopic topic modeling
- Display topic summary results
- Visualize top topics by frequency
- Show topics over time
- Show smoothed topic trends using exponential moving average
- Detect and rank emerging topics

---

## Why BERTopic Was Used
BERTopic was selected because it combines semantic embeddings, clustering, and keyword-based topic representation. Compared with traditional topic modeling methods, BERTopic can better capture meaning in short texts such as headlines or descriptions.

This makes it suitable for datasets where topics are not explicitly labeled and where understanding theme evolution over time is important.

---

## Why Time-Based Analysis Was Added
Topic modeling alone only identifies clusters of related documents. However, many real-world datasets also contain time information, which makes it possible to study how topics rise or decline.

For this reason, the project adds:
- topic-over-time analysis
- emerging-topic scoring
- exponential smoothing for trend interpretation

These components make the dashboard easier to use for trend discovery rather than only topic extraction.

---

## Folder Structure
```bash
bertopic-dashboard/
│
├── app/
│   └── main.py
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── topic_model.py
│   ├── trend_analysis.py
│   ├── visualization.py
│   └── utils.py
├── data/
├── outputs/
├── notebooks/
├── tests/
├── requirements.txt
└── README.md

```
