from Food import Food
class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 20
        self.speed = 90

    def move(self):
        mx = mouseX - self.x
        my = mouseY - self.y
        
        d = dist(self.x, self.y, mouseX, mouseY)
        
        if d > 5:
            vx = mx/d
            vy = my/d
            # cuanto mas grande -> mas lento
            vel = self.speed / self.r
            self.x += vx * vel
            self.y += vy * vel
        
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)

    def dibujar(self):
        rectMode(CENTER)
        fill(0)
        circle(self.x, self.y, self.r*2)
    
    def eat(self, foods):
        for f in foods[:]:
            if dist(self.x, self.y, f.x, f.y) < self.r:
                foods.append(Food(f.col))
                foods.remove(f)
                self.r+=0.2
        
