from flask import Flask, render_template, request
import os
import cv2
import numpy as np

app = Flask(__name__)

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

            # Procesar la imagen (esto es solo un ejemplo, puedes aplicar un modelo de visión por computadora aquí)
            image = cv2.imread(filepath)
            # Aquí podrías hacer tu procesamiento de imagen
            # Ejemplo de convertir a escala de grises
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Guardar o mostrar el resultado
            result_filepath = os.path.join('uploads', 'result_' + file.filename)
            cv2.imwrite(result_filepath, gray_image)

            return render_template('result.html', result_image=result_filepath)

if __name__ == '__main__':
    app.run(debug=True)
