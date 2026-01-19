# Day 11 (19/01/26) – Statistical Analysis & ML Preparation 📈  
## Phase 3: Advanced Analytics

## 📌 Overview
Day 11 focused on applying **statistical analysis and feature engineering**
to prepare data for **machine learning workflows**.
The objective was to understand data behavior, validate assumptions,
and engineer meaningful features.

---

## 📘 What I Learned

- **Descriptive Statistics**  
  Analyzed distributions and summary metrics to understand data patterns.

- **Hypothesis Testing**  
  Compared weekday vs weekend behavior to validate analytical assumptions.

- **Correlation Analysis**  
  Explored relationships between numerical features.

- **Feature Engineering**  
  Created time-based, behavioral, and transformed features for ML readiness.

---

## 🛠️ Hands-On Tasks

1. Calculated statistical summaries on event data  
2. Tested hypotheses (weekday vs weekend conversion behavior)  
3. Identified correlations between key variables  
4. Engineered features for downstream ML models  

---

## 🧪 Practice & Implementation

### Descriptive Statistics
```python
events.describe(["price"]).show()

Hypothesis Testing – Weekday vs Weekend
weekday = events.withColumn(
    "is_weekend",
    F.dayofweek("event_date").isin([1, 7])
)

weekday.groupBy("is_weekend", "event_type").count().show()

Correlation Analysis
events.stat.corr("price", "conversion_rate")

Feature Engineering for ML
from pyspark.sql.window import Window

features = events.withColumn("hour", F.hour("event_time")) \
    .withColumn("day_of_week", F.dayofweek("event_date")) \
    .withColumn("price_log", F.log(F.col("price") + 1)) \
    .withColumn(
        "time_since_first_view",
        F.unix_timestamp("event_time") -
        F.first("event_time")
         .over(Window.partitionBy("user_id").orderBy("event_time"))
    )

🎯 Key Takeaways

Statistical analysis helps validate assumptions before modeling

Hypothesis testing strengthens analytical conclusions

Feature engineering is critical for effective ML pipelines

ML preparation starts well before model training

🔧 Tools & Technologies

Databricks

Apache Spark

PySpark

Spark ML (conceptual)

Statistical Analysis
