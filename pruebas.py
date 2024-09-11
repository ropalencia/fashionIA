import pickle
train_features_path = 'Trabajo 3/Modelos/train_features.pkl'
val_features_path = 'Trabajo 3/Modelos/val_features.pkl'
pca_model_path = 'Trabajo 3/Modelos/pca_model.pkl'
knn_model_path = 'Trabajo 3/Modelos/knn_model.pkl'
val_path = 'Trabajo 3/Modelos/val_data.pkl'


# Cargar el PCA y KNN desde los archivos pickle
with open(pca_model_path, 'rb') as f:
    pca = pickle.load(f)
