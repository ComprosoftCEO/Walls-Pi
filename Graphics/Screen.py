from sense_hat import SenseHat
from time import sleep
import random

_backgroundColor = (0,0,0)
_image = [(0,0,0)] * 64
_sense = SenseHat()




#======================================
# Draw the background to the sense hat
#======================================
def draw():
    global _image
    _sense.set_pixels(_image)
    return;



#============================
# Pick a pseudo-random color
#============================
# @Return Random color (R,G,B)
def randomColor():
        r = 0
        g = 0
        b = 0

        #Make sure wall is indeed visible
        while (r < 64 and g < 64 and b < 64):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        
        return (r,g,b);





#====================================
# Shift all pixels in the background
#  one to the left
#
#  --Fills in with background color
#====================================
def shiftLeft():
    global _image, _backgroundColor
    for i in range(0,8,1):
        for j in range(0,7,1):
            _image[i*8 + j] = _image[i*8 + (j+1)]
            
    # Clear left most pixels
    for i in range (0,8,1):
        _image[i*8+7] = _backgroundColor
        
    return;



#====================================
# Shift all pixels in the background
#  one to the right
#
#  --Fills in with background color
#====================================
def shiftRight():
    global _image, _backgroundColor
    for i in range(0,8,1):
        for j in range(7,0,-1):
            _image[i*8 + j] = _image[i*8 + (j-1)]
            
    # Clear left most pixels
    for i in range (0,8,1):
        _image[i*8] = _backgroundColor
        
    return;




#====================================
# Shift all pixels in the background
#  one pixel up
#
#  --Fills in with background color
#====================================
def shiftUp():
    global _image, _backgroundColor
    for i in range(0,7,1):
        for j in range(0,8,1):
            _image[i*8 + j] = _image[(i+1)*8 + j]
            
    # Clear left most pixels
    for i in range (0,8,1):
        _image[7*8+i] = _backgroundColor
        
    return;




#====================================
# Shift all pixels in the background
#  one pixel down
#
#  --Fills in with background color
#====================================
def shiftDown():
    global _image, _backgroundColor
    for i in range(7,0,-1):
        for j in range(0,8,1):
            _image[i*8 + j] = _image[(i-1)*8 + j]
            
    # Clear left most pixels
    for i in range (0,8,1):
        _image[i] = _backgroundColor
        
    return;



#===============================
# Copy a row from img_row in img
#  into dst_row in internal image
#=================================
def copyRow(img,img_row,dst_row):
    global _image;
    for i in range(0,8):
        _image[8*dst_row + i] = img[8*img_row + i];

    return;



#==================================
# Copy a column from img_row in img
#  into dst_row in internal image
#===================================
def copyCol(img,img_col,dst_col):
    global _image;
    for i in range(0,8):
        _image[8*i + dst_col] = img[8*i + img_col];

    return;



#=====================================
# Set the value of a pixel in the
#   background using X,Y coordinates 
#=====================================
def setPixel(x,y,color):
    global _image
    if (type(x).__name__ != 'int' or type(y).__name__ != 'int'):
        raise TypeError("X and Y need to be integer values")
    if (x < 0 or x > 7):
        raise ValueError("X must be between 0 and 7")
    if (y < 0 or y > 7):
        raise ValueError("Y must be between 0 and 7")
    if (type(color).__name__ != 'tuple' or len(color) != 3):
        raise TypeError("Illegal color!")

    _image[y*8+x] = color
    return;



#=====================================
# Set the whole image with a 64
#  element array
#=====================================
def setPixels(pixels):
    global _image

    #Validate image as a whole
    if (type(pixels).__name__ != 'list' or len(pixels) != 64):
        raise TypeError("Illegal Picture!")

    #Validate each individual pixel
    for i in range(0,64):
        if (type(pixels[i]).__name__ != 'tuple' or len(pixels[i]) != 3):
            raise TypeError("Illegal Picture!")
        

    _image = pixels
    return;


#================================
# Get a pixel at X,Y in image
#================================
def getPixel(x,y):
    if (type(x).__name__ != 'int' or type(y).__name__ != 'int'):
        raise TypeError("X and Y need to be integer values")
    if (x < 0 or x > 7):
        raise ValueError("X must be between 0 and 7")
    if (y < 0 or y > 7):
        raise ValueError("Y must be between 0 and 7")
    if (type(color).__name__ != 'tuple' or len(color) != 3):
        raise TypeError("Illegal color!")
        raise ValueError("X must be between 0 and 7")
    if (y < 0 or y > 7):
        raise ValueError("Y must be between 0 and 7")
                 
    return _image[y*8 + x];


#====================================
# Get array of all pixels in the screen
#=======================================
def getPixels():
     return _image;





#=================================
# Set the background color of the
#    screen
#=================================
def setBGColor(color):
    global _backgroundColor
    if (type(color).__name__ != 'tuple' or len(color) != 3):
        raise TypeError("Illegal color!")
    _backgroundColor = color
    return;




#===============================
# Generate a full screen of one
#  whole color
#===============================
def singleColor(color):
    global _image
    if (type(color).__name__ != 'tuple' or len(color) != 3):
        raise TypeError("Illegal color!")
    _image = [color] * 64;
    


#===============================
# Put a border around the image
#===============================
def border(color):
    global _image
    if (type(color).__name__ != 'tuple' or len(color) != 3):
        raise TypeError("Illegal color!")

    for i in range(0,8):
        setPixel(i,0,color)
        setPixel(i,7,color)
        setPixel(0,i,color)
        setPixel(7,i,color)

    return;


#=========================
# Clear the screen, ahora
#=========================
def clear():
    singleColor((0,0,0))
    return;
