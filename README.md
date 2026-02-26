# customer-behavior-analysis-sql-python
End-to-end customer behavior analysis project using MySQL and Python. Includes automated data ingestion, SQL-based analytics, engagement analysis, and sentiment analysis on customer reviews.

# 📊 Customer Behavior Analysis – ShopEasy

## 📌 Project Overview
This project analyzes customer behavior for an e-commerce platform (ShopEasy) using SQL and Python.  
The objective is to understand customer engagement, product performance, marketing effectiveness, and review sentiment.

---

## 🛠 Tools & Technologies
- MySQL
- Python
- Pandas
- SQLAlchemy
- TextBlob (Sentiment Analysis)

---

## 📂 Project Structure

project 1/
│
├── Data/
│   ├── customers.csv
│   ├── products.csv
│   ├── customer_journey.csv
│   ├── customer_reviews.csv
│   ├── engagement_data.csv
│   └── geography.csv
│
├── sql/
│   └── analysis.sql
│
├── data_loading.py
├── run_sql_analysis.py
├── sentiment_analysis.py
├── review_sentiment_output.csv
└── README.md

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
python -m textblob.download_corpora

2️⃣ Load Data into MySQL
python data_loading.py

3️⃣ Run SQL Analysis
python run_sql_analysis.py

4️⃣ Run Sentiment Analysis
python sentiment_analysis.py

📊 Key Results
🔹 Dataset Summary
Total Customers: 100
Total Products: 20
Total Reviews: 100
Average Rating: 3.73


🔹 Engagement Summary
Total Engagement Records: 100
Total Likes: 10,446
Average Likes per Record: 104.46

🔹 Top Campaign
Campaign 17 → 1,910 likes

🔹 Geography Distribution
Top Region: GeographyID 4 → 18 customers

Business Insights
Video marketing generates highest engagement.
Product 8 is highly rated and should be promoted more.
Product 7 has lowest rating and requires improvement.
Campaign 17 strategy should be replicated.
Newsletter content needs optimization.
Region 4 has highest customer concentration.
