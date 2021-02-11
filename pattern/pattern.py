import random

size(500, 500)

def stepping():
    squareSize = 15
    width = 250
    for x in range(0, width, squareSize):
        fill(random.random(), random.random(), random.random(), (250-x)/250)
        # this is such a weird way to do this but oh well
        rect(x, x, width*2-x*2, width*2-x*2)

stepping()