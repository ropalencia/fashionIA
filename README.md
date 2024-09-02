# Sistema de Recomendación de Moda Basado en Deep Learning

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un sistema de recomendación de moda para mitigar la "parálisis por análisis" que enfrentan los consumidores en plataformas de comercio electrónico. Utilizando técnicas avanzadas de deep learning y procesamiento de lenguaje natural (NLP), el sistema ofrece recomendaciones personalizadas de productos de moda, adaptándose a las tendencias actuales y las preferencias del usuario.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Análisis de Requisitos del Sistema](#análisis-de-requisitos-del-sistema)
3. [Diagrama de Arquitectura](#diagrama-de-arquitectura)
4. [Evidencias de Pruebas Funcionales](#evidencias-de-pruebas-funcionales)
5. [Exploratory Data Analysis (EDA) y Visualización](#eda-and-visualization)
6. [Desarrollo del Modelo](#desarrollo-del-modelo)
    - [Partición de los Datos](#partición-de-los-datos)
    - [Preparador del Generador de Imágenes](#preparador-del-generador-de-imagenes)
    - [Configuración del Modelo Base y Arquitectura Final](#configuración-del-modelo-base-y-arquitectura-final)
    - [Extracción de Características de las Imágenes y Guardado](#extracción-de-características-de-las-imágenes-y-guardado)
    - [Reducción de Dimensionalidad](#reducción-de-dimensionalidad)
    - [Entrenamiento del Modelo de Clasificación K-Nearest Neighbors (KNN)](#entrenamiento-del-modelo-de-clasificación-k-nearest-neighbors-knn)
7. [Implementación del Modelo](#implementación-del-modelo)
    - [Ejemplo de Recomendación 1](#ejemplo-de-recomendación-1)
    - [Ejemplo de Recomendación 2](#ejemplo-de-recomendación-2)
    - [Ejemplo de Recomendación 3](#ejemplo-de-recomendación-3)
8. [Conclusión](#conclusión)
9. [Contribución Individual](#contribución-individual)
10. [Autores](#autores)

## Introducción

En este proyecto, abordamos el problema de la parálisis por análisis en el comercio electrónico de moda, desarrollando un sistema de recomendación basado en deep learning. Este sistema está diseñado para ofrecer recomendaciones personalizadas que reflejen las preferencias del usuario y las tendencias actuales de la moda, mejorando la experiencia de compra en línea.

## Análisis de Requisitos del Sistema

### Requisitos Funcionales
- El sistema debe analizar interacciones y comportamientos de compra para ofrecer recomendaciones personalizadas.
- Debe filtrar y presentar solo productos alineados con las preferencias del usuario.
- Ofrecer una plataforma dinámica que permita descubrir nuevas tendencias y diseñadores.
- Adaptarse a las tendencias globales y cambios en el comportamiento del usuario.

### Requisitos No Funcionales
- Recuperarse rápidamente de fallos con un mínimo de interrupciones.
- Ser escalable y manejar grandes volúmenes de usuarios y datos.
- Estar disponible en todo momento con un tiempo de inactividad mínimo.
- Proporcionar recomendaciones en el menor tiempo posible.

## Diagrama de Arquitectura

(Insertar imagen del diagrama de arquitectura aquí)

El diagrama muestra la estructura del sistema, incluyendo la base de datos, los módulos de deep learning, y los flujos de datos. La base de datos proviene de múltiples fuentes, y se integra mediante procesos de ETL (Extract, Transform, Load).

## Evidencias de Pruebas Funcionales

Capturas de pantalla y logs que muestran la ejecución de pruebas funcionales para validar que el sistema cumple con los requisitos establecidos.

## EDA and Visualization

Se realizó un análisis exploratorio de los datos para entender la distribución y características de los mismos. Esto incluyó la visualización de las categorías de productos y sus relaciones.

## Desarrollo del Modelo

### Partición de los Datos
El 80% de los datos se utilizó para entrenamiento y el 20% para validación.

### Preparador del Generador de Imágenes
Se utilizaron técnicas de preprocesamiento de imágenes para normalizarlas y redimensionarlas, mejorando la eficiencia del modelo.

### Configuración del Modelo Base y Arquitectura Final
Se empleó la red preentrenada VGG16, ajustada para la tarea específica del proyecto.

### Extracción de Características de las Imágenes y Guardado
Se extrajeron características utilizando VGG16 y se guardaron para su posterior uso.

### Reducción de Dimensionalidad
Se aplicó PCA para reducir la dimensionalidad a 200 componentes, explicando el 99% de la varianza.

### Entrenamiento del Modelo de Clasificación K-Nearest Neighbors (KNN)
Se entrenó un modelo KNN para clasificar las imágenes en diferentes categorías.

## Implementación del Modelo

### Ejemplo de Recomendación 1
(Visualizar resultados)

### Ejemplo de Recomendación 2
(Visualizar resultados)

### Ejemplo de Recomendación 3
(Visualizar resultados)

## Conclusión

El modelo mostró errores debido a las limitaciones computacionales y el reducido tamaño de la muestra. Se espera que al aumentar la muestra, la precisión mejore significativamente.

## Contribución Individual

- **Ronald Gabriel Palencia**: Desarrollo de pruebas funcionales.
- **Junior Antonio Muños Henao**: Introducción, Análisis de Requisitos del Sistema y Diagrama de Arquitectura.

## Autores

- **Ronald Gabriel Palencia**
- **Junior Antonio Muños Henao**
