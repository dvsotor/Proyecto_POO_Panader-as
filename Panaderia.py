from db import db

class Panaderia(db.Model):
    
    __tablename__ = "Panaderia"
    
    id = db.Column(db.Integer, primary_key=True)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    nombre = db.Column(db.String(20))
    descripcion = db.Column(db.String(100))
    especialidad = db.Column(db.String(15))
    pasteleria = db.Column(db.String(2))
    calificacion = db.Column(db.Integer)
    
    def __init__(self, latitud, longitud, nombre, descripcion, especialidad, pasteleria, calificacion):
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
        self.descripcion = descripcion
        self.especialidad = especialidad
        self.pasteleria = pasteleria
        self.calificacion = calificacion