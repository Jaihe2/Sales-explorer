# Sales Explorer

App de Streamlit para explorar ventas diarias (filtros por región y categoría, KPIs, unidades diarias y top 10 de SKUs por ingresos).

## Estructura
```
app.py                  # solo conecta: config, filtros, KPIs y llamadas
data/loaders.py         # clean_sales + load_sales (@st.cache_data)
components/charts.py    # daily_units_chart, top_skus_chart
sales_daily.csv
requirements.txt
```
Correr: `pip install -r requirements.txt && streamlit run app.py`

## Comparación con `session1/activity2_solution`

1. **Ruta del CSV.** La solución lee la ruta desde la variable de entorno `SALES_CSV` y, si no existe, usa un archivo dentro de `data/` del kit. Yo la dejé fija (`sales_daily.csv` junto a `app.py`) porque mi app solo corre en un lugar y Streamlit Cloud no necesita variables extra; menos configuración, menos puntos de falla.
2. **Gráfica de top SKUs.** La solución usa barras verticales con el SKU en el eje x. Yo la dejé horizontal y ordenada de menor a mayor, porque con 10 SKUs las etiquetas se leen mejor y el más vendido queda arriba.
