import random
import math

canvasHeight = 500
canvasWidth  = 500

pages = 20

# size(canvasWidth,canvasHeight)

def rgb(r, g, b):
    return (r / 255, g/255, b/255)

def fold(startX, startY, height, currentPage):
    colorOffset = int(startX/width() * 300)
    # fill(*rgb(186 + colorOffset, 17 + colorOffset, 82 + colorOffset))
    # polygon(
    #     (startX, startY),
    #     (startX + height * 2, startY),
    #     (startX + height * 2 - height / 2, startY + height * 0.8),
    #     (startX - height / 2, startY + height),
    # )
    
    horizontalColorOffset = startX / canvasWidth
    verticalColorOffset = startY / canvasHeight
    
    color = (
        186 - horizontalColorOffset * 50 + math.sin((math.pi * 2) * currentPage/pages) * 30,
        17 + horizontalColorOffset * 30 + math.sin((math.pi * 2) * currentPage/pages) * 10,
        82 + horizontalColorOffset * 40 + math.sin((math.pi * 2) * currentPage/pages) * 10
    )
    
    gradientSteps = 80
    for x in range(0, gradientSteps):
        colorOffset -= colorOffset + x/gradientSteps * 50
        fill(*rgb(color[0]+ colorOffset, color[1] + colorOffset, color[2] + colorOffset))
        # fill(random.random())
        polygon(
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
        # for x in range(0, canvasWidth, int(foldWidth * 1.8)):
        with savedState():
            yCopy = y
            # translate(-2 * foldWidth * currentPage / pages, 0)
            rotate(-30, center=(0,yCopy))
            # translate(-10 * currentPage / pages, -30 * currentPage / pages)
            xOffset = -foldWidth
            for x in range(xOffset, int(canvasWidth * 1.3), int(foldWidth * 1.8)):
                yCopy -= foldWidth * 0.03
                rotate(math.sqrt((x - xOffset + 1) * 0.1), center=(x,yCopy))
                # fold(y, int(100 - x/width() * 10), foldWidth)
                fold(x, yCopy, foldWidth, currentPage)
                ticks += 1
                if(ticks > 2000):
                    raise Exception('Maximum depth reached')
    print(ticks)

if __name__ == '__main__':
    for p in range(pages):
        newPage(canvasWidth, canvasHeight)
        drawFolds(40, p)
    
    saveImage('door.gif')
