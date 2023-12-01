from flask import Flask, render_template, request, redirect, url_for
from db import db
from Panaderia import Panaderia

class Programa:
    def __init__(self):
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///panaderias.sqlite3'
        
        db.init_app(self.app)
        self.app.add_url_rule('/', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])
        
        with self.app.app_context():
            db.create_all()
            self.app.run(debug=True)
        
    def buscarTodos(self):
        
        return render_template('mostrarTodos.html', panaderias=Panaderia.query.all())
    
    def agregar(self):
        
        if request.method=="POST":
            latitud=request.form['latitud']
            longitud=request.form['longitud']
            nombre=request.form['nombre']
            descripcion=request.form['descripcion']
            especialidad=request.form['especialidad']
            pasteleria=request.form['pasteleria']
            calificacion=request.form['calificacion']
            
            miPanaderia=Panaderia(latitud, longitud, nombre, descripcion, especialidad, pasteleria, calificacion)
            
            db.session.add(miPanaderia)
            db.session.commit()
            
            return redirect(url_for('buscarTodos'))
            
        
        
        return render_template('NuevaPanaderia.html')
    
    
miPrograma=Programa()