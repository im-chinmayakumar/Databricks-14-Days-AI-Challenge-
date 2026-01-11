# Databricks notebook source
events = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data",header=True,inferSchema=True, sep = ',')
display(events)

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

#Top 5 product by revenue
revenue =  events.filter(F.col("event_type") == "purchase")\
        .groupBy("product_id", "brand")\
        .agg(F.sum("price").alias("revenue"))\
        .orderBy(F.desc("revenue")).limit(5)
revenue.display()

# COMMAND ----------

#Running Total
Window = Window.partitionBy("user_id").orderBy("event_time")
events.withColumn("cumulative_event",F.count("*").over(Window)).display()

# COMMAND ----------

events = events.withColumn(
    "is_purchase",
    F.when(F.col("event_type") == "purchase", 1).otherwise(0)
)

events.select("event_type", "is_purchase").display()


# COMMAND ----------

df_customers = spark.read.csv("/FileStore/tables/customers.csv", header=True, inferSchema=True)
df_products  = spark.read.csv("/FileStore/tables/products.csv", header=True, inferSchema=True)


# COMMAND ----------

df_inner = df_sales.join(df_customers, "customer_id, inner")

# COMMAND ----------

df_left = df_sales.join(df_customers,"customer_id, left")

# COMMAND ----------

df_right = df_sales.join(df_customers,"customer_id, right")

# COMMAND ----------

df_outer = df_sales.join(df_customers,"customer_id, outer")

# COMMAND ----------

df_sales.columns
