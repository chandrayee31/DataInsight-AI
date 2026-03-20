# 🚀 DataInsight AI

### AI-Powered Automated Data Analytics & Insight Engine

---

## 📌 Overview

DataInsight AI is an AI-powered analytics service that automatically analyzes tabular datasets and generates business insights using automated exploratory data analysis (EDA) and a locally hosted large language model via Ollama.

The system allows users to upload a CSV dataset through a FastAPI endpoint. The application performs automated data validation, computes statistical summaries using pandas, and converts those findings into human-readable insights such as executive summaries, key observations, business risks, and strategic recommendations.

The project demonstrates how traditional data analytics pipelines can be combined with generative AI systems to automate data interpretation and decision-support reporting.


---

## 🎬 Demo

<p align="center">
  <img src="readme_docs/datainsight_ai_GIF.gif" width="800"/>
</p>

---

## 🏗️ Architecture Diagram
```bash
CSV Upload
   ↓
FastAPI API
   ↓
Data Validation & Cleaning
   ↓
EDA using pandas
   ↓
Prompt Builder
   ↓
Ollama LLM
   ↓
Business Insights
   ↓
JSON API Response
```
<p align="center">
  <img src="readme_docs/datainsight_ai.gif" width="800"/>
</p>

---

## ✨ Key Features


- Automated data validation and preprocessing

- Exploratory Data Analysis (EDA) using pandas

- Aggregation of sales, profit, quantity, and category-level metrics

- Prompt orchestration for LLM-based interpretation

- Business insight generation using Ollama

- Structured API responses with Pydantic models

- Logging for production-style observability

- Docker containerization for deployment
---



## 📁 Project Structure

```bash
datainsight-ai/
├── Dockerfile
├── README.md
├── app
│   ├── api
│   │   └── routes.py
│   ├── config.py
│   ├── main.py
│   ├── models
│   │   ├── request_models.py
│   │   └── response_models.py
│   ├── prompts
│   │   └── insight_prompt.txt
│   ├── script.ipynb
│   ├── services
│   │   ├── analysis_service.py
│   │   ├── file_service.py
│   │   ├── llm_service.py
│   │   └── prompt_service.py
│   └── utils
│       ├── logger.py
│       └── validators.py
├── data
│   └── sample
│       ├── Groceries_dataset.csv
│       ├── Online Retail.xlsx
│       ├── ecommerce_sales_sample.csv
│       ├── olist_customers_dataset.csv
│       └── train.csv
├── docs
│   ├── api_examples.md
│   └── architecture.md
├── readme_docs
│   ├── datainsight_ai.gif
│   └── datainsight_ai_GIF.gif
├── requirements.txt
└── tests
```

---

## API Endpoints
```
Health Check
GET /health

Response:

{
 "status": "ok"
}
Analyze Dataset
POST /analyze

Upload a CSV dataset and receive automated insights.

Response Example:

{
 "summary": {
   "total_rows": 9994,
   "total_sales": 2297200,
   "total_profit": 286397,
   "top_region_sales": {
     "West": 725457,
     "East": 678781
   }
 },
 "insights": "Executive Summary... Key Observations... Recommendations..."
}
```
## How It Works
- User uploads a CSV dataset.

- The system validates the dataset and checks required columns.

- Pandas performs exploratory data analysis to compute key statistics.

- A structured prompt is generated from the dataset summary.

- The prompt is sent to a locally hosted LLM via Ollama.

- The LLM produces human-readable business insights.

- The API returns both the raw summary and generated insights.

## ⚙️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🐳 Docker

```bash
docker build -t datainsight-ai .
docker run -p 8000:8000 datainsight-ai
```

---
## 🚀 Future Improvements

- 📊 Excel dataset support  
- 📈 Visualization dashboards (Plotly / Streamlit)  
- 🗄️ BigQuery / SQL data source integration  
- 🤖 Anomaly detection using Machine Learning  
- 🔍 RAG-based analytics assistant  

## 👩‍💻 Author

Chandrayee Kumar  
Python Developer | AI/ML Engineer
