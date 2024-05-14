from flask import Flask, render_template , url_for, redirect,request
from config import *
from models.persona import Persona 


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



if __name__=='__main__':
    app.run(debug=True, port=5000)

