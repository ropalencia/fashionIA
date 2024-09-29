import streamlit as st
import requests
from PIL import Image
import io
import os
import base64

# Configurar la API endpoint que usas con FastAPI
API_ENDPOINT = "https://fashionia-2.onrender.com/recommend/"

# Función para cargar la imagen desde una ruta
def load_image(image_path):
    return Image.open(image_path)

# Título llamativo
st.title("Descubre tus Prendas Ideales con una Sola Imagen")
# Explicación del ejemplo


# Función para cargar una imagen y convertirla en base64 para mostrarla en HTML
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Explicación del ejemplo
st.write("### Ejemplo de cómo funciona:")

# Ruta de la imagen de prueba
example_image_path = "publicidad/ejemplo1.png"  # Aquí debes colocar la ruta a la imagen de ejemplo

# Obtener la imagen como base64
example_image_base64 = get_image_as_base64(example_image_path)

# Usar HTML para centrar la imagen y mostrarla en base64
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{example_image_base64}" style="width: 500px; height: 500px;" />
    </div>
    """,
    unsafe_allow_html=True
)

# Explicación debajo de la imagen
st.write("""
    Subiendo una imagen como esta, te recomendaremos productos similares basados en características como el estilo, color y tipo de prenda. 
    ¡Sube tu imagen ahora y prueba el sistema!
""")


############

# Sección para subir imagen del usuario
st.write("## Sube tu imagen para recibir recomendaciones")
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

    # Elegir el número de recomendaciones
    num_recommendations = st.slider('Número de productos recomendados', 1, 10, 5)

    # Botón de Generar Recomendaciones
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
                        st.write(f"Este producto se ha recomendado por su similitud en estilo, color o categoría con la imagen original.")
            else:
                st.error("Hubo un problema al obtener las recomendaciones.")
        except Exception as e:
            st.error(f"Error al conectar con la API: {e}")

        # Añadir una nota explicativa al final
        st.write("""
            **Nota:** Es posible que algunos productos recomendados no tengan sentido con la imagen cargada. 
            Esto se debe a que el modelo está entrenado con una base de datos pequeña, debido a limitaciones de recursos computacionales. 
            En futuras actualizaciones, esperamos mejorar la precisión del sistema de recomendación con una base de datos más grande y mejores recursos.
        """)
