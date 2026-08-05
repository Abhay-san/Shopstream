# E-commerce Orders — Streamlit Dashboard

Interactive EDA dashboard for the e-commerce orders dataset, built with Streamlit + Plotly.

## Files

- `app.py` — the Streamlit dashboard
- `ecommerce_orders_dataset.csv` — the dataset
- `EDA_ecommerce_orders.ipynb` — Jupyter notebook with the full exploratory analysis
- `requirements.txt` — Python dependencies for Streamlit Cloud

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repo (see steps below).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, pick this repo/branch, and set the main file to `app.py`.
4. Click **Deploy**.
