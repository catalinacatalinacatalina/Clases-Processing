class Persona:
    def __init__(self, id, nombre, edad, ciudad):
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._ciudad = ciudad
    
    # Getters (métodos para obtener valores privados)
    def obtener_id(self):
        return self._id
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_edad(self):
        return self._edad
    
    def obtener_ciudad(self):
        return self._ciudad
    
    # Setters (métodos para modificar valores privados)
    def establecer_nombre(self, nombre):
        if len(nombre) > 0:
            self._nombre = nombre
        else:
            print("El nombre no puede estar vacío")
    
    def establecer_edad(self, edad):
        if 0 <= edad <= 120:
            self._edad = edad
        else:
            print("La edad debe estar entre 0 y 120")
    
    def establecer_ciudad(self, ciudad):
        if len(ciudad) > 0:
            self._ciudad = ciudad
        else:
            print("La ciudad no puede estar vacía")
    
    def __str__(self):
        return f"Persona(ID: {self._id}, Nombre: {self._nombre}, Edad: {self._edad}, Ciudad: {self._ciudad})"
    
    def obtener_datos(self):
        """Devuelve una tupla con los datos"""
        return (self._id, self._nombre, self._edad, self._ciudad)
