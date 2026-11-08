"""Sales Explorer: app.py solo conecta las piezas (config, filtros, KPIs, gráficas)."""
import streamlit as st

from components.charts import daily_units_chart, top_skus_chart
from data.loaders import load_sales

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

df = load_sales()

with st.sidebar:
    st.header("Filtros")
    all_regions = sorted(df["region"].unique())
    all_categories = sorted(df["category"].unique())
    regions = st.multiselect("Región", all_regions, default=all_regions, key="f_region")
    categories = st.multiselect("Categoría", all_categories, default=all_categories, key="f_category")

view = df[df["region"].isin(regions) & df["category"].isin(categories)]
if view.empty:
    st.warning("Los filtros no devuelven filas. Selecciona al menos una región y una categoría.")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("Unidades", f"{view['units'].sum():,.0f}")
c2.metric("Ingresos", f"${view['revenue'].sum():,.0f}")
c3.metric("SKUs", view["sku"].nunique())

st.plotly_chart(daily_units_chart(view), width="stretch")
st.plotly_chart(top_skus_chart(view), width="stretch")

with st.expander("Ver filas filtradas"):
    st.dataframe(view, width="stretch")
