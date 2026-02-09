class Color:

    def __init__(self, r=None, g=None, b=None):

        if r is None:
            # Constructor aleatorio
            self.cromosoma = [random(255), random(255), random(255)]
        else:
            self.cromosoma = [r, g, b]

    def distancia(self, altre):
        return 0

    def getColor(self):
        return color(self.cromosoma[0],
                     self.cromosoma[1],
                     self.cromosoma[2])

    def display(self, x, y, w, h):
        pushStyle()
        fill(self.getColor())
        rectMode(CENTER)
        rect(x, y, w, h)

        fill(0)
        textAlign(CENTER)
        textSize(12)
        text(str(round(self.cromosoma[0], 1)), x, y - h/4)
        text(str(round(self.cromosoma[1], 1)), x, y)
        text(str(round(self.cromosoma[2], 1)), x, y + h/4)
        popStyle()

    def cruza(self, otro):
        # to-do
        return Color(0, 0, 0)

    def muta(self):
        # to-do
        return Color(0, 0, 0)
