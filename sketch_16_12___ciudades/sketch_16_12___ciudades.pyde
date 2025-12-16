
from Edificio import Edificio
edificios = []   # Lista que almacenará todos los edificios
n = 40
def setup():
    size(1900,1000)
    background(10, 10, 30)
    altura = width/6
    
    for i in range(n):
        e = Edificio(random(0, width),altura, 25)
        edificios.append(e)
        altura += 20
    
def draw():
    background(10,10,30)
    
    for e in edificios:
        e.show()
