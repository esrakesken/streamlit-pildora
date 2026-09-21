import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")
st.caption("Build Your First Interactive Data App with Streamlit — Píldora 1")

# --- Load data ---
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sales.csv")
    st.info("No file uploaded yet — showing the sample dataset below.")

# --- Filters ---
st.sidebar.header("Filters")
categories = df["Category"].unique()
selected = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)
filtered_df = df[df["Category"].isin(selected)]

# --- KPIs ---
total_sales = filtered_df["Sales"].sum()
avg_sales = filtered_df["Sales"].mean() if len(filtered_df) else 0
num_products = filtered_df["Product"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Average Sales", f"${avg_sales:,.0f}")
col3.metric("Products", num_products)

# --- Charts ---
st.subheader("Sales by Category")
sales_by_category = filtered_df.groupby("Category")["Sales"].sum()
st.bar_chart(sales_by_category)

st.subheader("Sales Distribution")
if len(filtered_df):
    fig = px.pie(filtered_df, names="Category", values="Sales")
    st.plotly_chart(fig, use_container_width=True)

# --- Raw data ---
st.subheader("Raw data")
st.dataframe(filtered_df, use_container_width=True)
