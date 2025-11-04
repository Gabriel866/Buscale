#!/usr/bin/env python

import altair as alt
import pandas as pd
import streamlit as st

# ------------------------------------------------------------
# Configuración de la página
# ------------------------------------------------------------
st.set_page_config(
    page_title="Biología – Botánica",
    layout="centered",
    page_icon="🌿"
)

# ------------------------------------------------------------
# Datos de ejemplo: Palabras clave de Biología y Botánica con ponderación
# ------------------------------------------------------------
@st.cache_data
def load_sample_data() -> pd.DataFrame:
    data = {
        "palabra_clave": [
            "Fotosíntesis",
            "Clorofila",
            "Transpiración",
            "Polinización",
            "Germinación",
            "Xilema",
            "Floema",
            "Estomas",
            "Tropismo",
            "Nutrientes del suelo",
            "Tejido vegetal",
            "Célula vegetal",
            "Plasma celular",
            "Semilla",
            "Flor",
            "Raíz",
            "Tallo",
            "Hoja",
            "Reproducción vegetal",
            "Adaptación de plantas"
        ],
        "descripcion": [
            "Proceso mediante el cual las plantas producen su alimento a partir de la luz solar.",
            "Pigmento verde responsable de la captación de energía solar en las hojas.",
            "Pérdida de agua por las hojas a través de los estomas.",
            "Transferencia de polen desde el estambre al pistilo.",
            "Proceso de desarrollo de una nueva planta a partir de una semilla.",
            "Tejido que transporta agua y minerales desde la raíz hasta las hojas.",
            "Tejido encargado de transportar nutrientes desde las hojas a toda la planta.",
            "Poros microscópicos en las hojas que permiten el intercambio gaseoso.",
            "Movimiento de las plantas en respuesta a estímulos externos.",
            "Elementos esenciales del suelo para el crecimiento vegetal.",
            "Conjunto de células que forman estructuras funcionales en la planta.",
            "Unidad básica de la estructura y función de las plantas.",
            "Sustancia que separa el núcleo del resto del citoplasma celular.",
            "Estructura que contiene el embrión de una nueva planta.",
            "Órgano reproductor de las plantas angiospermas.",
            "Parte de la planta que absorbe agua y minerales del suelo.",
            "Estructura que sostiene la planta y transporta nutrientes.",
            "Órgano encargado de la fotosíntesis y el intercambio de gases.",
            "Conjunto de mecanismos que permiten la formación de nuevas plantas.",
            "Capacidad de las plantas para ajustarse a diferentes condiciones ambientales."
        ],
        "ponderacion": [
            98, 95, 92, 90, 93, 89, 88, 87, 85, 84,
            83, 96, 82, 91, 90, 85, 86, 94, 89, 88
        ]
    }
    return pd.DataFrame(data)


def search_dataframe(df: pd.DataFrame, column: str, search_str: str) -> pd.DataFrame:
    """Buscar palabra dentro del DataFrame."""
    return df.loc[df[column].str.contains(search_str, case=False)]


def generate_barplot(results: pd.DataFrame, count_column: str, value_column: str):
    """Gráfico de barras de ponderación por palabra."""
    return (
        alt.Chart(results)
        .mark_bar(color="#4CAF50")
        .encode(
            y=alt.Y(f"{count_column}:N", sort="-x", title="Palabra clave"),
            x=alt.X(f"{value_column}:Q", title="Ponderación (%)"),
            tooltip=[f"{count_column}:N", f"{value_column}:Q"]
        )
        .properties(width=700, height=400)
        .interactive()
    )


# ------------------------------------------------------------
# Aplicación principal
# ------------------------------------------------------------
def app():
    st.title("🌿 Análisis de palabras clave de Biología – Botánica")
    st.write("Busca términos biológicos y botánicos y observa su ponderación de relevancia.")

    df = load_sample_data()

    with st.form(key="Buscar"):
        text_query = st.text_input(label="🔍 Ingresa una palabra para buscar (ej. 'hoja', 'raíz', 'fotosíntesis')")
        submit_button = st.form_submit_button(label="Buscar")

    if submit_button:
        with st.spinner("Buscando términos relacionados... 🌱"):
            results = search_dataframe(df, "palabra_clave", text_query)

        if len(results) > 0:
            st.success(f"✅ Se encontraron **{len(results)}** resultados.")
            st.table(results)
            st.altair_chart(generate_barplot(results, "palabra_clave", "ponderacion"))
        else:
            st.warning("⚠️ No se encontraron coincidencias. Prueba con otra palabra.")


# ------------------------------------------------------------
# Ejecutar la app
# ------------------------------------------------------------
if __name__ == "__main__":
    app()
