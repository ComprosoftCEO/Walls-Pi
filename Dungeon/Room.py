from Graphics import Screen
import random



#Represents a single room in the dungeon
class Room:

    #Constants for wall types:
    #===========================
    # USED IN CONSTRUCTOR!!!
    #  Use with updateWall
    C_NO_WALL = 0
    C_RED_DOOR = 1
    C_YELLOW_DOOR = 2
    C_GREEN_DOOR = 3
    C_BLUE_DOOR = 4
    C_WATER = 5
    C_LAVA = 10
    C_EXIT = 15
    C_WALL = 30
    C_SECRET = 45

    #Constants for center types
    #=============================
    # USED IN CONSTRUCTOR!!!!!
    # Use with updateItem
    C_NO_ITEM = 0
    C_WATER_CENTER = 1
    C_LAVA_CENTER = 2
    C_RED_KEY = 3
    C_YELLOW_KEY = 6
    C_GREEN_KEY = 9
    C_BLUE_KEY = 12
    C_BOOTS = 15
    C_TORCH = 18
    C_STAIR_UP = 21
    C_STAIR_DOWN = 24
    C_STAIR_UP_DOWN = 27
    C_EXIT_ENERGY = 30



    #Door type constnats
    #===========================
    #   Use with self.xxx_door
    NO_DOOR = 0
    RED_DOOR = 1
    YELLOW_DOOR = 2
    GREEN_DOOR = 3
    BLUE_DOOR = 4

    #Set to this when doors are opened
    RED_OPEN = 5
    YELLOW_OPEN = 6
    GREEN_OPEN = 7
    BLUE_OPEN = 8


    #Liquid constants
    #=============================
    #  Use with self.xxx_liquid
    #  Use with self.center_liquid
    NO_LIQUID = 0
    WATER_LIQUID = 1
    LAVA_LIQUID = 2


    #Wall type constants
    #===========================
    #   Use with self.xxx_type
    NO_WALL = 0
    EXIT_WALL = 1
    SOLID_WALL = 2
    SECRET_WALL = 3

    #Set this when exit is opened!
    EXIT_OPENED = 4
    



    #Item Type Constants
    #============================
    #  Use with self.item
    NO_ITEM = 0
    RED_KEY = 1
    YELLOW_KEY = 2
    GREEN_KEY = 3
    BLUE_KEY = 4
    BOOTS = 5
    TORCH = 6
    STAIR_UP = 7
    STAIR_DOWN = 8
    STAIR_UP_DOWN = 9
    EXIT_ENERGY = 10


    #Room Darkness constants
    #==============================
    #  Used with self.room_dark
    ROOM_LIT = 0
    ROOM_DARK = 1



    #Color constants
    #=================================
    __NULL_COLOR = (0,0,0)
    __RED_DOOR_KEY = (255,0,0)
    __YELLOW_DOOR_KEY = (255,255,0)
    __GREEN_DOOR_KEY = (0,255,0)
    __BLUE_DOOR_KEY = (0,0,255)
    __BOOT_COLOR = (0,64,64)
    __TORCH_COLOR = (128,64,0)
    __STAIR_UP = (255,128,128)
    __STAIR_DOWN = (128,255,255)



    #Constants used for room layout
    #================================
    L_NOTHING = 0
    L_WALL = 1
    L_SECRET_WALL= 2
    L_EXIT = 3

    L_RED_DOOR = 4
    L_YELLOW_DOOR = 5
    L_GREEN_DOOR = 6
    L_BLUE_DOOR = 7

    L_WATER = 8
    L_LAVA = 9

    L_BOOTS = 10
    L_TORCH = 11
    L_RED_KEY = 12
    L_YELLOW_KEY = 13
    L_GREEN_KEY = 14
    L_BLUE_KEY = 15
    L_EXIT_ENERGY = 16

    L_STAIR_UP = 17
    L_STAIR_DOWN = 18

    L_RED_OPENED = 20
    L_YELLOW_OPENED = 21
    L_GREEN_OPENED = 22
    L_BLUE_OPENED = 23
    L_EXIT_OPENED = 24

    L_UP_EXIT = 25
    L_DOWN_EXIT = 26
    L_LEFT_EXIT = 27
    L_RIGHT_EXIT = 28
    



    #Directions for which doors to open
    #====================================
    # Use with UnlockDoor function
    DOOR_TOP = 0
    DOOR_BOTTOM = 1
    DOOR_LEFT = 2
    DOOR_RIGHT = 3

    


    #===============================================
    #Create a new room in the dungeon
    #
    # Top/Bottom/Left/Right Wall = Wall Obstacles
    #     ex) NOTHING + RED_DOOR + WATER
    #
    # Item = What to put in middle of room
    #     ex) BLUE_KEY + WATER_CENTER
    #===============================================
    def __init__(self,
                 top_wall, bottom_wall, left_wall, right_wall,
                 center_item):


        #Door Variables (RED, YELLOW, Green, etc.)
        self.top_door = top_wall % 5
        self.bottom_door = bottom_wall % 5
        self.left_door = left_wall % 5
        self.right_door = right_wall % 5

        #Water or Lava?
        self.top_liquid = (top_wall % 15) / 5
        self.bottom_liquid = (bottom_wall % 15) / 5
        self.left_liquid = (left_wall % 15) / 5
        self.right_liquid = (right_wall % 15) / 5

        #What type of wall?
        self.top_type = top_wall / 15
        self.bottom_type = bottom_wall / 15
        self.left_type = left_wall / 15
        self.right_type = right_wall / 15


        #Center varibles
        self.center_liquid = center_item % 3
        self.item = center_item / 3

        #Choose wall color and darkness
        self.wall_color = Screen.randomColor()
        if (random.randint(0,100) > 80):
            self.room_dark = Room.ROOM_DARK
        else:
            self.room_dark = Room.ROOM_LIT


        # Holds the position in the room of all
        #   these thingies
        self.layout = [0] * 64


        #Rainbow effect for exit
        self.rainbow_red = 250
        self.rainbow_green = 0
        self.rainbow_blue = 0
        self.rainbow_2 = False

        #ALWAYS build the layout
        self.__buildLayout()
        
        return;




    #======================================
    #Convert an integer to a liquid color
    #======================================
    def __getLiquidType(self,val):
        if (val == Room.WATER_LIQUID):
            return Room.L_WATER;
        elif (val == Room.LAVA_LIQUID):
            return Room.L_LAVA;
        else:
            return Room.L_NOTHING;



    #=============================================
    # Get the color to use for this corner
    #    Resolves all issued with liquid corners
    #==============================================
    def __getLiquidCorner(self,color1, color2):

            #Colors are the same (don't matter)
            if (color1 == color2):
                return self.__getLiquidType(color1);

            #Get whatever color is not null
            elif (color1 == Room.NO_LIQUID or color2 == Room.NO_LIQUID): 
                if (color1 == Room.NO_LIQUID):
                    return self.__getLiquidType(color2);
                else:
                    return self.__getLiquidType(color1);
                
            #Pick between lava and water
            else:
                if (random.randint(0,100) < 30):
                    return Room.L_WATER;
                else:
                    return Room.L_LAVA;


    #========================================
    # Convert center liquid into layout type
    #========================================
    def __getMiddleLiquid(self):
        if (self.center_liquid == Room.WATER_LIQUID):
            return Room.L_WATER;
        elif (self.center_liquid == Room.LAVA_LIQUID):
            return Room.L_LAVA;
        else:
            return Room.L_NOTHING;



    #========================================
    # Get the layout value for a closed door
    #========================================
    def __getClosedDoor(self,var):
        if (var == Room.NO_DOOR or var >= Room.RED_OPEN):
            return Room.L_NOTHING;
        elif (var == Room.RED_DOOR):
            return Room.L_RED_DOOR;
        elif (var == Room.YELLOW_DOOR):
            return Room.L_YELLOW_DOOR;
        elif (var == Room.GREEN_DOOR):
            return Room.L_GREEN_DOOR;
        elif (var == Room.BLUE_DOOR):
            return Room.L_BLUE_DOOR;
        else:
            return Room.L_NOTHING;


    #======================================
    #Get layout values for spot where an
    #    opened door would go
    #======================================
    def __getOpenDoor(self,var):
        if (var <= Room.BLUE_DOOR):
            return Room.L_WALL;
        elif (var == Room.RED_OPEN):
            return Room.L_RED_OPENED;
        elif (var == Room.YELLOW_OPEN):
            return Room.L_YELLOW_OPENED;
        elif (var == Room.GREEN_OPEN):
            return Room.L_GREEN_OPENED;
        elif (var == Room.BLUE_OPEN):
            return Room.L_BLUE_OPENED;


    #========================================  
    # Convert wall types (wall,secret,exit)
    #  to a layout type
    #========================================
    def __getWallType(self,var,opened):
        if (var == Room.NO_WALL):
            return Room.L_NOTHING;
        elif (var == Room.EXIT_OPENED):
            return opened;
        elif (var == Room.SOLID_WALL):
            return Room.L_WALL;
        elif (var == Room.SECRET_WALL):
            return Room.L_SECRET_WALL
        elif (var == Room.EXIT_WALL):
            return Room.L_EXIT;
        else:
            return Room.L_NOTHING;
        




    #====================================
    #Build the room using the parameters
    #====================================
    def __buildLayout(self):

        self.layout = [(0,0,0)] * 64

        #Sections of wall are always set
        self.layout[0    ] = self.L_WALL
        self.layout[1    ] = self.L_WALL
        self.layout[2    ] = self.L_WALL
        self.layout[5    ] = self.L_WALL
        self.layout[6    ] = self.L_WALL
        self.layout[7    ] = self.L_WALL
        self.layout[1*8  ] = self.L_WALL
        self.layout[1*8+7] = self.L_WALL
        self.layout[2*8  ] = self.L_WALL
        self.layout[2*8+7] = self.L_WALL
        self.layout[5*8  ] = self.L_WALL
        self.layout[5*8+7] = self.L_WALL
        self.layout[6*8  ] = self.L_WALL
        self.layout[6*8+7] = self.L_WALL
        self.layout[7*8  ] = self.L_WALL
        self.layout[7*8+1] = self.L_WALL
        self.layout[7*8+2] = self.L_WALL
        self.layout[7*8+5] = self.L_WALL
        self.layout[7*8+6] = self.L_WALL
        self.layout[7*8+7] = self.L_WALL

        #Create water/lava
        for i in range(3,5):
            self.layout[1*8 + i] = self.__getLiquidType(self.top_liquid)
            self.layout[2*8 + i] = self.__getLiquidType(self.top_liquid)
            self.layout[5*8 + i] = self.__getLiquidType(self.bottom_liquid)
            self.layout[6*8 + i] = self.__getLiquidType(self.bottom_liquid)
            self.layout[i*8 + 1] = self.__getLiquidType(self.left_liquid)
            self.layout[i*8 + 2] = self.__getLiquidType(self.left_liquid)
            self.layout[i*8 + 5] = self.__getLiquidType(self.right_liquid)
            self.layout[i*8 + 6] = self.__getLiquidType(self.right_liquid)
            
            #Calcualte corners
            self.layout[1*8 + (i-2)] =  self.__getLiquidCorner(self.top_liquid,self.left_liquid)
            self.layout[2*8 + (i-2)] =  self.__getLiquidCorner(self.top_liquid,self.left_liquid)
            self.layout[5*8 + (i-2)] =  self.__getLiquidCorner(self.bottom_liquid,self.left_liquid)
            self.layout[6*8 + (i-2)] =  self.__getLiquidCorner(self.bottom_liquid,self.left_liquid)
            self.layout[1*8 + (i+2)] =  self.__getLiquidCorner(self.top_liquid,self.right_liquid)
            self.layout[2*8 + (i+2)] =  self.__getLiquidCorner(self.top_liquid,self.right_liquid)
            self.layout[5*8 + (i+2)] =  self.__getLiquidCorner(self.bottom_liquid,self.right_liquid)
            self.layout[6*8 + (i+2)] =  self.__getLiquidCorner(self.bottom_liquid,self.right_liquid)


        #Center Liquid
        if (self.center_liquid != Room.NO_LIQUID):
            self.layout[8*2 + 2] = self.__getMiddleLiquid()
            self.layout[8*2 + 3] = self.__getMiddleLiquid()
            self.layout[8*2 + 4] = self.__getMiddleLiquid()
            self.layout[8*2 + 5] = self.__getMiddleLiquid()
            self.layout[8*3 + 2] = self.__getMiddleLiquid()
            self.layout[8*4 + 2] = self.__getMiddleLiquid()
            self.layout[8*3 + 5] = self.__getMiddleLiquid()
            self.layout[8*4 + 5] = self.__getMiddleLiquid()
            self.layout[8*5 + 2] = self.__getMiddleLiquid()
            self.layout[8*5 + 3] = self.__getMiddleLiquid()
            self.layout[8*5 + 4] = self.__getMiddleLiquid()
            self.layout[8*5 + 5] = self.__getMiddleLiquid()


        #Doors!
        if (self.top_door != Room.NO_DOOR):
            self.layout[1*8 + 3] = self.__getClosedDoor(self.top_door)
            self.layout[1*8 + 4] = self.__getClosedDoor(self.top_door)
        if (self.bottom_door != Room.NO_DOOR):
            self.layout[6*8 + 3] = self.__getClosedDoor(self.bottom_door)
            self.layout[6*8 + 4] = self.__getClosedDoor(self.bottom_door)
        if (self.left_door != Room.NO_DOOR):
            self.layout[3*8 + 1] = self.__getClosedDoor(self.left_door)
            self.layout[4*8 + 1] = self.__getClosedDoor(self.left_door)
        if (self.right_door != Room.NO_DOOR):
            self.layout[3*8 + 6] = self.__getClosedDoor(self.right_door)
            self.layout[4*8 + 6] = self.__getClosedDoor(self.right_door)  


        #Open door effect
        self.layout[0*8 + 2] = self.__getOpenDoor(self.top_door)
        self.layout[0*8 + 5] = self.__getOpenDoor(self.top_door)     
        self.layout[7*8 + 2] = self.__getOpenDoor(self.bottom_door)
        self.layout[7*8 + 5] = self.__getOpenDoor(self.bottom_door)
        self.layout[2*8 + 0] = self.__getOpenDoor(self.left_door)
        self.layout[5*8 + 0] = self.__getOpenDoor(self.left_door)
        self.layout[2*8 + 7] = self.__getOpenDoor(self.right_door)
        self.layout[5*8 + 7] = self.__getOpenDoor(self.right_door)


        #Calculate special walls:
        self.layout[0*8 + 3] = self.__getWallType(self.top_type,Room.L_UP_EXIT)
        self.layout[0*8 + 4] = self.__getWallType(self.top_type,Room.L_UP_EXIT)
        self.layout[7*8 + 3] = self.__getWallType(self.bottom_type,Room.L_DOWN_EXIT)
        self.layout[7*8 + 4] = self.__getWallType(self.bottom_type,Room.L_DOWN_EXIT)
        self.layout[3*8 + 0] = self.__getWallType(self.left_type,Room.L_LEFT_EXIT)
        self.layout[4*8 + 0] = self.__getWallType(self.left_type,Room.L_LEFT_EXIT)
        self.layout[3*8 + 7] = self.__getWallType(self.right_type,Room.L_RIGHT_EXIT)
        self.layout[4*8 + 7] = self.__getWallType(self.right_type,Room.L_RIGHT_EXIT)

        #Overwrite walls for 4-wide exit
        if (self.top_type == Room.EXIT_WALL):
            self.layout[0*8 + 2] = Room.L_EXIT
            self.layout[0*8 + 5] = Room.L_EXIT

        if (self.bottom_type == Room.EXIT_WALL):
            self.layout[7*8 + 2] = Room.L_EXIT
            self.layout[7*8 + 5] = Room.L_EXIT

        if (self.left_type == Room.EXIT_WALL):
            self.layout[2*8 + 0] = Room.L_EXIT
            self.layout[5*8 + 0] = Room.L_EXIT

        if (self.right_type == Room.EXIT_WALL):
            self.layout[2*8 + 7] = Room.L_EXIT
            self.layout[5*8 + 7] = Room.L_EXIT


        #Do special exits
        for i in range(0,2):
            for j in range(2,6,3):
                if (self.top_type == Room.EXIT_OPENED):
                    self.layout[i*8 + j] = Room.L_EXIT_OPENED
                    
                if (self.bottom_type == Room.EXIT_OPENED):
                    self.layout[(7-i)*8 + j] = Room.L_EXIT_OPENED
                    
                if (self.left_type == Room.EXIT_OPENED):
                    self.layout[j*8 + i] = Room.L_EXIT_OPENED

                if (self.right_type == Room.EXIT_OPENED):
                    self.layout[j*8 + (7-i)] = Room.L_EXIT_OPENED

        #Items:
        if (self.item == Room.RED_KEY):
            self.layout[8*3 + 3] = Room.L_RED_KEY
        if (self.item == Room.YELLOW_KEY):
            self.layout[8*3 + 3] = Room.L_YELLOW_KEY
        if (self.item == Room.GREEN_KEY):
            self.layout[8*3 + 3] = Room.L_GREEN_KEY
        if (self.item == Room.BLUE_KEY):
            self.layout[8*3 + 3] = Room.L_BLUE_KEY
        if (self.item == Room.BOOTS):
            self.layout[8*3 + 3] = Room.L_BOOTS
            self.layout[8*3 + 4] = Room.L_BOOTS
        if (self.item == Room.TORCH):
            self.layout[8*3 + 3] = Room.L_TORCH
            self.layout[8*3 + 4] = Room.L_TORCH
        if (self.item == Room.EXIT_ENERGY):
            self.layout[8*3 + 3] = Room.L_EXIT_ENERGY


        #Stairs
        if (self.item == Room.STAIR_UP or self.item == Room.STAIR_UP_DOWN):
            self.layout[8*4 + 3] = Room.L_STAIR_UP
        if (self.item == Room.STAIR_DOWN or self.item == Room.STAIR_UP_DOWN):
            self.layout[8*3 + 4] = Room.L_STAIR_DOWN
        

        return;





    #=========================================
    # Turn the layout into actual, physical
    #  pixel colors
    #=========================================
    def buildScreen(self,isDark):

            room = [(0,0,0)] * 64

            #Update exit rainbow effect
            self.__nextColor()    
        
            #Loop through everything and build!
            for i in range(0,64):
                
                spot = self.layout[i]

                #------Only show if room is lit (or you have torch):-----
                if (self.room_dark == Room.ROOM_LIT or isDark):
                    if (spot == Room.L_WALL or spot == Room.L_SECRET_WALL):
                        room[i] = self.wall_color
                        
                    #Make random water color                    
                    if (spot == Room.L_WATER):
                         room[i] = (0, random.randint(0,74), random.randint(74,255))

                    #Make random lava color    
                    if (spot == Room.L_LAVA):
                        room[i] = (random.randint(74,255), random.randint(0,74), 0)



                #---These ones are always visible


                #Doors
                if (spot == Room.L_RED_DOOR or spot == Room.L_RED_OPENED):
                    room[i] = Room.__RED_DOOR_KEY
                        
                if (spot == Room.L_YELLOW_DOOR or spot == Room.L_YELLOW_OPENED):
                    room[i] = Room.__YELLOW_DOOR_KEY
                        
                if (spot == Room.L_GREEN_DOOR or spot == Room.L_GREEN_OPENED):
                    room[i] = Room.__GREEN_DOOR_KEY
                        
                if (spot == Room.L_BLUE_DOOR or spot == Room.L_BLUE_OPENED):
                    room[i] = Room.__BLUE_DOOR_KEY

                #Exit
                if (spot == Room.L_EXIT or spot == Room.L_EXIT_OPENED):
                    room[i] = (self.rainbow_red,self.rainbow_green,self.rainbow_blue)


                #Stairs
                if (spot == Room.L_STAIR_UP):
                    room[i] = Room.__STAIR_UP
                if (spot == Room.L_STAIR_DOWN):
                    room[i] = Room.__STAIR_DOWN


                #Keys
                if (spot == Room.L_RED_KEY):
                    room[i] = Room.__RED_DOOR_KEY
                if (spot == Room.L_YELLOW_KEY):
                    room[i] = Room.__YELLOW_DOOR_KEY
                if (spot == Room.L_GREEN_KEY):
                    room[i] = Room.__GREEN_DOOR_KEY
                if (spot == Room.L_BLUE_KEY):
                    room[i] = Room.__BLUE_DOOR_KEY


                #Other Items
                if (spot == Room.L_BOOTS):
                    room[i] = Room.__BOOT_COLOR
                if (spot == Room.L_TORCH):
                    room[i] = Room.__TORCH_COLOR
                if (spot == Room.L_EXIT_ENERGY):
                    room[i] = (self.rainbow_blue,self.rainbow_green,self.rainbow_red)


            return room;





    #===================================
    # Calculate the nexty rainbow color
    #   for the exit effect
    #===================================
    def __nextColor(self):
        if (self.rainbow_2 == False):
            if (self.rainbow_red > 0):
                self.rainbow_red -=50
                self.rainbow_green += 50
            elif (self.rainbow_green > 0):
                self.rainbow_green -=50
                self.rainbow_blue +=50
            else:
                self.rainbow_2 = True
        else:
            if (self.rainbow_blue > 0):
                self.rainbow_blue -=50
                self.rainbow_red +=50
            elif (self.rainbow_red > 0):
                self.rainbow_2 = False

        return;



    #--------------Action Functions---------------------



    #==============================
    # Collect the item in the room
    #==============================
    def collectItem(self):
        self.item = Room.NO_ITEM
        self.__buildLayout()
        return;


    
    #======================================
    # Unlock a red,yellow,green,blue door
    #   on direction up,down,left,right
    #======================================
    def unlockDoor(self,door):
        if (door == Room.DOOR_TOP and self.top_door != 0):
            self.top_door +=4
        elif (door == Room.DOOR_BOTTOM and self.bottom_door != 0):
            self.bottom_door +=4
        elif (door == Room.DOOR_LEFT and self.left_door != 0):
            self.left_door += 4
        elif (door == Room.DOOR_RIGHT and self.right_door != 0):
            self.right_door += 4
        self.__buildLayout()
        return;


    #===================================
    # Unlock exit doors in the room
    #===================================
    def unlockExit(self,door):
        if (door == Room.DOOR_TOP and self.top_type == Room.EXIT_WALL): self.top_type = Room.EXIT_OPENED
        if (door == Room.DOOR_BOTTOM and self.bottom_type == Room.EXIT_WALL): self.bottom_type = Room.EXIT_OPENED
        if (door == Room.DOOR_LEFT and self.left_type == Room.EXIT_WALL): self.left_type = Room.EXIT_OPENED
        if (door == Room.DOOR_RIGHT and self.right_type == Room.EXIT_WALL): self.right_type = Room.EXIT_OPENED
        self.__buildLayout()
        return;
        


    #===================================
    # Return the action/item/wall at a
    #   x,y position in the room
    #===================================
    def getSpot(self, x, y):
        return self.layout[y*8 + x];



    #-------------Mutators------------------


    #=====================================
    #Update a given wall with a new value
    #=====================================
    def updateWall(self,wall,newValue):
        if (wall == Room.DOOR_TOP):
            self.top_door = newValue % 5
            self.top_liquid = (newValue % 15) / 5
            self.top_type = newValue / 15

        elif (wall == Room.DOOR_BOTTOM):
            self.bottom_door = newValue % 5
            self.bottom_liquid = (newValue % 15) / 5
            self.bottom_type = newValue / 15                    

        elif (wall == Room.DOOR_LEFT):
            self.left_door = newValue % 5
            self.left_liquid = (newValue % 15) / 5
            self.left_type = newValue / 15

        elif (wall == Room.DOOR_RIGHT):
            self.right_door = newValue % 5
            self.right_liquid = (newValue % 15) / 5
            self.right_type = newValue / 15
        self.__buildLayout()
        return;


    #====================================
    #Update the item/middle part of room
    #====================================
    def updateItem(self,center_item):
        self.center_liquid = center_item % 3
        self.item = center_item / 3
        self.__buildLayout()
        return;
