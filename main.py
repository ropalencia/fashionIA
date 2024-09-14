from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import pickle
import pandas as pd
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D
from sklearn.neighbors import NearestNeighbors
import io

# Crear la aplicación FastAPI
app = FastAPI()

# Cargar los modelos preentrenados (VGG16, PCA, KNN)
base_model = VGG16(include_top=False, input_shape=(256, 256, 3))

model = Sequential()
for layer in base_model.layers:
    model.add(layer)
model.add(GlobalAveragePooling2D())


# Definir rutas de archivos
train_features_path = './Modelos/train_features.pkl'
val_features_path = './Modelos/val_features.pkl'
pca_model_path = './Modelos/pca_model.pkl'
knn_model_path = './Modelos/knn_model.pkl'
val_path = './Modelos/val_data.pkl'


# Cargar el PCA y KNN desde los archivos pickle
with open(pca_model_path, 'rb') as f:
    pca = pickle.load(f)

with open(knn_model_path, 'rb') as f:
    neigh = pickle.load(f)

# Cargar el dataframe 'val' desde el archivo .pkl usando pd.read_pickle()
val_loaded = pd.read_pickle(val_path)

# Muestreo de las 200 filas d e validación
val_sampled = val_loaded.sample(n=600, random_state=42).reset_index(drop=True)


# Función para leer y procesar una imagen
def read_img(image_file):
    image = Image.open(image_file)
    image = image.convert("RGB")  # Convertir a RGB en caso de PNG o JPG
    image = image.resize((256, 256))  # Redimensionar la imagen
    image = np.array(image) / 255.0  # Convertir a array y normalizar
    return np.expand_dims(image, axis=0)




# Función para leer y procesar una imagen
def read_img(image_file):
    image = Image.open(image_file)
    image = image.convert("RGB")
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# Endpoint para cargar la imagen, extraer características, aplicar PCA y KNN
@app.post("/recommend/")
async def recommend_similar_products(file: UploadFile = File(...), num_recommendations: int = 5):
    # Leer y procesar la imagen
    image = await file.read()
    img = read_img(io.BytesIO(image))

    # Extraer características usando el modelo preentrenado VGG16
    img_features = model.predict(img)

    # Aplicar PCA a las características
    img_features_pca = pca.transform(img_features)

    # Encontrar las imágenes más similares en el dataset utilizando KNN
    dist, index = neigh.kneighbors(img_features_pca[0][:313].reshape(1, -1), n_neighbors=num_recommendations)

    # Obtener las rutas de las imágenes similares
    similar_images = []
    for i in range(num_recommendations):
        similar_image_path = val_sampled.loc[index[0][i], 'filename']
        similar_images.append({
            "image_path": similar_image_path,
            "distance": dist[0][i]
        })

    # Devolver las rutas de las imágenes similares como respuesta JSON
    return {"similar_images": similar_images}