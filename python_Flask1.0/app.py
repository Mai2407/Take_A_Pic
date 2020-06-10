from flask import Flask, render_template, request
from cv2 import cv2

         

app = Flask(__name__)
FLASK_DEBUG=1

@app.route('/')
def inicio():

    return render_template('index.html')

@app.route('/mostrar', methods=['POST'])
def mostrar():

    video = cv2.VideoCapture(0) 

    a = 0

    while True:
        a = a + 1

        check, frame = video.read()

        cv2.imshow("Capturing",frame)

        key = cv2.waitKey(1)

        if key == ord(' '):

            break  

    showPic = cv2.imwrite("static/fotouser.jpg",frame)

    video.release()

    cv2.destroyAllWindows()

    print(check)

    nombre = request.form.get("nombre")

    apellido = request.form.get("apellido")

    foto = request.form.get("foto")

    foto = showPic

    showPic = cv2.imwrite("static/fotouser.jpg",frame)

    return render_template("index.html",
        nombre = nombre, apellido = apellido, foto = foto)
