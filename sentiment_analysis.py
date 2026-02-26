import pandas as pd
import urllib.parse
from sqlalchemy import create_engine, text
from textblob import TextBlob

USERNAME = "root"
PASSWORD = urllib.parse.quote_plus("Venkat@123")
HOST = "localhost"
DB_NAME = "shopeasy"

engine = create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}"
)

# Load reviews
reviews = pd.read_sql("SELECT * FROM customer_reviews", engine)

# Try to find a review text column automatically
possible_text_cols = ["ReviewText", "review_text", "Review", "review", "Text", "text", "Comments", "comments"]
text_col = None
for c in reviews.columns:
    if c in possible_text_cols:
        text_col = c
        break

if text_col is None:
    # fallback: choose any object/string column (first one)
    obj_cols = [c for c in reviews.columns if reviews[c].dtype == "object"]
    if obj_cols:
        text_col = obj_cols[0]

if text_col is None:
    raise ValueError("No text column found in customer_reviews for sentiment analysis.")

def sentiment_score(x: str) -> float:
    return TextBlob(str(x)).sentiment.polarity

def sentiment_label(s: float) -> str:
    if s > 0:
        return "Positive"
    if s < 0:
        return "Negative"
    return "Neutral"

reviews["sentiment_score"] = reviews[text_col].apply(sentiment_score)
reviews["sentiment"] = reviews["sentiment_score"].apply(sentiment_label)

# Save output file
out_file = "review_sentiment_output.csv"
reviews.to_csv(out_file, index=False)

print("✅ Sentiment analysis completed.")
print("Text column used:", text_col)
print("Output saved as:", out_file)
print(reviews[["sentiment"]].value_counts())