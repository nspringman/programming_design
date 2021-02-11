import random
import math
import drawBot as db

canvasHeight = 500
canvasWidth  = 500

pages = 40

def rgb(r, g, b):
    return (r / 255, g/255, b/255)

# modeled after https://me120.mme.pdx.edu/lib/exe/fetch.php?media=notes:breathing_led_equations.pdf
# that will take to long to actually implement, so not yet.
# just a trianngle (ish) wave today
def breathingColor(currentPage, r, g, b):
    t_0 = 0
    t_1 = pages * 0.3
    t_2 = pages * 0.5
    t_3 = pages

    d = 40 # delta color

    if currentPage < t_1: # v_in
        color = (
            r + (d / (t_1 - t_0)) * currentPage,
            g + (d / (t_1 - t_0)) * currentPage,
            b + (d / (t_1 - t_0)) * currentPage
        )
    elif currentPage < t_2: # pause
        color = (
            r + d,
            g + d,
            b + d
        )
    else: # v_ex
        color = (
            r + d - (d / (t_3 - t_2)) * (currentPage - t_2), # this last bit is bad math (I think)
            g + d - (d / (t_3 - t_2)) * (currentPage - t_2), # but it works ?
            b + d - (d / (t_3 - t_2)) * (currentPage - t_2)
        )
    return color

def fold(startX, startY, height, currentPage):
    colorOffset = int(startX/canvasWidth * 300)
    
    horizontalColorOffset = startX / canvasWidth
    verticalColorOffset = startY / canvasHeight

    color = (
        186 - horizontalColorOffset * 50,
        17 + horizontalColorOffset * 30,
        82 + horizontalColorOffset * 40
    )

    color = breathingColor(currentPage, *color)
    
    gradientSteps = 80
    for x in range(0, gradientSteps):
        colorOffset -= colorOffset + x/gradientSteps * 50
        db.fill(*rgb(color[0]+ colorOffset, color[1] + colorOffset, color[2] + colorOffset))
        db.polygon(
            (startX + ((height * 0.3) * x/gradientSteps), startY + height * 0.3 * x/gradientSteps),
            (startX + height * 2 - ((height * 0.2) * x/gradientSteps), 
                startY + ((height * 0.3)* x/gradientSteps) ),
            (startX + height * 1.5, startY + height * 0.8),
            (startX - height / 2 + (height * 0.3 * x/gradientSteps), 
                startY + height - 0.1 * (height * 0.3) * x/gradientSteps),
        )

def drawFolds(foldWidth, currentPage):    
    ticks = 0
    for y in range(0, int(canvasHeight * 1.3), int(foldWidth * 0.6)):
        with db.savedState():
            yCopy = y
            db.rotate(-30, center=(0,yCopy))
            xOffset = -foldWidth
            for x in range(xOffset, int(canvasWidth * 1.3), int(foldWidth * 1.8)):
                yCopy -= foldWidth * 0.03
                db.rotate(math.sqrt((x - xOffset + 1) * 0.1), center=(x,yCopy))
                fold(x, yCopy, foldWidth, currentPage)
                ticks += 1
                if(ticks > 2000):
                    raise Exception('Maximum depth reached')
    print(ticks)

if __name__ == '__main__':
    db.newDrawing()

    for p in range(pages):
        db.newPage(canvasWidth, canvasHeight)
        drawFolds(40, p)
    
    db.saveImage('output/door.gif')

    db.endDrawing()
