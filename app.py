import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Mapa de riesgo Barranquilla",
    page_icon="🗺️",
    layout="wide"
)

st.title("Mapa de riesgo de deslizamiento - Barranquilla")
st.caption("Visualización interactiva cargada desde archivo HTML")

# Ruta del archivo HTML dentro del repo
html_file = Path("mapa_riesgo_barranquilla.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    components.html(html_content, height=700, scrolling=True)
else:
    st.error("No se encontró el archivo 'mapa_riesgo_barranquilla.html' en el repositorio.")
