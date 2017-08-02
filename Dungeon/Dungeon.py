from sense_hat import SenseHat
from time import sleep
from Graphics import Screen
from Room import Room
from Gameplay import Event
from Maps import Loader


class Dungeon:


    #Scroll directions
    SCROLL_UP = 0
    SCROLL_DOWN = 1
    SCROLL_LEFT = 2
    SCROLL_RIGHT = 3


    #=====================================
    #Create a new dungeon from the loader:
    #
    #    Length - X Length (Not Used)
    #    Width - Y Length (Not Used)
    #    Height - Number of levels (Not Used)
    #======================================
    def __init__(self):
        self.length = Loader.length();
        self.width = Loader.width();
        self.height = Loader.height();
        self.energy = Loader.startEnergy();

        #Define default dungeon
        self.dungeon = Loader.load();
        self.startX = Loader.startX();
        self.startY = Loader.startY();
        self.startZ = Loader.startZ();

        return;

    #=============================
    # Get starting X, Y, or Z position
    # for pre-build dungeon
    #=============================
    def getStartX(self):
        return self.startX;

    def getStartY(self):
        return self.startY;

    def getStartZ(self):
        return self.startZ;




    #==============================
    # Get pixel colors for screen
    #   in X,Y,Z
    #==============================
    def getScreen(self,x,y,z,isDark):
        return self.dungeon[x][y][z].buildScreen(isDark);



    #================================
    # Get the total amount of energy
    #   needed to win
    #================================
    def getEnergy(self):
        return self.energy


    #=======================================
    # Do effect at X,Y position in the room,
    #   and update the dungeon accordingly
    #
    # True = Player can stay
    # False = Return to previous spot
    #========================================
    def doEffect(self,x,y,z,player_x,player_y):

        #You can always move outside of screen!
        if (player_x < 0 or player_x > 7 or player_y < 0 or player_y > 7):
            return True;

        action = self.dungeon[x][y][z].getSpot(player_x,player_y);

        if (action == Room.L_WALL or (action >= Room.L_RED_OPENED and action <= Room.L_EXIT_OPENED)):
            return False;

        if (action >= Room.L_BOOTS and action <= Room.L_EXIT_ENERGY):
            self.dungeon[x][y][z].collectItem()
            Event.itemSplash(action);
            return True;

        if (action >= Room.L_RED_DOOR and action <= Room.L_BLUE_DOOR):
            return Event.openDoor(player_x,player_y,action,self.dungeon[x][y][z]);

        if (action == Room.L_WATER):
            return Event.splash(player_x,player_y,True,self.dungeon[x][y][z]);

        if (action == Room.L_LAVA):
            return Event.splash(player_x,player_y,False,self.dungeon[x][y][z]);

        if (action == Room.L_STAIR_UP):
            Event.staircase(self.dungeon[x][y][z],True,(128,64,64));
            return False;

        if (action == Room.L_STAIR_DOWN):
            Event.staircase(self.dungeon[x][y][z],False,(64,128,128));
            return False;

        if (action == Room.L_EXIT):
            return Event.openExit(player_x,player_y,self.energy,self.dungeon[x][y][z]);

        return True;



    #=====================================
    # Scroll the dungeon into a new room
    #
    #   This is technically an effect
    #=====================================
    def scroll(self,direction,room_x,room_y,z,p_x,p_y):


        #Two rooms to find:
        room1 = self.dungeon[room_x][room_y][z]
        room2 = 0


        if (direction == Dungeon.SCROLL_UP):
            room2 = self.dungeon[room_x][room_y-1][z]

        if (direction == Dungeon.SCROLL_DOWN):
            room2 = self.dungeon[room_x][room_y+1][z]

        if (direction == Dungeon.SCROLL_LEFT):
            room2 = self.dungeon[room_x-1][room_y][z]
            
        if (direction == Dungeon.SCROLL_RIGHT):
            room2 = self.dungeon[room_x+1][room_y][z]
        
        Event.scroll(direction,room1,room2,p_x,p_y);



    #=============================
    # Test when to do win action!
    #=============================
    def testWin(self,screen_x,screen_y,screen_z,x,y,direction):
        action = self.dungeon[screen_x][screen_y][screen_z].getSpot(x,y);
        room = self.dungeon[screen_x][screen_y][screen_z]

        if (direction == Dungeon.SCROLL_UP and action == Room.L_UP_EXIT):
            Event.winScreen(direction,room);
            return True;
        elif (direction == Dungeon.SCROLL_DOWN and action == Room.L_DOWN_EXIT):
            Event.winScreen(direction,room);
            return True;
        elif (direction == Dungeon.SCROLL_LEFT and action == Room.L_LEFT_EXIT):
            Event.winScreen(direction,room);
            return True;
        elif (direction == Dungeon.SCROLL_RIGHT and action == Room.L_RIGHT_EXIT):
            Event.winScreen(direction,room);
            return True;

        return False;


