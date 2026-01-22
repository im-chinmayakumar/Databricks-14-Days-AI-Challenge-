# Day 14 (22/01/26) – AI-Powered Analytics: Genie & Mosaic AI 🤖✨  
## Phase 4: AI & ML

## 📌 Overview
Day 14 concluded the Databricks 14 Days AI Challenge by exploring
**AI-powered analytics and Generative AI capabilities** in Databricks.

The focus was on using **natural language interfaces and AI models**
to enhance data exploration, analytics, and insights.

---

## 📘 What I Learned

- **Databricks Genie**  
  Used natural language queries to generate SQL and insights automatically.

- **Mosaic AI**  
  Explored Databricks’ GenAI capabilities for analytics and ML workflows.

- **Generative AI Integration**  
  Understood how GenAI enhances analyst productivity and insight discovery.

- **AI-Assisted Analysis**  
  Learned how conversational analytics changes how users interact with data.

---

## 🛠️ Hands-On Tasks

1. Queried datasets using natural language with Genie  
2. Explored Mosaic AI features  
3. Built a simple NLP task (sentiment analysis)  
4. Logged AI experiments using MLflow  

---

## 🧪 Practice & Implementation

### Genie – Natural Language Queries
Examples of queries used:
- *“Show me total revenue by category”*  
- *“Which products have the highest conversion rate?”*  
- *“What’s the trend of daily purchases over time?”*  
- *“Find customers who viewed but never purchased”*  

---

### Mosaic AI – NLP Example
```python
from transformers import pipeline
import mlflow

# Sentiment analysis example
classifier = pipeline("sentiment-analysis")
reviews = [
    "This product is amazing!",
    "Terrible quality, waste of money"
]

results = classifier(reviews)

# Log experiment to MLflow
with mlflow.start_run(run_name="sentiment_model"):
    mlflow.log_param("model", "distilbert-sentiment")
    mlflow.log_metric("accuracy", 0.95)  # Example metric
