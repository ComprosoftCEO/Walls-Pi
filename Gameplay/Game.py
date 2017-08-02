from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED, ACTION_HELD
from time import sleep
from Graphics import Screen
from Dungeon.Dungeon import Dungeon

sense = Screen._sense

# Pause Variables
__paused = False
__pauseScreen = [(0,0,0)] * 64
__playGame = True

#Gameplay elements
__playerX = 0        #Player position in current screen
__playerY = 0

__screenX = 0        #Player position in map screen
__screenY = 0
__screenZ = 0

__noDraw = False

__redKeys = 0
__yellowKeys = 0
__greenKeys = 0
__blueKeys = 0
__exitEnergy = 0
__boots = False
__torch = False


__dungeon = Dungeon();

#==============================
#Initialize game options and
#  Start the game!
#==============================
def initGame():

    #Reset all variables
    resetAll()


    #Define all controller functions
    respawn();
    __enableMovement();

    while(__playGame):
        if (__paused == False and __noDraw == False):
            Screen.setPixels(__prepareScreen())
        if (__noDraw == False): Screen.draw()
        sleep(0.2)
    return;


def __redraw():
    Screen.draw()
    return;




#============================
# Reset all in-game variables
#  to defaultt values
#============================
def resetAll():

    # Make sure to specify that all are GLOBALS!!!
    global __paused, __pauseScreen, __playGame, __noDraw
    global __playerX, __playerY, __screenX, __screenY, __screenZ
    global __redKeys, __yellowKeys, __greenKeys, __blueKeys, __exitEnergy
    global __boots, __torch
    global __dungeon

    __dungeon = Dungeon();

    __paused = False;
    __pauseScreen = [(0,0,0)] * 64;
    __playGame = True;
    __noDraw = False;
    
    __playerX = 3;
    __playerY = 3;
    __screenX = __dungeon.getStartX();
    __screenY = __dungeon.getStartY();
    __screenZ = __dungeon.getStartZ();

    __redKeys = 0;
    __yellowKeys = 0;
    __greenKeys = 0;
    __blueKeys = 0;
    __exitEnergy = 0;
    __boots = False;
    __torch = False;

    return;




#=========================
# Exactly what it says...
#=========================
def __nothing(event):
    return;





#--------------------
# Move the player up
#--------------------
def __moveUp(event):
    global __playerX, __playerY, __noDraw, __screenX, __screenY, __playGame

    if (event.action != ACTION_PRESSED):
        return;

    __disableMovement()
    __noDraw = True
    if (__dungeon.doEffect(__screenX,__screenY,__screenZ,__playerX,__playerY-1) == True):
        __playerY-=1 


        #Test for win first:
        if (__dungeon.testWin(__screenX,__screenY,__screenZ,__playerX,__playerY+1,Dungeon.SCROLL_UP) == True):
            __playGame = False;
            return;

        # Test for scroll
        if (__playerY < 0):
            __playerY = 7
            __screenY-=1;
            __dungeon.scroll(Dungeon.SCROLL_UP,__screenX,__screenY+1,__screenZ,__playerX,__playerY);




    __enableMovement()
    __noDraw = False
    return;


#----------------------
# Move the player down
#----------------------
def __moveDown(event):
    global __playerX, __playerY, __noDraw, __screenX, __screenY, __playGame

    if (event.action != ACTION_PRESSED):
        return;

    __disableMovement()
    __noDraw = True
    if (__dungeon.doEffect(__screenX,__screenY,__screenZ,__playerX,__playerY+1) == True):
        __playerY+=1 


        #Test for win first:
        if (__dungeon.testWin(__screenX,__screenY,__screenZ,__playerX,__playerY-1,Dungeon.SCROLL_DOWN) == True):
            __playGame = False;
            return;
        

        # Test for scroll
        if (__playerY > 7):
            __playerY = 0
            __screenY+=1;
            __dungeon.scroll(Dungeon.SCROLL_DOWN,__screenX,__screenY-1,__screenZ,__playerX,__playerY);




    __enableMovement()
    __noDraw = False
    return;


#---------------------
# Move the player left
#---------------------
def __moveLeft(event):
    global __playerX, __playerY, __noDraw, __screenX, __screenY, __playGame

    if (event.action != ACTION_PRESSED):
        return;
    
    __disableMovement()
    __noDraw = True
    if (__dungeon.doEffect(__screenX,__screenY,__screenZ,__playerX-1,__playerY) == True):
        __playerX-=1


        #Test for win first:
        if (__dungeon.testWin(__screenX,__screenY,__screenZ,__playerX+1,__playerY,Dungeon.SCROLL_LEFT) == True):
            __playGame = False;
            return;


        # Test for scroll
        if (__playerX < 0):
            __playerX = 7
            __screenX-=1;
            __dungeon.scroll(Dungeon.SCROLL_LEFT,__screenX+1,__screenY,__screenZ,__playerX,__playerY);


    __enableMovement()
    __noDraw = False
    return;


#----------------------
# Move the player right
#-----------------------
def __moveRight(event):
    global __playerX, __playerY, __noDraw, __screenX, __screenY, __playGame

    if (event.action != ACTION_PRESSED):
        return;

    __disableMovement()
    __noDraw = True
    if (__dungeon.doEffect(__screenX,__screenY,__screenZ,__playerX+1,__playerY) == True):
        __playerX+=1 

        #Test for win first:
        if (__dungeon.testWin(__screenX,__screenY,__screenZ,__playerX-1,__playerY,Dungeon.SCROLL_RIGHT) == True):
            __playGame = False;
            return;


        # Test for scroll
        if (__playerX > 7):
            __playerX = 0
            __screenX+=1;
            __dungeon.scroll(Dungeon.SCROLL_RIGHT,__screenX-1,__screenY,__screenZ,__playerX,__playerY);


    __enableMovement()
    __noDraw = False
    return;




#===============================================
# Do event if player lands somewhere
#   Called with stairs and other stuff happens
#===============================================
def respawn():
    __disableMovement()
    __noDraw = True

    __dungeon.doEffect(__screenX,__screenY,__screenZ,__playerX,__playerY)

    __enableMovement()
    __noDraw = False
    return;
    


#---------------------
# Show the pause menu
#---------------------
def __showPause(event):

    global __paused, __pauseScreen


    #Only do this on key press
    if (event.action != ACTION_PRESSED):
        return;
    
    __paused = True


    # Store screen information
    __pauseScreen = Screen.getPixels()


    #Draw all of the pause information
    Screen.clear()
    Screen.border((64,64,64))

    #Red Key
    if (__redKeys < 7):
        for i in range(1,__redKeys + 1): Screen.setPixel(i,1,(255,0,0))
    else:
        for i in range(1,7): Screen.setPixel(i,1,(255,0,0))

    #Yellow Key 
    if (__yellowKeys < 7):
        for i in range(1,__yellowKeys + 1): Screen.setPixel(i,2,(255,255,0))
    else:
        for i in range(1,7): Screen.setPixel(i,2,(255,255,0))

    #Green Key
    if (__greenKeys < 7):
        for i in range(1,__greenKeys + 1): Screen.setPixel(i,3,(0,255,0))
    else:
        for i in range(1,7): Screen.setPixel(i,3,(0,255,0))

    #Blue Key
    if (__blueKeys < 7):
        for i in range(1,__blueKeys + 1): Screen.setPixel(i,4,(0,0,255))
    else:
        for i in range(1,7): Screen.setPixel(i,4,(0,0,255))

    #Draw Boots
    if (__boots):
        Screen.setPixel(1,6,(0,64,64))
        Screen.setPixel(2,6,(0,64,64))

    #Draw Torch
    if (__torch):
        Screen.setPixel(4,6,(128,64,0))
        Screen.setPixel(5,6,(128,64,0))
        
    
    Screen.draw()

    # Disable Movement
    sense.stick.direction_any = __nothing
    sense.stick.direction_up = __nothing
    sense.stick.direction_down = __nothing
    sense.stick.direction_left = __nothing
    sense.stick.direction_right = __nothing
    sense.stick.direction_middle = __hidePause
    return;



#-------------------------------
#Return back to normal gameplay
#  from pause screen
#-------------------------------
def __hidePause(event):

    global __paused, __pauseScreen

    #Only do this on key press
    if (event.action != ACTION_PRESSED):
        return;
    
    __paused = False

    # Grab screen information
    Screen.setPixels(__pauseScreen)

    # Re-enable movement
    __enableMovement()
    return;



#================================
#Prepare the screen for drawing:
#================================
def __prepareScreen():
    screen = __dungeon.getScreen(__screenX,__screenY,__screenZ,__torch)

    #Set player position on screen
    if (__playerX >= 0 and __playerX < 8 and __playerY >= 0 and __playerY < 8):
        screen[__playerY * 8 + __playerX] = (255,255,255)
    return screen;




#===========================
# Disable the controller
#===========================
def __disableMovement():
    global sense
    sense.stick.direction_any = __nothing
    sense.stick.direction_up = __nothing
    sense.stick.direction_down = __nothing
    sense.stick.direction_left = __nothing
    sense.stick.direction_right = __nothing
    sense.stick.direction_middle = __nothing
    return;


#===========================
# Enable the controller
#============================
def __enableMovement():
    global sense
    sense.stick.direction_any = __redraw
    sense.stick.direction_up = __moveUp
    sense.stick.direction_down = __moveDown
    sense.stick.direction_left = __moveLeft
    sense.stick.direction_right = __moveRight
    sense.stick.direction_middle = __showPause
    return;



#-----------Outside callable actions---------


#Items collected:
#==================

def addRedKey():
    global __redKeys
    __redKeys+=1;
    return;


def addYellowKey():
    global __yellowKeys
    __yellowKeys+=1;
    return;

def addGreenKey():
    global __greenKeys
    __greenKeys+=1;
    return;

def addBlueKey():
    global __blueKeys
    __blueKeys+=1;
    return;

def addEnergy():
    global __exitEnergy
    __exitEnergy+=1;
    return;
    
def findBoots():
    global __boots
    __boots = True
    return;


def findTorch():
    global __torch
    __torch = True
    return;


#Use Keys and test for items
#============================

def hasBoots():
    return __boots;

def hasTorch():
    return __torch;

def getEnergy():
    return __exitEnergy;


#  True  = Success
#  False = Failure
def useRed():
    global __redKeys
    if (__redKeys <= 0): return False;
    __redKeys -= 1
    return True;


def useYellow():
    global __yellowKeys
    if (__yellowKeys <= 0): return False;
    __yellowKeys -= 1
    return True;


def useGreen():
    global __greenKeys
    if (__greenKeys <= 0): return False;
    __greenKeys -= 1
    return True;


def useBlue():
    global __blueKeys
    if (__blueKeys <= 0): return False;
    __blueKeys -= 1
    return True;
