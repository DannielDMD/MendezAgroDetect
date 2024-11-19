from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2

# Inicializar la aplicación Flask y configurar la carpeta de archivos estáticos
app = Flask(__name__, static_folder='uploads')  # Esta es la línea que debes agregar

# Asegurarse de que la carpeta 'uploads' exista
upload_folder = 'uploads'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)  # Crear la carpeta si no existe


# Cargar el modelo de TensorFlow
model = load_model('model.h5')  # Asegúrate de que 'model.h5' esté en el mismo directorio o la ruta correcta

# Función para obtener las recomendaciones
def get_recommendation(disease_class):
    recommendations = {
        'Healthy': "Tu planta está sana. Sigue cuidándola con riego adecuado y exposición al sol.",
        'Powdery': "Tu planta tiene hongos en polvo. Te recomendamos aplicar un fungicida y mejorar la circulación de aire.",
        'Rust': "La planta tiene roya. Usa un fungicida específico para roya y retira las hojas afectadas."
    }
    return recommendations.get(disease_class, "No se pudo determinar la enfermedad.")

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la imagen subida
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Asegúrate de que se haya subido una imagen
        file = request.files['image']
        if file:
            # Guarda la imagen subida
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)

            # Procesar la imagen
            img = image.load_img(filepath, target_size=(128, 128))  # Redimensionamos la imagen para que coincida con la entrada del modelo
            img_array = image.img_to_array(img) / 255.0  # Convertimos la imagen a array y normalizamos
            img_array = np.expand_dims(img_array, axis=0)  # Añadimos la dimensión del batch

            # Hacer la predicción
            prediction = model.predict(img_array)

            # Obtener la clase predicha
            class_labels = ['Healthy', 'Powdery', 'Rust']  # Cambia las clases según tu modelo
            predicted_class_index = np.argmax(prediction)
            predicted_class = class_labels[predicted_class_index]

            # Obtener las recomendaciones basadas en la predicción
            recommendation = get_recommendation(predicted_class)

            # Guardar o mostrar el resultado (esto es opcional, pero puede ser útil para mostrar la imagen procesada)
            result_filepath = os.path.join(upload_folder, 'result_' + file.filename)
            img.save(result_filepath)  # Guardamos la imagen subida como resultado

            # Mostrar el resultado en el template
            return render_template('result.html', predicted_class=predicted_class, recommendation=recommendation, result_image=result_filepath)

# Ruta para servir las imágenes procesadas desde la carpeta uploads
@app.route('/uploads/<filename>')
def send_result_image(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)