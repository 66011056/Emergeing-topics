# BERTopic Emerging Topic Dashboard

## Project Overview
This project develops an interactive dashboard for discovering hidden themes in text datasets using BERTopic. The system allows users to upload a CSV dataset, choose text and time columns, and run topic modeling to identify major topics, track how they change over time, and detect emerging trends.

The main goal of the project is to demonstrate practical data science skills in text preprocessing, topic modeling, trend analysis, data visualization, and dashboard design.


https://github.com/user-attachments/assets/ea9024e8-e695-4a11-8e26-cc221b9f1e00

// i have attached a video in case the files have issues.


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
---
This project adds: 
- **Topics Over Time** to show raw topic frequency changes
- **Smoothed Topic Trends** using exponential moving average (EMA)
- **Emerging Topic Detection** to identify fast-growing topics

  These additions make the dashboard more useful for understanding trends, not just topic clusters.

---
## Visual Outputs
<img width="1843" height="878" alt="Screenshot 2026-03-28 002804" src="https://github.com/user-attachments/assets/5a4d8f60-d38c-486a-b166-d94d1cf0ceb7" />
<img width="1848" height="880" alt="Screenshot 2026-03-28 002831" src="https://github.com/user-attachments/assets/35500f60-420a-4ab3-baf5-3efc3244e500" />

### Topic Summary
This table shows the discovered topics, how many documents belong to each topic, and the representative keywords for each topic. 


<img width="1822" height="931" alt="Screenshot 2026-03-28 002851" src="https://github.com/user-attachments/assets/7d2d5aba-f8c0-4dcc-a3bf-1532478f657f" />


### Emerging Topics Chart
This chart ranks the topics with the highest emerging scores, helping identify which topics are growing most rapidly. 

### Emerging Topics Table 
This table compares recent topic frequency with previous topic frequency and calculates the emerging score. 

<img width="1857" height="550" alt="Screenshot 2026-03-28 002907" src="https://github.com/user-attachments/assets/543a54eb-c14b-4283-bb45-b48908dd8ab5" />

### Top Topics by Count 
This bar chart highlights the most frequent topics in the selected dataset sample. 


<img width="1904" height="550" alt="Screenshot 2026-03-28 002932" src="https://github.com/user-attachments/assets/f78695d4-f0a3-40a2-8b3f-9f6f7bdd390e" />

### Topics Over Time 
This chart shows the raw frequency of the most important topics across time. 

<img width="1841" height="579" alt="Screenshot 2026-03-28 002950" src="https://github.com/user-attachments/assets/9f327e67-5ea1-43ee-8327-46f8615030f2" />


### Smoothed Topic Trends 
This chart applies **exponential moving average (EMA)** smoothing to reduce short-term noise and make long-term topic patterns easier to interpret. 

--- 

## Why Sampling Is Used BERTopic can be computationally expensive because it performs several processing steps, including: 
- text embedding
- dimensionality reduction
- clustering
- topic representation To improve speed and make the dashboard easier to use, this version allows the user to choose a sample size before training.

---

## Recommended Dataset Format The dashboard works best with a CSV file containing: 
- one text column such as headline, description, abstract, or title
- one valid date/time column

Example:
```bash
csv
Time,Headlines,Description
2020-01-01,"Market falls sharply","Stocks dropped after new trade concerns."
2020-01-02,"Oil prices rise","Energy markets reacted to supply expectations."
2020-01-03,"Tech firms announce earnings","Several companies released quarterly reports."
```
---

## How to Run the Project in the Terminal 

After downloading or extracting the project folder, open the folder in **Visual Studio Code**.

Then open the **terminal** in VS Code and run these commands step by step. 

### 1. Move into the project folder

powershell
```bash
cd $HOME\Downloads\bertopic-dashboard\bertopic-dashboard
```
--- 

### 2. Check that the files are there
powershell
```bash
dir
```
### 3. Install the required packages
powershell
```bash
py -m pip install -r requirements.txt
```
### 4. Run the Streamlit dashboard
powershell
```bash
py -m streamlit run app/main.py
```
