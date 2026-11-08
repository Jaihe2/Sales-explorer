"""Activity 1: Sales Explorer (una sola app, estilo notebook)."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA = Path(__file__).parent / "sales_daily.csv"

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

df = pd.read_csv(DATA, parse_dates=["date"])

# Filtros (TODO 1 y 2)
st.sidebar.header("Filtros")
regions = sorted(df["region"].unique())
categories = sorted(df["category"].unique())
sel_regions = st.sidebar.multiselect("Región", regions, default=regions, key="f_region")
sel_categories = st.sidebar.multiselect("Categoría", categories, default=categories, key="f_category")

df = df[df["region"].isin(sel_regions) & df["category"].isin(sel_categories)]

if df.empty:
    st.warning("Los filtros no devuelven filas. Selecciona al menos una región y una categoría.")
    st.stop()

# KPIs (TODO 3)
c1, c2, c3 = st.columns(3)
c1.metric("Unidades", f"{df['units'].sum():,.0f}")
c2.metric("Ingresos", f"${df['revenue'].sum():,.0f}")
c3.metric("SKUs", df["sku"].nunique())

# Gráfica de unidades diarias
daily = df.groupby("date", as_index=False)["units"].sum()
fig = px.line(daily, x="date", y="units", title="Daily units")
st.plotly_chart(fig, width="stretch")

# Top 10 SKUs por ingresos (TODO 4)
top = (
    df.groupby("sku", as_index=False)["revenue"].sum()
    .nlargest(10, "revenue")
    .sort_values("revenue")
)
fig2 = px.bar(top, x="revenue", y="sku", orientation="h", title="Top 10 SKUs por ingresos")
st.plotly_chart(fig2, width="stretch")

# Filas filtradas (TODO 5, opcional)
with st.expander("Ver filas filtradas"):
    st.dataframe(df, width="stretch")
