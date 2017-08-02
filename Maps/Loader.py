from Dungeon.Room import Room
import PreBuilt

currentDungeon = PreBuilt.demo_level;


#===============================
# Set the dungeon to be loaded
#===============================
def setDungeon(index):
    global currentDungeon;
    currentDungeon = PreBuilt.allLevels[index];
    return;


#=============================
# Parse and load the dungeon
#=============================
def load():

    global currentDungeon;

    #Set up size of dungeon
    dungeon = __sizeIt(length(),width(),height());


    for i in range(0,length()):
        for j in range(0,width()):
            for k in range(0,height()):

                #Parse out all variables
                top =    currentDungeon[4][i][j][k][0]
                bottom = currentDungeon[4][i][j][k][1]
                left =   currentDungeon[4][i][j][k][2]
                right =  currentDungeon[4][i][j][k][3]
                item =   currentDungeon[4][i][j][k][4]

                #print i,j,k
                
                dungeon[i][j][k] = Room(top,bottom,left,right,item);


    #print dungeon;
    return dungeon;




#========================================
# Set up an array for the correct size
#   Len = X width
#   Wid = Y Width
#   Hei = Number of levels
#=======================================
def __sizeIt(length,width,height):

    dungeon = [0] * length
    for i in range(0,length):
        dungeon[i] = [0]*width
        for j in range(0,width):
            dungeon[i][j] = [0] * height

    return dungeon;


#=============================
# Get starting X, Y, or Z position
# for pre-build dungeon
#=============================
def startX():
    global currentDungeon;
    return currentDungeon[0];

def startY():
    global currentDungeon;
    return currentDungeon[1];

def startZ():
    global currentDungeon;
    return currentDungeon[2];


#==================================
# Get the starting energy for the
#   pre-built dungeon
#==================================
def startEnergy():
    global currentDungeon;
    return currentDungeon[3];


#=======================================
# Get the length, width, or height of
#   the prebuilt dungeon
#=======================================
def length():
    global currentDungeon;
    return len(currentDungeon[4]);


def width():
    global currentDungeon;
    return len(currentDungeon[4][0]);


def height():
    global currentDungeon;
    return len(currentDungeon[4][0][0]);



#================================
# Get the total number of levels
#  programmed into the game
#=================================
def levelCount():
    return len(PreBuilt.allLevels);
