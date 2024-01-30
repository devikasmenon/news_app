import pandas as pd
from sqlalchemy import create_engine

# Connect to the PostgreSQL database
engine = create_engine('postgresql://postgres:123456@localhost:5433/news_articles_db')

# Query data from the database
df = pd.read_sql_query("SELECT * FROM news_articles", engine)

# Export data to a CSV file
df.to_csv("news_articles.csv", index=False)
