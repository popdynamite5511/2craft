BACKGROUNDCOLOUR = 'teal'

MAXTILES = 64
MAPWIDTH = 40
MAPHEIGHT = 20

DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
GLASS   = 4
PLANK   = 5
WOOD    = 6
SAND    = 7
GRAVEL  = 8
CLAY    = 9
STICK   = 10
IRONINGOT = 11
SWORD   = 12
WHITEWOOL = 13
GRASSPATH = 14
STONE   = 15
GOLDINGOT = 16
BUSHYGRASS = 17


#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK,GLASS,PLANK,WOOD,GRAVEL,CLAY,STICK,IRONINGOT,SWORD,WHITEWOOL,GRASSPATH,STONE,GOLDINGOT,BUSHYGRASS]

#the names of the resources.
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick',
  WOOD    : 'wood',
  PLANK   : 'plank',
  GLASS   : 'glass',
  SAND    : 'sand',
  GRAVEL  : 'gravel',
  CLAY    : 'clay',
  STICK   : 'stick',
  IRONINGOT : 'iron ingot',
  SWORD   : 'sword',
  WHITEWOOL : 'white wool',
  GRASSPATH : 'grass path',
  STONE   : 'stone',
  GOLDINGOT : 'gold ingot',
  BUSHYGRASS : 'bushy grass'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  PLANK   : 'plank.gif',
  GLASS   : 'glass.gif',
  WOOD    : 'wood.gif' ,
  SAND    : 'sand.gif',
  GRAVEL  : 'gravel.gif',
  CLAY    : 'clay.gif',
  STICK   : 'stick.gif',
  IRONINGOT : 'ironingot.gif',
  SWORD   : 'sword.gif',
  WHITEWOOL : 'whitewool.gif',
  GRASSPATH : 'grass_path.gif',
  STONE   : 'stone.gif',
  GOLDINGOT : 'goldingot.gif',
  BUSHYGRASS : 'bushygrass.gif'
}

#the number of each resource the player has.
inventory = {
  DIRT    : 5,
  GRASS   : 0,
  WATER   : 0,
  BRICK   : 1,
  WOOD    : 0,
  GLASS   : 0,
  PLANK   : 5,
  SAND    : 0,
  GRAVEL  : 0,
  CLAY    : 0,
  STICK   : 2,
  IRONINGOT : 4,
  SWORD   : 0,
  WHITEWOOL : 6,
  GRASSPATH : 2,
  STONE   : 0,
  GOLDINGOT : 0,
  BUSHYGRASS : 0
}

#the player image.
playerImg = 'player.gif'

#the player position.
playerX = 0
playerY = 0

#rules to make new resources.
crafting = {
  BRICK    : { WATER : 1, CLAY : 3 },
  GLASS    : { SAND : 2, WATER : 1 },
  STICK    : { PLANK : 1 },
  SWORD    : { IRONINGOT : 2, STICK : 1 },
  PLANK    : { WOOD : 1}
  
}

#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',
  GLASS : '5',
  WOOD  : '6',
  PLANK : '7',
  SAND  : '8',
  GRAVEL: '9',
  CLAY  : '0',
  STICK : '-',
  IRONINGOT : '=',
  SWORD : '+',
  WHITEWOOL : 'p',
  GRASSPATH : 'o',
  STONE : 'i',
  GOLDINGOT : 'u',
  BUSHYGRASS : 'k'
  
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r',
  GLASS : 't',
  STICK : 'y',
  SWORD : 'u',
  PLANK : 'i'
  
}
#game instructions that are displayed.
instructions =  [
  'Game Instructions:',
  'Use the WASD keys to move, space bar to pick up blocks.',
  'Look at the inventory bars to find crafting recipies, and keybinds to place certain blocks..',
  'Version: 2Craft b1.3.5',
  'Not sure if you have the newest version? Go to https://github.com/popdynamite5511/2craft',
  'and click on Releases to see if there is a newer version.'
  
]
