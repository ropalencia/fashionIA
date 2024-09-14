from PIL import Image

# Define la ruta de la imagen
image_path = "./Datos/extracted_files/images\\42872.jpg"

#Datos\extracted_files\images\1164.jpg
#C:\Users\DELL\Documents\GitHub\fashionIA\Trabajo 3\Datos\extracted_files\images\1164.jpg
# Abre la imagen
img = Image.open(image_path)
import pickle
# Muestra la imagen
#img.show()




# Definir rutas de archivos
train_features_path = './Modelos/train_features.pkl'
val_features_path = './Modelos/val_features.pkl'
pca_model_path = './Modelos/pca_model.pkl'
knn_model_path = './Modelos/knn_model.pkl'
val_path = './Modelos/val_data.pkl'

# Cargar el PCA y KNN desde los archivos pickle
with open(pca_model_path, 'rb') as f:
    pca = pickle.load(f)