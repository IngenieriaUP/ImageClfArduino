# Clasificador de imágenes 📸 + Arduino 📟

Este repositorio tiene como objetivo construir un programa que permita utilizar las predicciones un modelo clasificación de imágenes como disparador de accciones.
Entre las acciones tenemos: mandar correos, registrar información/imágenes en una base de datos o repositorio de archivos, lanzar alguna alerta sonora o visual mediante un Arduino, entre otros.

Para facilitar el entrenamiento del modelo se recomienda el uso de [teachable machines de google](https://teachablemachine.withgoogle.com/) 🚀

# Uso 👨‍💻

Se debe ejecutar el archivo `teachable_arduino.py` desde un dispositvo que tenga una camara web activada y un arduino conectado mediante USB.
El arduino debe tener precargado el codigo `signalReceiver/signalReceiver.ino``
