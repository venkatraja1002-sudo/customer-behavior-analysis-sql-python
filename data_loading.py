import pandas as pd
import urllib.parse
from sqlalchemy import create_engine

# Database connection
username = "root"
password = urllib.parse.quote_plus("Venkat@123")
host = "localhost"
database = "shopeasy"

engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
)

# Load actual CSV files
customers = pd.read_csv("Data/customers.csv")
products = pd.read_csv("Data/products.csv")
customer_journey = pd.read_csv("Data/customer_journey.csv")
customer_reviews = pd.read_csv("Data/customer_reviews.csv")
engagement_data = pd.read_csv("Data/engagement_data.csv")
geography = pd.read_csv("Data/geography.csv")

# Insert into database
customers.to_sql("customers", engine, if_exists="replace", index=False)
products.to_sql("products", engine, if_exists="replace", index=False)
customer_journey.to_sql("customer_journey", engine, if_exists="replace", index=False)
customer_reviews.to_sql("customer_reviews", engine, if_exists="replace", index=False)
engagement_data.to_sql("engagement_data", engine, if_exists="replace", index=False)
geography.to_sql("geography", engine, if_exists="replace", index=False)

print("✅ Data Loaded Successfully!")