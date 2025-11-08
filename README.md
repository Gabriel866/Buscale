## Materia 
Programación logica funcional 7 SS
## Maestro
Guillermo Alejandro, Chavez Sanchez
## Alumno
Gabriel Enrique Lugo López
## Proyecto
Buscador de tesxto sobre biología y botánica desarrollado en Python – Streamlit.


# Análisis de texto y palabras calve de Biología – Botánica

Aplicación interactiva desarrollada en Python con Streamlit, diseñada para explorar palabras clave y texto relacionadas con biología y botánica, mostrando su descripción y nivel de relevancia y ponderación.

El proyecto fue actualizado para incluir una nueva funcionalidad de análisis de texto completo, complementando la búsqueda de palabras clave ya existente.

Permite realizar búsquedas por palabra o texto y visualizar los resultados en forma de tabla y gráfico de barras dinámico utilizando Altair.

## Cambios en la actualizacón

Esta versión incluye una **nueva funcionalidad de análisis de texto completo**, que complementa la búsqueda por palabra clave ya existente.

### Nueva analizador de texto

Permite ingresar un **párrafo o texto completo**.  
- Detecta automáticamente las **palabras clave** relacionadas con Biología y Botánica.  
- Calcula un **puntaje total de relevancia** en función de las ponderaciones asociadas a cada palabra.  
- Clasifica el texto según su relación con el tema:

  | Puntaje total | Clasificación |
  |----------------|-----------------------------|
  | 0              | Sin relación |
  | 1–199          | Relación leve |
  | 200–499        | Relación moderada |
  | 500 o más      | Alta relación  |

  ### Nueva visualización

  Tabla de palabras clave detectadas con su ponderación.  
- Gráfico de barras dinámico generado con **Altair** para visualizar la relevancia de cada término.

  ### Mejora del flujo de la app

  Buscar conceptos clave y texto de biología y botánica.  
- Mostrar descripciones breves de cada término.  
- Visualizar su ponderación o grado de relevancia mediante un gráfico interactivo.  
- Analizar textos completos y determinar su relación con el tema Biología–Botánica.

## Descripción del Proyecto

Este proyecto tiene como objetivo ofrecer una herramienta educativa que permita:

Buscar conceptos clave y texto de biología y botánica.

Mostrar descripciones breves de cada término.

Visualizar su ponderación o grado de relevancia mediante un gráfico interactivo.



## Tecnologías Utilizadas

Python 3.9+

Streamlit – interfaz web interactiva

Altair – visualización de datos

Pandas – manipulación de datos

## Requisitos Previos

Asegúrate de tener instalado Python 3.9 o superior.
Luego, instala las dependencias necesarias ejecutando: pip install streamlit altair pandas


## Ejecución del Proyecto

Guarda el archivo con el nombre buscale.py.

Se abre una terminal en la carpeta donde se encuentre el archivo y/o desde la consola del visual studio code.

Ejecuta el siguiente comando: streamlit run buscale.py y/o en CMD : streamlit run buscale.py 


## Ejemplo de Uso

En la barra de búsqueda (Escribe o pega un texto para analizar), escribe una palabra como hoja, raíz o fotosíntesis o un texto.

Presiona Analizar texto.

Se mostrará una tabla con los resultados y un gráfico con la ponderación de las palabras coincidentes.









