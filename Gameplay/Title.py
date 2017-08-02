from sense_hat import SenseHat
from time import sleep
from Graphics import Screen

sense = Screen._sense
stop = False


def showTitle():
    global stop

    # Set up functions
    sense.stick.direction_any = __hideTitle
    sense.stick.direction_up = __nothing
    sense.stick.direction_down = __nothing
    sense.stick.direction_left = __nothing 
    sense.stick.direction_right = __nothing

    stop = False
    while (stop == False):
        sense.show_message("Walls", 0.1 ,Screen.randomColor());
        
        if (stop): break;

        sleep(0.5)
        if (stop):  break


        sense.show_message("By", 0.1,Screen.randomColor());
        if (stop):  break

        color = Screen.randomColor();
        sense.show_message("Bryan", 0.1, color);
        if (stop):  break
        sense.show_message("McClain", 0.1, color);
        
    return;



def __hideTitle():
    global stop
    stop = True

    #Flash the screen to notify the person
    Screen.singleColor((64,64,64))
    Screen.draw()
    return;


def __nothing():
    return;
