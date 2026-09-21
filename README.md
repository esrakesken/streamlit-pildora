# Streamlit Sales Dashboard

**FactoriaF5 — IA Bootcamp · Píldora 1/4**

A small interactive dashboard built with [Streamlit](https://streamlit.io): upload a CSV,
filter it by category, and see live KPIs and charts update instantly.

🎞️ Slides: *[add your deck link here]*
🌐 Live app: *[add your Streamlit Community Cloud link here, once deployed]*

## What it does

- Upload your own CSV, or the app falls back to the sample dataset in `data/sales.csv`
- Filter the data by category from the sidebar
- See Total Sales, Average Sales and Product count update live
- Bar chart of sales by category
- Pie chart of sales distribution

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL Streamlit prints in your terminal (usually `http://localhost:8501`).

## Project structure

```
streamlit-pildora/
├── app.py
├── data/
│   └── sales.csv
├── requirements.txt
└── README.md
```

## Deploy for free

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub.
3. Click "New app", pick this repo and `app.py`, and deploy.
