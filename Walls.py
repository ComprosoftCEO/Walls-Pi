from sense_hat import SenseHat
from time import sleep
import random
from Graphics import Screen
from Gameplay import Title
from Gameplay import Menu
from Gameplay import Game


#Run the game forever!
while (True):
    Title.showTitle();
    Menu.showMenu();
    Game.initGame();
    
