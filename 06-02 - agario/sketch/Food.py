class Food:
    def __init__(self, col):
        self.x = random(width)
        self.y = random(height)
        self.r = random(4, 8)
        self.col = col

    def display(self):
        fill(self.col)
        noStroke()
        circle(self.x, self.y, self.r * 2)
