# Dashboard de Acciones Argentinas - Panel Líder
# Versión Inicial con datos falsos y placeholder para API de IOL

import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Título principal
st.set_page_config(page_title="Dashboard Panel Líder ARG", layout="wide")
st.title("🇦🇷 Panel Líder - Dashboard Financiero Inteligente")

st.markdown("""
Este sistema analiza empresas argentinas del panel líder.
Utilizamos indicadores clave para definir el atractivo de inversión de cada acción.
Próximamente estará conectado a la API de IOL para obtener datos en tiempo real.
""")

# Placeholder de datos simulados
data = {
    "Ticker": ["GGAL", "YPF", "PAMP", "IRSA"],
    "Empresa": ["Grupo Galicia", "YPF Sociedad Anónima", "Pampa Energía", "IRSA"],
    "Precio": [5520, 38375, 2330, 1455],
    "Cambio 7D (%)": [-5.7, 6.1, 3.2, 6.1],
    "Cambio 1Y (%)": [81.5, 53.2, 71.6, 45.3],
    "% Atractivo": [88, 74, 81, 32],
    "Valor Intrínseco": [10500, 56200, 3930, 0],
    "Recomendación": [
        "Muy infravalorada. Comprar ahora.",
        "Potencial de suba. Comprar con cautela.",
        "Buen momento para mantener posición.",
        "Sobrevalorada. Esperar para entrar."
    ]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mapa de calor del % de atractivo
st.subheader("Mapa de Atractivo de Inversión")
colors = df["% Atractivo"].apply(lambda x: "🟢" if x >= 70 else ("🟡" if x >= 50 else "🔴"))
df_color = df[["Ticker", "% Atractivo"]].copy()
df_color["Atractivo"] = colors
st.dataframe(df_color.set_index("Ticker"))

# Tabla completa con recomendaciones
st.subheader("Detalles por Acción")
st.dataframe(df.set_index("Ticker"))

# Placeholder para conexión a la API de IOL
st.markdown("""
---
### 🚧 Conexión a IOL API
**Estado:** *Pendiente de clave y habilitación de IP.*
Una vez habilitado, los datos serán en tiempo real desde tu cuenta IOL.
---
""")
