from flask import Flask, render_template , url_for, redirect,request, send_from_directory
from config import *
from models.persona import Persona 
import os 
from werkzeug.utils import secure_filename


con_bd =conexion() 

app=Flask(__name__) 

@app.route('/') 
def index():  
    coleccionPersonas =con_bd['registro']
    PersonasRegistradas = coleccionPersonas.find()
    return render_template('/auth/inicio.html', datos = PersonasRegistradas)


@app.route('/guardar_registro',methods=['POST']) 
def agregarPersona():
    personas =con_bd['registro']
    
    nombre = request.form['nombre']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    confiContraseña = request.form['confiContraseña']
    telefono = request.form['telefono']

    if nombre and correo and contraseña and confiContraseña and telefono: 
        persona1 = Persona(nombre,correo,contraseña,confiContraseña,telefono)
        personas.insert_one(persona1.formato_doc())
        return redirect(url_for('login'))
    
    else:
        return "Error "


@app.route('/registro') 
def registro():  
    return render_template('/auth/registro.html')

@app.route('/login') 
def login():  
    return render_template('/auth/login.html')


ALLOWED_EXTENSIONS = set(["doc","txt","docx","pdf"])

app.config["UPLOAD_FOLDER"]= "src/static/uploads"

def allowed_file(file):
    file = file.split('.')
    print(file)
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

@app.route('/proyectos', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['documento']
        print(file, file.filename)
        filename = secure_filename(file.filename)
        print(filename)
        if file and allowed_file(filename):
            print("permitido")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'GUARDADO EXITOSAMENTE'
    else:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('/auth/proyectos.html', files=files) 

@app.route('/proyectos')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/perfil', methods=['GET']) 
def perfil ():
    return render_template('/auth/perfil.html') 

@app.route('/info', methods=['GET']) 
def info ():
    return render_template('/auth/info.html')


if __name__=='__main__':
    app.run(debug=True, port=5000)

