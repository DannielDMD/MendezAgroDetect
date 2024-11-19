# MendezAgroDetect 🌱

**MendezAgroDetect** es un proyecto desarrollado en el marco del **Bootcamp IA Fullstack**, ofrecido por la **Cámara de Comercio de Bogotá**. Este proyecto se centra en la detección de enfermedades en cultivos con el objetivo de ayudar a los campesinos en la identificación temprana de problemas en sus plantas. Aunque actualmente se encuentra en una fase **beta**, tiene un gran potencial para futuras mejoras y aplicaciones más avanzadas.

## 📋 Descripción

El propósito de este proyecto es ofrecer una herramienta que, mediante técnicas de procesamiento de imágenes e Inteligencia Artificial, pueda identificar de forma precisa ciertas enfermedades en los cultivos. De esta manera, se busca empoderar a los agricultores proporcionándoles información útil para tomar decisiones y mejorar la salud de sus cultivos.

Actualmente, MendezAgroDetect puede clasificar enfermedades en categorías como:
- **Healthy** (Planta sana)
- **Powdery** (Mildiu polvoriento)
- **Rust** (Óxido)

### 🚀 Futuras Mejoras

El proyecto se encuentra en fase inicial, pero las mejoras futuras incluyen:
- Ampliar la base de datos para reconocer más enfermedades.
- Optimizar el modelo para mejorar la precisión de predicciones.
- Implementar un sistema de alertas y sugerencias automáticas.
- Añadir soporte para otros tipos de cultivos.

## 📚 Tecnologías Utilizadas

El proyecto se ha desarrollado utilizando las siguientes tecnologías:

- **Python**: Lenguaje principal para el procesamiento de datos y la implementación del modelo de IA.
- **TensorFlow/Keras**: Biblioteca utilizada para construir y entrenar el modelo de redes neuronales.
- **OpenCV**: Utilizado para el procesamiento de imágenes.
- **Matplotlib / Seaborn**: Librerías de visualización utilizadas para graficar las métricas de entrenamiento, como las curvas de pérdida, y crear mapas de calor de la matriz de confusión para evaluar el modelo.
- **Scikit-learn**: Usada para calcular la matriz de confusión y otras métricas de evaluación del modelo.
- **Flask**: Framework para la creación del backend y la gestión de la API.
- **HTML/CSS**: Para el desarrollo del frontend básico.
- **JavaScript**: Para mejorar la interactividad en el frontend.
- **Bootstrap/Tailwind CSS**: Estilización del frontend.
- **Git**: Control de versiones.
- **GitHub**: Almacenamiento del código fuente y gestión del repositorio.


## 🖥️ Instalación

Para ejecutar el proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
   
   ```bash
   git clone https://github.com/DannielDMD/MendezAgroDetect.git

2.  **Accede al directorio del proyecto**:
   
     ```bash
     cd MendezAgroDetect
     
3. **Crea un entorno virtual (opcional pero recomendado)**:
    ```bash
    python -m venv venv
    
4. **Activa el entorno virtual**:
   - En Windows:
     
   ```bash
    venv\Scripts\activate
 
  - En macOS/Linux:

     ```bash
     source venv/bin/activate

5. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    
6. **Ejecuta la aplicación**:
   ```bash
    python app.py
   
7. **Accede a la aplicación en tu navegador en http://localhost:5000.**
      
## 📸 Uso

1. **Sube una imagen de una planta afectada o sana.**
2. **La aplicación procesará la imagen y clasificará la enfermedad.**
3. **Recibirás una predicción junto con recomendaciones para el tratamiento de la enfermedad detectada.**

## 📂 Estructura del Proyecto
MendezAgroDetect/
│
├── app.py                # Archivo principal de la aplicación Flask
├── requirements.txt      # Dependencias del proyecto
├── README.md              # Este archivo
│
├── uploads/              # Carpeta para almacenar imágenes subidas
│
├── templates/            # Archivos HTML (frontend)
│   ├── index.html        # Página principal de la aplicación
│   └── result.html       # Página de resultados
│
├── static/               # Archivos estáticos como CSS, JS, imágenes
│
├── data/                 # Datos para entrenamiento y validación
│   ├── Train/            # Imágenes de entrenamiento
│   ├── Test/             # Imágenes de prueba
│   └── Validation/       # Imágenes de validación
│
└── scripts/              # Scripts de entrenamiento del modelo
    └── train_model.py    # Código para entrenar el modelo de IA

## 👨‍💻 Desarrollado por

**Daniel Esteban Méndez Díaz**

Estudiante del Bootcamp IA Fullstack ofrecido por la Cámara de Comercio de Bogotá.


   
