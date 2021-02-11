import random

canvasHeight = 500
canvasWidth  = 500
size(canvasWidth,canvasHeight)

# def tiles(tileSize):
#     currentY = 0;
#     clicks = 0;
#     while(currentY < canvasHeight):
#         polygon(
#             (250, currentY),
#             (250 + tileSize * 1.2, currentY + tileSize / 2),
#             (250, currentY + tileSize),
#             (250 - tileSize * 1.2, currentY + tileSize / 2),
#         )
#         currentY += tileSize
#         tileSize = tileSize * 0.9 if (tileSize * 0.9 > 0.2) else 0.2
#         clicks += 1
#         if(clicks > 400): # prevent infinite while
#             return

# steps = 18
# tiles(55)

threadSize = 1.5
smallestThreadHeight = 10

def drawHorizontalLine(startX, startY, height):
    if(startX > canvasWidth or startY > canvasHeight):
        return
    strokeWidth(threadSize)
    line((startX, startY), (startX + height, startY + height))
    drawHorizontalLine(startX + threadSize * 2, startY, height)
    
def drawVerticalLine(startX, startY, height):
    if(startX > canvasWidth or startY > canvasHeight):
        return
    strokeWidth(threadSize)
    line((startX, startY), (startX + height, startY + height))
    drawVerticalLine(startX, startY + threadSize * 2, height)

fill(.1,.3,.15)
rect(0,0,canvasWidth,canvasHeight)

def tartan():
    stroke(0)
    drawHorizontalLine(-smallestThreadHeight - smallestThreadHeight*2, canvasHeight/2 - smallestThreadHeight*2, smallestThreadHeight*2)
    drawVerticalLine(canvasWidth/2 - smallestThreadHeight*2, -smallestThreadHeight * 2, smallestThreadHeight*2)
    drawHorizontalLine(-smallestThreadHeight - smallestThreadHeight*2, canvasHeight/2 + smallestThreadHeight*5, smallestThreadHeight*2)
    drawVerticalLine(canvasWidth/2 + smallestThreadHeight*5, -smallestThreadHeight * 2, smallestThreadHeight*2)

    stroke(.2,.5,.8)
    drawHorizontalLine(-smallestThreadHeight - smallestThreadHeight*4, canvasHeight/2, smallestThreadHeight*5)
    drawVerticalLine(canvasWidth/2, -smallestThreadHeight * 5, smallestThreadHeight*5)

    stroke(0)
    drawHorizontalLine(-smallestThreadHeight, 0, smallestThreadHeight)
    drawHorizontalLine(-smallestThreadHeight, 2 * smallestThreadHeight, smallestThreadHeight)

    stroke(1)
    drawHorizontalLine(-smallestThreadHeight, smallestThreadHeight, smallestThreadHeight)
    drawVerticalLine(smallestThreadHeight, -smallestThreadHeight - threadSize, smallestThreadHeight)

    stroke(0)
    drawVerticalLine(smallestThreadHeight * 2, -smallestThreadHeight - threadSize, smallestThreadHeight)
    drawVerticalLine(0, -smallestThreadHeight - threadSize, smallestThreadHeight)

    stroke(1,0.12,0)
    drawHorizontalLine(-smallestThreadHeight - threadSize, canvasHeight/4, smallestThreadHeight)
    drawVerticalLine(canvasWidth/4, -smallestThreadHeight, smallestThreadHeight)
    drawHorizontalLine(-smallestThreadHeight - threadSize, canvasHeight*.75 + smallestThreadHeight*3, smallestThreadHeight)
    drawVerticalLine(canvasWidth*.75 + smallestThreadHeight*3, -smallestThreadHeight, smallestThreadHeight)

tartan()




