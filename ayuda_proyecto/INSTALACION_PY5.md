# Instalación de Python + py5

## Requisitos Previos
- **Java JDK** (versión 21 recomendada)
- **Python** (versión 3.9 o superior)

## Pasos de Instalación

### 1. Instalar py5
Abre PowerShell o terminal y ejecuta:
```bash
pip install py5
```

### 2. Configurar JAVA_HOME
py5 necesita Java para funcionar. Configura la variable de entorno:

En PowerShell:
```powershell
$env:JAVA_HOME = "C:\Program Files\Java\jdk-21"
```

Para hacerlo permanente, agrega esta línea a tu perfil de PowerShell o establécelo en variables de entorno del sistema.

### 3. Ejecutar un Script py5
Con JAVA_HOME configurado, ejecuta:
```bash
python tu_script.py
```

## Ejemplo Básico
```python
import py5 as p

def settings():
    p.size(400, 400)

def setup():
    p.background(220)

def draw():
    p.background(220)
    p.fill(100, 150, 255)
    p.circle(p.mouse_x, p.mouse_y, 50)

p.run_sketch()
```

## Tips
- Usa el alias `as p` para escribir menos código
- `settings()` es para tamaño de ventana
- `setup()` se ejecuta una sola vez
- `draw()` se ejecuta continuamente
- Accede a variables de entrada como `p.mouse_x`, `p.mouse_y`

## Solución de Problemas
Si obtienes error `JVMNotFoundException`, asegúrate de:
1. Tener Java JDK instalado
2. Configurar correctamente JAVA_HOME
3. Reiniciar la terminal después de cambiar variables de entorno
