
from Food import Food

class Enemy:

    def __init__(self):

        self.x = random(1000)
        self.y = random(700)
        self.r = random(20, 60)

        self.vx = random(-2, 2)
        self.vy = random(-2, 2)

    def move(self):

        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > width:
            self.vx *= -1

        if self.y < 0 or self.y > height:
            self.vy *= -1

    def eat(self, foods):

        for f in foods[:]:
            d = dist(self.x, self.y, f.x, f.y)
            if d < self.r:
                self.r += 0.05
                foods.append(Food(f.col))
                foods.remove(f)



    def display(self):

        fill(255, 100, 100)
        stroke(255)

        ellipse(
            self.x,
            self.y,
            self.r * 2,
            self.r * 2
        )
