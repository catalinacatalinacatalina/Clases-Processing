from Player import Player
from Food import Food
from Enemy import Enemy
n_comidas = 50
foods = []
n_enemigos = 3
enemigos = []
def setup():
    global p, foods
    size(1000,700)
    p = Player(width/2, height/2)

    for _ in range(n_comidas):
        col = color(random(255), random(255), random(255))
        foods.append(Food(col))
    
    for _ in range(n_enemigos):
        enemigos.append(Enemy())
    
def draw():
    global foods
    background(200)
    p.move()
    p.eat(foods)
    for e in enemigos:
        e.move()
        e.eat(foods)
        
    for f in foods:
        f.display()
    for e in enemigos:
        e.display()
    p.dibujar()
    


    
