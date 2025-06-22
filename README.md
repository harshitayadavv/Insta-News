# 📰 Insta-News

Insta-News is a simple and elegant Flask-based web app that displays the latest news headlines using the [NewsAPI](https://newsapi.org/). Users can search for topics, browse categories, and view news cards styled with Bootstrap and custom SCSS.

---

## 📸 Project Demo

https://insta-news.onrender.com

---

## 🚀 Features

- Search the latest news articles by keyword
- Filter out irrelevant or unwanted news sources
- Clean, responsive UI using Bootstrap 5
- Category-based quick filters (e.g., Sports, Tech, Finance)
- Custom styling with SCSS

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML & Jinja2
- Bootstrap 5
- SCSS (compiled to CSS)
- NewsAPI

---

## 🔧 Installation and Setup

Follow the steps below to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/insta-news.git
cd insta-news
### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv flask_news
flask_news\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv flask_news
source flask_news/bin/activate
```

---

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, generate one with:

```bash
pip freeze > requirements.txt
```

---

### 4. API Key Setup

1. Get your free API key from [https://newsapi.org/](https://newsapi.org/)
2. Create a new file named `config.py` in the root of your project.
3. Add your API key inside it like this:

```python
NEWS_API_KEY = "your_api_key_here"
```

> ⚠️ **Important:** Do NOT upload `config.py` to GitHub or share it publicly.

---

### 5. Run the App

```bash
python app.py
```

Now open your browser and go to:

```bash
http://127.0.0.1:5000/
```



