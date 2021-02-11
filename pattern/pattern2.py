import random
import requests

size(500, 500)

def stepping():
    squareSize = 15
    width = 250
    for x in range(0, width, squareSize):
        fill(random.random(), random.random(), random.random(), (250-x)/250)
        # this is such a weird way to do this but oh well
        rect(x, x, width*2-x*2, width*2-x*2)

stepping()

res = requests.get("https://api.kanye.rest/")
res = res.json()
# print(res)

font("Times-Italic", 50)
fill(1, 1, 1)
stroke(1, 0.5, 1, .5)
strokeWidth(.8)

margin = 10
width = width() - 2 * margin

h = textSize(res['quote'],width=400)

textBox(res['quote'], (margin, margin, width, h[1]), align="left")

font("Impact", 50)
fill(0, 0, 1)
stroke(1, 0.5, 1, .5)
strokeWidth(.8)

print(height())

textBox("Kanye says:", (margin, height() - margin - 500, width, width), align="left")