from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("NEWS_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query', 'latest')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return render_template('index.html', articles=[], query=query, error="Failed to fetch news.")
    
    news_data = response.json()
    articles = news_data.get('articles', [])

    # Filter out Yahoo articles and articles with "removed" in the title
    filtered_articles = [
        article for article in articles 
        if 'Yahoo' not in article['source']['name'] and 'removed' not in article['title'].lower()
    ]

    return render_template('index.html', articles=filtered_articles, query=query)

if __name__ == '__main__':
    app.run(debug=True)
