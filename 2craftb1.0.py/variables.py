BACKGROUNDCOLOUR = 'red'

MAXTILES = 100
MAPWIDTH = 45
MAPHEIGHT = 20

DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
GLASS   = 4
PLANK   = 5
WOOD    = 6

#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK,GLASS,PLANK,WOOD]

#the names of the resources.
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick',
  WOOD    : 'wood',
  PLANK   : 'plank'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.png',
  GRASS   : 'grass.png',
  WATER   : 'water.png',
  BRICK   : 'brick.png',
  PLANK   : 'plank.png',
  GLASS   : 'glass.png',
  WOOD    : 'wood.png'
}

#the number of each resource the player has.
inventory = {
  DIRT    : 5,
  GRASS   : 12,
  WATER   : 11,
  BRICK   : 1,
  WOOD    : 3,
  GLASS   : 1,
  PLANK   : 0
}

#the player image.
playerImg = 'player.png'

#the player position.
playerX = 0
playerY = 0

#rules to make new resources.
crafting = {
  BRICK    : { GLASS : 1, DIRT : 2 }
}

#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',
  GLASS : '5',
  WOOD  : '6',
  PLANK : '7'
  
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r'
}

#game instructions that are displayed.
instructions =  [
  'Instructions:',
  'Use the WASD keys to move, then start building! -'
  'Version: 2Craft v1.0'
  
]