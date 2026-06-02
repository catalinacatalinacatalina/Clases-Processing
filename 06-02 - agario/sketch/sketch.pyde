from Player import Player
from Food import Food
n_comidas = 50
foods = []

def setup():
    global p, foods
    size(1000,700)
    p = Player(width/2, height/2)

    for _ in range(n_comidas):
        col = color(random(255), random(255), random(255))
        foods.append(Food(col))
    
def draw():
    global foods
    background(200)
    p.move()
    p.eat(foods)

    for f in foods:
        f.display()
    p.dibujar()

    
