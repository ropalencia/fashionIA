import streamlit as st
import requests
from PIL import Image
import io
import os

# Configurar la API endpoint que usas con FastAPI
#API_ENDPOINT = "http://127.0.0.1:8000/recommend/"


API_ENDPOINT = "https://fashionia-2.onrender.com/recommend/"
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

    # Redimensionar la imagen principal para que sea más pequeña y con mayor nitidez
    image = image.resize((150, 150))  # Ajusta el tamaño según prefieras
    st.image(image, caption="Imagen Original", use_column_width=False)  # Mostrar imagen redimensionada

    # Paso 2: Elegir el número de recomendaciones
    num_recommendations = st.slider('Número de productos recomendados', 1, 10, 5)

    # Botón para generar recomendaciones
    if st.button("Generar Recomendaciones"):
        # Convertir la imagen en un archivo binario para enviarla a la API
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        img_bytes = img_bytes.getvalue()

        try:
            # Añadir el parámetro 'num_recommendations' como parte de la URL (query parameter)
            api_url_with_params = f"{API_ENDPOINT}?num_recommendations={num_recommendations}"
            
            # Llamar a la API para obtener recomendaciones
            response = requests.post(
                api_url_with_params,
                files={'file': ('image.jpg', img_bytes, 'image/jpeg')}  # Enviar correctamente el archivo
            )

            # Depuración: Mostrar el código de estado y el contenido de la respuesta
            st.write(f"Status Code: {response.status_code}")
            # st.write(f"Response content: {response.text}")

            if response.status_code == 200:
                # Procesar las recomendaciones
                recommendations = response.json()['similar_images']
                
                st.write(f"### {num_recommendations} Productos Recomendados:")

                # Mostrar las imágenes en un formato de mosaico
                cols = st.columns(3)  # Distribuir en 3 columnas (puedes cambiar a 2 o más según prefieras)
                
                for i, rec in enumerate(recommendations):
                    rec_image_path = rec['image_path']
                    rec_distance = rec['distance']

                    # Ajustar la ruta según el sistema de archivos
                    rec_image_path = rec_image_path.replace("\\", "/")  # Para rutas en Windows
                    
                    # Cargar la imagen recomendada
                    rec_image = load_image(rec_image_path)
                    
                    # Redimensionar la imagen para que sea más pequeña y se vea más nítida
                    rec_image = rec_image.resize((150, 150))  # Ajusta el tamaño según prefieras
                    
                    # Mostrar la imagen en la columna correspondiente con su distancia
                    with cols[i % 3]:  # Cambia el número para ajustarlo a la cantidad de columnas
                        st.image(rec_image, caption=f"Producto {i+1} - Distancia: {rec_distance}")
            else:
                st.error("Hubo un problema al obtener las recomendaciones.")
        except Exception as e:
            st.error(f"Error al conectar con la API: {e}")



