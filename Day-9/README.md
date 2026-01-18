# Day 9 (17/01/26) – SQL Analytics & Dashboards 📊  
## Phase 3: Advanced Analytics

## 📌 Overview
Day 9 marked the start of **Phase 3: Advanced Analytics**, focusing on using **Databricks SQL**
to transform curated data into **business insights** through analytical queries and dashboards.

---

## 📘 What I Learned

- **SQL Warehouses**  
  Learned how Databricks SQL warehouses execute scalable and performant analytical queries.

- **Complex Analytical Queries**  
  Used CTEs, window functions, and aggregations for trend and funnel analysis.

- **Dashboard Creation**  
  Built dashboards to track revenue trends, funnels, and top-performing products.

- **Visualizations & Filters**  
  Added filters and scheduled refreshes to make dashboards interactive and business-ready.

---

## 🛠️ Hands-On Tasks

1. Created a Databricks SQL warehouse  
2. Wrote analytical queries on Gold and Silver tables  
3. Built dashboards for revenue trends, funnels, and top products  
4. Added filters and scheduled automatic refresh  

---

## 🧪 Practice & Implementation

### Revenue Trend with 7-Day Moving Average
```sql
WITH daily AS (
  SELECT event_date, SUM(revenue) AS rev
  FROM gold.products
  GROUP BY event_date
)
SELECT
  event_date,
  rev,
  AVG(rev) OVER (
    ORDER BY event_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS ma7
FROM daily;

---
### Conversion Funnel Analysis
```sql
SELECT
  category_code,
  SUM(views) AS views,
  SUM(purchases) AS purchases,
  ROUND(SUM(purchases) * 100.0 / SUM(views), 2) AS conversion_rate
FROM gold.products
GROUP BY category_code;
---

Customer Segmentation (LTV-Based)
SELECT
  CASE
    WHEN cnt >= 10 THEN 'VIP'
    WHEN cnt >= 5 THEN 'Loyal'
    ELSE 'Regular'
  END AS tier,
  COUNT(*) AS customers,
  AVG(total_spent) AS avg_ltv
FROM (
  SELECT
    user_id,
    COUNT(*) AS cnt,
    SUM(price) AS total_spent
  FROM silver.events
  WHERE event_type = 'purchase'
  GROUP BY user_id
)
GROUP BY tier;


---

## 📊 Dashboard – SQL Analytics & Insights

I built an interactive Databricks SQL dashboard showcasing:
- Revenue trends with moving averages
- Conversion funnel analysis
- Top-performing products and categories
- Customer segmentation insights

🔗 **Live Dashboard (Published):**  
https://dbc-c69cfbfa-4d4a.cloud.databricks.com/dashboardsv3/01f0f36bf3451171a3bddb8d18f0eb50/published?o=7474650645919341

> Note: Dashboard is published for view-only access.

