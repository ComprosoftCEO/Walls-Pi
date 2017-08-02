from sense_hat import SenseHat
import random
from Graphics import Images
from Graphics import Screen
from Dungeon.Room import Room
import Game
from time import sleep


sense = Screen._sense


#Define animation colors
__waterColors = [(0,0,255),(0,0,0),(0,0,192),(0,0,0),(0,0,128),(0,0,0),(0,0,64)]
__lavaColors = [(255,0,0),(0,0,0),(192,64,0),(0,0,0),(64,64,0),(0,0,0),(128,64,0)]



#Directions
SCROLL_UP = 0
SCROLL_DOWN = 1
SCROLL_LEFT = 2
SCROLL_RIGHT = 3


#====================================
# Display a full screen splash image
#    when item is collected
#====================================
def itemSplash(key):
    new_img = []

    if (key == Room.L_RED_KEY):
        new_img = Images.RED_KEY
        Game.addRedKey()
        
    if (key == Room.L_YELLOW_KEY):
        new_img = Images.YELLOW_KEY
        Game.addYellowKey()
        
    if (key == Room.L_GREEN_KEY):
        new_img = Images.GREEN_KEY
        Game.addGreenKey()
        
    if (key == Room.L_BLUE_KEY):
        new_img = Images.BLUE_KEY
        Game.addBlueKey()

    if (key == Room.L_BOOTS):
        new_img = Images.BOOTS
        Game.findBoots()

    if (key == Room.L_TORCH):
        new_img = Images.TORCH
        Game.findTorch()

    if (key == Room.L_EXIT_ENERGY):
        new_img = Images.ENERGY
        Game.addEnergy()
    

    Screen.setPixels(new_img)
    Screen.draw()
    for i in range(0,10):
        Screen.draw()
        sleep(0.2)

    return;




#================================
# Do any action related to doors
#
# True  = Successful open
# False = Failed to open
#================================
def openDoor(player_x,player_y,door_type,room):

    #Red Door
    if (door_type == Room.L_RED_DOOR and Game.useRed()):
        __findDoor(player_x,player_y,room)
        return True;

    #Yellow Door
    if (door_type == Room.L_YELLOW_DOOR and Game.useYellow()):
        __findDoor(player_x,player_y,room)
        return True;

    #Green Door
    if (door_type == Room.L_GREEN_DOOR and Game.useGreen()):
        __findDoor(player_x,player_y,room)
        return True;

    #Blue Door
    if (door_type == Room.L_BLUE_DOOR and Game.useBlue()):
        __findDoor(player_x,player_y,room)
        return True;

    return False;



#================================
# Figure out which door to open
#   top/bottom/left/right
#================================
def __findDoor(x,y,room):
    
    #Top:
    if (y == 1 and (x == 3 or x == 4)):
        room.unlockDoor(Room.DOOR_TOP)

    #Bottom:
    if (y == 6 and (x == 3 or x == 4)):
        room.unlockDoor(Room.DOOR_BOTTOM)

    #Left:
    if (x == 1 and (y == 3 or y == 4)):
        room.unlockDoor(Room.DOOR_LEFT)

    #Right:
    if (x == 6 and (y == 3 or y == 4)):
        room.unlockDoor(Room.DOOR_RIGHT)

    return;



#=====================================
# Do actions related to opening exits
#
# True  = Successful open
# False = Failed to open
#======================================
def openExit(x,y,energy_needed,room):
    if (Game.getEnergy() < energy_needed):
        return False;

    #There is enough energy!
    #  so which exit to open???

    #Top:
    if (y == 0 and (x == 3 or x == 4)):
        room.unlockExit(Room.DOOR_TOP);
        return True;

    #Bottom
    if (y == 7 and (x == 3 or x == 4)):
        room.unlockExit(Room.DOOR_BOTTOM);
        return True;

    #Left
    if (x == 0 and (y == 3 or y == 4)):
        room.unlockExit(Room.DOOR_LEFT);
        return True;

    if (x == 7 and (y == 3 or y == 4)):
        room.unlockExit(Room.DOOR_RIGHT);
        return True;


    #Should not get here, but just to be safe...
    return False;




#============================
# Do water/lava event here:
#
#   True  = Can Walk
#   False = Cannot Walk
#============================
def splash(x,y,isWater,room):

    #First test for boots
    if (isWater == True and Game.hasBoots() == True):
        return True;

    if (isWater == True):
        Screen.setPixels(room.buildScreen(Game.hasTorch()));
        __colorSequence(x,y,__waterColors,room);        

    if (isWater == False):
        Screen.setPixels(room.buildScreen(Game.hasTorch()));
        __colorSequence(x,y,__lavaColors,room); 
        
    return False;
    


    

#===================================
#Show 3 colors, one right after the
#   other, in sequence
#
#  colors is array of colors
#====================================
def __colorSequence(x,y,colors,room):

    for i in range(0,len(colors)):
        #When to update the screen
        if (i % 4 == 3):
            Screen.setPixels(room.buildScreen(Game.hasTorch()));
        
        Screen.setPixel(x,y,colors[i])
        Screen.draw()
        sleep(0.05)

    return;



#=============================
# Move up and down staircase
#=============================
def staircase(room,isUp,color):

    if (isUp == True):
        Game.__playerX = 3
        Game.__playerY = 3
        Game.__screenZ += 1
    else:
        Game.__playerX = 4
        Game.__playerY = 4
        Game.__screenZ -= 1

    #Update the screen
    Screen.setBGColor(color);
    Screen.setPixels(room.buildScreen(Game.hasTorch()));

    #Show the fade animation
    for i in range(1,5):

        if (i % 2 == 1):
            Screen.setPixels(room.buildScreen(Game.hasTorch()));
                
        for j in range(0,i):
            Screen.shiftUp();
        for j in range(0,i):
            Screen.shiftDown();

        for j in range(0,i):
            Screen.shiftLeft();
        for j in range(0,i):
            Screen.shiftRight();

        for j in range(0,i):
            Screen.shiftDown();
        for j in range(0,i):
            Screen.shiftUp();

        for j in range(0,i):
            Screen.shiftRight();
        for j in range(0,i):
            Screen.shiftLeft();

        Screen.draw();
        sleep(0.1);
    Game.respawn();
    return;



#=================================
# Scroll from room 1 into room 2
#   room1 = Old Room
#   room2 = New Room
#
#   X/Y = Location in new room
#=================================
def scroll(direction,room1,room2,x,y):


    if (direction == SCROLL_UP):
        for i in range(1,8):
            screen_old = room1.buildScreen(Game.hasTorch());
            screen_new = room2.buildScreen(Game.hasTorch());
            screen_new[y*8 + x] = (255,255,255);
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftDown();
                Screen.copyRow(screen_new,7-j,0);
            Screen.draw();
            sleep(0.1);


    if (direction == SCROLL_DOWN):
        for i in range(1,8):
            screen_old = room1.buildScreen(Game.hasTorch());
            screen_new = room2.buildScreen(Game.hasTorch());
            screen_new[y*8 + x] = (255,255,255);
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftUp();
                Screen.copyRow(screen_new,j,7);
            Screen.draw();
            sleep(0.1);



    if (direction == SCROLL_LEFT):
        for i in range(1,8):
            screen_old = room1.buildScreen(Game.hasTorch());
            screen_new = room2.buildScreen(Game.hasTorch());
            screen_new[y*8 + x] = (255,255,255);
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftRight();
                Screen.copyCol(screen_new,7-j,0);
            Screen.draw();
            sleep(0.1);


    if (direction == SCROLL_RIGHT):
        for i in range(1,8):
            screen_old = room1.buildScreen(Game.hasTorch());
            screen_new = room2.buildScreen(Game.hasTorch());
            screen_new[y*8 + x] = (255,255,255);
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftLeft();
                Screen.copyCol(screen_new,j,7);
            Screen.draw();
            sleep(0.1);



#========================================
# Scroll from room 1 into ending screen
#   room1 = Old Room
#========================================
def winScreen(direction,room):

    #New Screen to show!
    screen_new = Images.WIN

    if (direction == SCROLL_UP):
        for i in range(1,9):
            screen_old = room.buildScreen(Game.hasTorch());
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftDown();
                Screen.copyRow(screen_new,7-j,0);
            Screen.draw();
            sleep(0.2);


    if (direction == SCROLL_DOWN):
        for i in range(1,9):
            screen_old = room.buildScreen(Game.hasTorch());
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftUp();
                Screen.copyRow(screen_new,j,7);
            Screen.draw();
            sleep(0.2);


    if (direction == SCROLL_LEFT):
        for i in range(1,9):
            screen_old = room.buildScreen(Game.hasTorch());
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftRight();
                Screen.copyCol(screen_new,7-j,0);
            Screen.draw();
            sleep(0.2);


    if (direction == SCROLL_RIGHT):
        for i in range(1,9):
            screen_old = room.buildScreen(Game.hasTorch());
            
            Screen.setPixels(screen_old);
            for j in range(0,i):
                Screen.shiftLeft();
                Screen.copyCol(screen_new,j,7);
            Screen.draw();
            sleep(0.2);


    sleep(10);
    sense.show_message("You Win!",0.1,Screen.randomColor());
    sleep(5)
    return;

