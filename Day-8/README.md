# Day 8 (16/01/26) – Unity Catalog & Data Governance 🔐  
## Phase 2: Data Engineering

## 📌 Overview
Day 8 focused on **data governance and access control** using **Unity Catalog** in Databricks.
The goal was to understand how enterprise data platforms manage security, permissions,
and lineage across data assets.

---

## 📘 What I Learned

- **Catalog → Schema → Table Hierarchy**  
  Learned how data is logically organized and governed within Databricks.

- **Access Control (GRANT / REVOKE)**  
  Understood role-based permissions and how access is managed at different levels.

- **Managed vs External Tables**  
  Compared ownership, storage responsibility, and governance implications.

- **Data Lineage**  
  Explored lineage for traceability, auditing, and compliance use cases.

---

## 🛠️ Hands-On Tasks

1. Created logical catalog and schema structures (conceptual)  
2. Registered Delta tables  
3. Explored permission models for secure access  
4. Created views to expose curated data instead of raw tables  

---

## 🧪 Practice & Implementation Notes

> ⚠️ **Databricks Community Edition Limitation**

Full Unity Catalog features (catalogs, principals, GRANT/REVOKE enforcement)
are available in **enterprise Databricks environments**.

To apply governance concepts practically:
- Simulated access control using curated **Gold-layer views**
- Avoided exposing raw or Silver-layer tables directly
- Followed governance-first design principles

---

## 🎯 Key Takeaways

- Data governance is essential for enterprise data platforms
- Unity Catalog centralizes access control and metadata
- Views are an effective way to expose controlled data access
- Governance should be designed alongside data pipelines

---

## 🔧 Tools & Technologies

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog (conceptual / simulated)
- Lakehouse Architecture

---

## 📅 Challenge Progress

- **Challenge:** Databricks 14 Days AI Challenge  
- **Phase:** Phase 2 – Data Engineering  
- **Day Completed:** Day 8

---

## 🔗 Resources

- Databricks Unity Catalog Documentation  
- Databricks Data Governance Guide  
