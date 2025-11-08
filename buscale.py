#!/usr/bin/env python

import altair as alt
import pandas as pd
import streamlit as st
import re

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
            "Fotosíntesis", "Clorofila", "Transpiración", "Polinización", "Germinación",
            "Xilema", "Floema", "Estomas", "Tropismo", "Nutrientes del suelo",
            "Tejido vegetal", "Célula vegetal", "Plasma celular", "Semilla", "Flor",
            "Raíz", "Tallo", "Hoja", "Reproducción vegetal", "Adaptación de plantas"
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


def analyze_text(df: pd.DataFrame, text: str):
    """
    Analiza el texto ingresado y calcula un puntaje de relevancia
    basado en las coincidencias con las palabras clave.
    """
    text = text.lower()
    total_score = 0
    matches = []

    for _, row in df.iterrows():
        word = row["palabra_clave"].lower()
        weight = row["ponderacion"]
        # Buscar coincidencias parciales (palabra o fragmento)
        if re.search(rf"\b{re.escape(word)}\b", text):
            total_score += weight
            matches.append((row["palabra_clave"], weight))

    if total_score == 0:
        return total_score, matches, "No se detecta relación con Biología – Botánica."
    elif total_score < 200:
        return total_score, matches, "Relación leve con Biología – Botánica 🌱"
    elif total_score < 500:
        return total_score, matches, "Relación moderada con Biología – Botánica 🌿"
    else:
        return total_score, matches, "Alta relación con Biología – Botánica 🌳"


# ------------------------------------------------------------
# Aplicación principal
# ------------------------------------------------------------
def app():
    st.title("🌿 Analizador de texto – Biología y Botánica")
    st.write("Ingresa un texto y el sistema analizará si pertenece al tema de Biología–Botánica.")

    df = load_sample_data()

    text_input = st.text_area("✏️ Escribe o pega un texto para analizar:", height=200)
    if st.button("Analizar texto"):
        if text_input.strip() == "":
            st.warning("Por favor ingresa un texto para analizar.")
        else:
            score, found, message = analyze_text(df, text_input)

            st.subheader("🔎 Resultado del análisis:")
            st.info(message)
            st.write(f"**Puntaje total:** {score}")

            if found:
                st.success(f"Palabras detectadas ({len(found)}):")
                st.table(pd.DataFrame(found, columns=["Palabra clave", "Ponderación"]))
            else:
                st.warning("No se encontraron palabras clave relacionadas.")

            # Mostrar gráfico si hay coincidencias
            if found:
                found_df = pd.DataFrame(found, columns=["palabra_clave", "ponderacion"])
                chart = (
                    alt.Chart(found_df)
                    .mark_bar(color="#4CAF50")
                    .encode(
                        y=alt.Y("palabra_clave:N", sort="-x", title="Palabra clave"),
                        x=alt.X("ponderacion:Q", title="Ponderación (%)"),
                        tooltip=["palabra_clave:N", "ponderacion:Q"]
                    )
                    .properties(width=700, height=400)
                )
                st.altair_chart(chart)

# ------------------------------------------------------------
# Ejecutar la app
# ------------------------------------------------------------
if __name__ == "__main__":
    app()
