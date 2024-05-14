class Persona:
    def __init__(self, nombre, correo, contraseña,confiContraseña, telefono):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.confiContraseña = confiContraseña
        self.telefono = telefono

    def formato_doc(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'contraseña': self.contraseña,
            'confiContraseña': self.confiContraseña,
            'telefono': self.telefono
        }