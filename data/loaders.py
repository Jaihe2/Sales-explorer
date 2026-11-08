"""Carga y limpieza de datos. Sin código de interfaz, salvo el decorador de caché."""
from pathlib import Path

import pandas as pd
import streamlit as st

# El CSV vive en la raíz del repo, junto a app.py.
DEFAULT_PATH = Path(__file__).resolve().parents[1] / "sales_daily.csv"


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Función pura (fácil de probar): quita duplicados y unidades negativas y recalcula revenue."""
    out = df.drop_duplicates().copy()
    out = out[out["units"] >= 0]
    out["revenue"] = (out["units"] * out["unit_price"]).round(2)
    return out.reset_index(drop=True)


@st.cache_data(show_spinner="Cargando ventas...")
def load_sales(path: str = str(DEFAULT_PATH)) -> pd.DataFrame:
    return clean_sales(pd.read_csv(path, parse_dates=["date"]))
