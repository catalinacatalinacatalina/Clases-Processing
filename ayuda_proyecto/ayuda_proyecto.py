import py5 as p
from Boton import Boton
from BaseDatos import BaseDatos
from Persona import Persona

boton1 = Boton(20, 350, 120, 50, "Agregar")
boton_reset = Boton(160, 350, 120, 50, "Reset BD")
bd = BaseDatos("personas.db")

def settings():
    p.size(700, 500)

def setup():
    p.background(220)

def draw():
    p.background(220)
    boton1.mostrar()
    boton_reset.mostrar()
    mostrar_personas()

def mostrar_personas():
    """Muestra las personas de la base de datos en pantalla"""
    personas = bd.obtener_todas_personas()
    
    # Título
    p.fill(0)
    p.text_size(16)
    p.text_align(p.LEFT)
    p.text("Lista de Personas", 20, 30)
    
    # Línea separadora
    p.stroke(0)
    p.stroke_weight(2)
    p.line(20, 40, 680, 40)
    p.stroke_weight(1)
    
    # Encabezados
    p.text_size(12)
    p.fill(50)
    p.text("ID", 30, 70)
    p.text("Nombre", 80, 70)
    p.text("Edad", 250, 70)
    p.text("Ciudad", 350, 70)
    
    # Mostrar personas usando encapsulación
    y = 100
    p.text_size(11)
    p.fill(80)
    for persona in personas:
        p.text(str(persona.obtener_id()), 30, y)
        p.text(persona.obtener_nombre(), 80, y)
        p.text(str(persona.obtener_edad()), 250, y)
        p.text(persona.obtener_ciudad(), 350, y)
        y += 30
    
    # Info adicional
    p.text_size(10)
    p.fill(100)
    p.text(f"Total de personas: {len(personas)}", 20, y + 30)

def mouse_pressed():
    if boton1.presionado():
        # Agregar nueva persona
        nueva_persona = Persona(0, "Nueva Persona", 25, "Madrid")
        bd.agregar_persona(nueva_persona)
        print(f"Persona agregada: {nueva_persona}")
    
    if boton_reset.presionado():
        # Resetear base de datos
        bd.resetear_bd()
        print("Base de datos limpiada")

p.run_sketch()