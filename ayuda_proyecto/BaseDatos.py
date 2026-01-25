import sqlite3
from Persona import Persona

class BaseDatos:
    def __init__(self, nombre_bd="personas.db"):
        self.nombre_bd = nombre_bd
        self.crear_bd()
    
    def crear_bd(self):
        """Crea la base de datos y la tabla de personas si no existen"""
        conexion = sqlite3.connect(self.nombre_bd, check_same_thread=False)
        cursor = conexion.cursor()
        
        # Crear tabla de personas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                ciudad TEXT NOT NULL
            )
        ''')
        
        # Insertar datos de ejemplo si la tabla está vacía
        cursor.execute('SELECT COUNT(*) FROM personas')
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES ('Ana García', 28, 'Madrid')")
            cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES ('Carlos López', 35, 'Barcelona')")
            cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES ('María Ruiz', 42, 'Valencia')")
            cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES ('Juan Martínez', 25, 'Sevilla')")
        
        conexion.commit()
        conexion.close()
    
    def obtener_todas_personas(self):
        """Obtiene todas las personas como objetos Persona"""
        conexion = sqlite3.connect(self.nombre_bd, check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute('SELECT id, nombre, edad, ciudad FROM personas')
        datos = cursor.fetchall()
        conexion.close()
        
        # Convertir a objetos Persona
        personas = [Persona(id, nombre, edad, ciudad) for id, nombre, edad, ciudad in datos]
        return personas
    
    def agregar_persona(self, persona):
        """Agrega una nueva persona a la base de datos"""
        conexion = sqlite3.connect(self.nombre_bd, check_same_thread=False)
        cursor = conexion.cursor()
        id, nombre, edad, ciudad = persona.obtener_datos()
        cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES (?, ?, ?)", 
                      (nombre, edad, ciudad))
        conexion.commit()
        conexion.close()
    
    def eliminar_persona(self, id):
        """Elimina una persona por ID"""
        conexion = sqlite3.connect(self.nombre_bd, check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM personas WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
    
    def obtener_persona_por_id(self, id):
        """Obtiene una persona específica por ID"""
        conexion = sqlite3.connect(self.nombre_bd, check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute('SELECT id, nombre, edad, ciudad FROM personas WHERE id = ?', (id,))
        dato = cursor.fetchone()
        conexion.close()
        
        if dato:
            return Persona(dato[0], dato[1], dato[2], dato[3])
        return None
    
    def resetear_bd(self):
        """Elimina todos los datos y reinicia la base de datos"""
        conexion = sqlite3.connect(self.nombre_bd, check_same_thread=False)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM personas")
        conexion.commit()
        conexion.close()
        print("✓ Base de datos reseteada")


