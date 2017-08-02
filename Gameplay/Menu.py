from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED, ACTION_HELD
from time import sleep
from Graphics import Screen
from Maps import Loader

#List of chars used when displaying menu name
# If it runs out, just loops around
charList = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

sense = Screen._sense
picked = False
currentScreen = 0;


def showMenu():
    global picked

    # Set up functions
    sense.stick.direction_any = __nothing
    sense.stick.direction_up = __nothing
    sense.stick.direction_down = __nothing
    sense.stick.direction_left = __pre_entry
    sense.stick.direction_right = __next_entry
    sense.stick.direction_middle = __select

    picked = False
    while (picked == False):
        sense.show_letter(charList[currentScreen % len(charList)],Screen.randomColor());
        sleep(0.2);
        
    return;



#=========================
# Pick an entry from menu
#==========================
def __select():
    global picked, currentScreen;
    Loader.setDungeon(currentScreen);
    picked = True;

    #Flash the screen to notify the person
    Screen.singleColor((64,64,64))
    Screen.draw()
    return;


#===================================
# Move to the next entry in the list
#===================================
def __next_entry(event):

    if (event.action != ACTION_PRESSED):
        return;

    global currentScreen;
    if (currentScreen < Loader.levelCount() - 1):
        currentScreen +=1;
    else:
        currentScreen = 0;
    
    return;


#========================================
# Move to the previous entry in the list
#========================================
def __pre_entry(event):

    if (event.action != ACTION_PRESSED):
        return;
    
    global currentScreen;
    if (currentScreen > 0):
        currentScreen -=1;
    else:
        currentScreen = Loader.levelCount() - 1;
        
    return;

def __nothing():
    return;
