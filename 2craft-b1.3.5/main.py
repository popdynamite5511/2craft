
#2craft by popdynamite5511. 2d Minecraft, but it's crappy. Make mods if you want.
#In my older releases, I used to note everything. But I've rewritten the code now and I can't be bothered to write new useless notes.
import turtle

win = turtle.Screen()
win.title("2craft b1.3.5")
win.bgcolor("teal")
win.setup(width=1280, height=800)
win.tracer(0)


def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)

def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  if inventory[currentTile] < MAXTILES:
    inventory[currentTile] += 1
    world[playerX][playerY] = DIRT
    drawResource(playerX, playerY)
    drawInventory()

def place(resource):
  print('placing: ', names[resource])
  if inventory[resource] > 0:
    currentTile = world[playerX][playerY]
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    world[playerX][playerY] = resource
    inventory[resource] -= 1
    drawResource(playerX, playerY)
    drawInventory()
    print('   Placing', names[resource], 'complete')
  else:
    print('   You have no', names[resource], 'left')

def craft(resource):
  print('Crafting: ', names[resource])
  if resource in crafting:
    canBeMade = True
    for i in crafting[resource]:
      if crafting[resource][i] > inventory[i]:
        canBeMade = False
        break
    if canBeMade == True:
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      inventory[resource] += 1
      print('   Crafting', names[resource], 'complete')
    else:
      print('   Can\'t craft', names[resource])
    drawInventory()

def makeplace(resource):
  return lambda: place(resource)

def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

def makecraft(resource):
  return lambda: craft(resource)

def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

def drawResource(y, x):
  global drawing
  if drawing == False:
    drawing = True
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    drawing = False

def drawWorld():
  for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
      drawResource(column, row)

def drawInventory():
  global drawing
  if drawing == False:
    drawing = True
    rendererT.color(BACKGROUNDCOLOUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    for i in range(2):
      rendererT.forward(inventory_height - 60)
      rendererT.right(90)
      rendererT.forward(width)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('black')
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("Key to place")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("Key to craft")
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 60
    itemNum = 0
    for i, item in enumerate(resources):
      rendererT.goto(xPosition + 10, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(names[item])
      rendererT.goto(xPosition, yPostition - TILESIZE - 40)
      rendererT.write(placekeys[item])
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 60)
        rendererT.write(craftkeys[item])
      xPosition += 70
      itemNum += 1
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

def generateInstructions():
  instructions.append('Crafting rules:')
  for rule in crafting:
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    instructions.append(craftrule)
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

def generateRandomWorld():
  for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
      randomNumber = random.randint(0,20)
      if randomNumber in [1,2]:
        tile = WATER
      elif randomNumber in [3,4]:
        tile = DIRT
      elif randomNumber in [5]:
        tile = GRASS
      elif randomNumber in [6]:
        tile = GRASS
      elif randomNumber in [7]:
        tile = GRAVEL
      elif randomNumber in [8]:
        tile = CLAY
      elif randomNumber in [9]:
        tile = WOOD
      elif randomNumber in [8]:
        tile = GRASS
      elif randomNumber in [9]:
        tile = GRASS
      elif randomNumber in [10]:
        tile = GRASS
      elif randomNumber in [11]:
        tile = SAND
      elif randomNumber in [12]:
        tile = STONE
      elif randomNumber in [13]:
        tile = BUSHYGRASS
      else:
        tile = GRASS
      world[column][row] = tile

#The code starts running here.

import turtle
import random
from variables import *
from math import ceil
from tkinter import *

TILESIZE = 21
INVWIDTH = 10
drawing = False

screen = turtle.Screen()
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

count = 0

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

screen.register_shape(playerImg)
for texture in textures.values():
  screen.register_shape(texture)

  
playerT = turtle.Turtle()
playerT.hideturtle()
playerT.shape(playerImg)
playerT.penup()
playerT.speed(1)

rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(1)
rendererT.setheading(90)

world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

bindPlacingKeys()
bindCraftingKeys()

generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()
playerT.showturtle()

