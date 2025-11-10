# IDX AI Stock Prediction Web App

A simple Flask-based web application showcasing the top 10 Indonesian stock prediction AI and agent models with actionable short-term forecasts.

## Features

- Curated list of 10 AI/agent models focused on IDX stocks.
- Tabular display of expected percentage change and buy/sell/hold signals.
- Responsive Bootstrap-based layout with custom styling.
- Ready for deployment via WSGI (`wsgi.py`).

## Requirements

- Python 3.10+
- Pip

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
export FLASK_APP=wsgi:app
flask run --host=0.0.0.0 --port=5000
```

Alternatively, run directly with Python:

```bash
python wsgi.py
```

Open your browser to `http://localhost:5000` to view the dashboard.

## Deployment

Use the provided `wsgi.py` as the entrypoint for production servers such as Gunicorn or uWSGI:

```bash
gunicorn wsgi:app
```

## Disclaimer

All predictions shown are illustrative placeholders and should not be interpreted as financial advice.
