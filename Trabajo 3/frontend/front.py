import streamlit as st
import requests
from PIL import Image
import io
import os

# Configurar la API endpoint que usas con FastAPI
API_ENDPOINT = "http://127.0.0.1:8000/recommend/"

# Función para cargar la imagen desde una ruta
def load_image(image_path):
    return Image.open(image_path)

# Título de la app
st.title("Sistema de Recomendación de Productos")

# Paso 1: Subir la imagen
st.write("## Subir una imagen para generar recomendaciones")
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png"])

# Variable para almacenar la imagen subida
image = None

# Verificar si se ha subido una imagen
if uploaded_file is not None:
    # Mostrar la imagen subida
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen Original", use_column_width=True)

    # Paso 2: Elegir el número de recomendaciones
    num_recommendations = st.slider('Número de productos recomendados', 1, 10, 5)

    # Botón para generar recomendaciones
    if st.button("Generar Recomendaciones"):
        # Convertir la imagen en un archivo binario para enviarla a la API
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        img_bytes = img_bytes.getvalue()

        try:
            # Llamar a la API para obtener recomendaciones
            response = requests.post(
                API_ENDPOINT,
                files={'file': ('image.jpg', img_bytes, 'image/jpeg')},  # Enviar correctamente el archivo
                data={'num_recommendations': num_recommendations}
            )

            # Depuración: Mostrar el código de estado y el contenido de la respuesta
            st.write(f"Status Code: {response.status_code}")
            st.write(f"Response content: {response.text}")

            if response.status_code == 200:
                # Procesar las recomendaciones
                recommendations = response.json()['similar_images']
                
                st.write(f"### {num_recommendations} Productos Recomendados:")
                
                # Mostrar las imágenes recomendadas
                for i, rec in enumerate(recommendations):
                    rec_image_path = rec['image_path']
                    rec_distance = rec['distance']
                    
                    # Ajustar la ruta según el sistema de archivos
                    rec_image_path = rec_image_path.replace("\\", "/")  # Para rutas en Windows
                    
                    # Mostrar la imagen recomendada con su distancia
                    st.write(f"Producto {i+1} - Distancia: {rec_distance}")
                    rec_image = load_image(rec_image_path)
                    st.image(rec_image, caption=f"Producto {i+1}", use_column_width=True)
            else:
                st.error("Hubo un problema al obtener las recomendaciones.")
        except Exception as e:
            st.error(f"Error al conectar con la API: {e}")
