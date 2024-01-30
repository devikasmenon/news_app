from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import cast, VARCHAR
# Instead of this import:
# from sqlalchemy.ext.declarative import declarative_base

# Use this import:
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)
    publication_date = Column(DateTime)
    source_url = Column(String)

# Create database engine
engine = create_engine('postgresql://postgres:123456@localhost:5433/news_articles_db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Function to store news articles in the database
from sqlalchemy import cast, VARCHAR

# Inside your store_articles function
# Inside your store_articles function
def store_articles(articles):
    for article in articles:
        article_id = hash(article["title"] + article["source_url"])
        if not session.query(NewsArticle).filter_by(id=str(article_id)).first():
            # Remove 'GMT' from the date string
            publication_date_str = article["publication_date"].replace(' GMT', '')
            new_article = NewsArticle(
                id=str(article_id),
                title=article["title"],
                content=article["content"],
                # Use a different format string without the timezone
                publication_date=datetime.strptime(publication_date_str, "%a, %d %b %Y %H:%M:%S"),
                source_url=article["source_url"]
            )
            session.add(new_article)
    session.commit()


# Example usage:
if __name__ == "__main__":
    # Assuming 'news_articles' is a list of articles collected using feedparser_script.py
    news_articles = [
        {"title": "Title 1", "content": "Content 1", "publication_date": "Tue, 01 Feb 2022 12:00:00 GMT", "source_url": "http://example.com/article1"},
        {"title": "Title 2", "content": "Content 2", "publication_date": "Wed, 02 Feb 2022 12:00:00 GMT", "source_url": "http://example.com/article2"},
    ]
    store_articles(news_articles)
