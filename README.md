# Walls-Pi
Dungeon crawler game for Raspberry Pi Sense HAT

<br>

## Running the Game:
Run the script "Walls.py" to start the game. You should see the text "Walls by Bryan McClain" scroll across the sense hat screen. Press the center of the control pad to start the game.

<br>

## Level Select Screen:
Use the left and right arrow keys to navigate through all dungeons in the game. Each dungeon is represented by a single ASCII character (0-9, A-Z, then a-z). The current version has 4 dungeons to choose from (though you can [create your own](#create-more-dungeons)). Press the middle button to select a dungeon and start the game.

<br>

## How to Play:
You control the white dot in the center of the screen. Use the left, right, up and down keys to move the player through the dungeon. Press the middle button to bring up the pause screen (see [pause screen](#pause-screen)).

Throughout the dungeon, you will encounter various gameplay elements:
* __Walls__ - You cannot walk through them. Each room has a different colored wall.
* __Secret Wall__ - They look just like a wall, but you can walk through them.
* __Water__ - Represented by random blue colored pixels. You must have boots to walk on water.
* __Lava__ - Represented by random red-orange-yellow colored pixels. You cannot walk on lava.
* __Keys__ - Used to unlock doors. Keys are represented by a single colored dot (red, yellow, green, or blue).
* __Doors__ - You need the key to unlock them. Doors are a 1x2 pixel wall (colored red, yellow, green, or blue respectively)
* __Boots__ - Allow you to walk on water. Represented by a pale blue pixel.
* __Stairs__ - Red stairs take you up a level in the dungeon, and blue stairs take you down a level in the dungeon.
* __Dark Rooms__ - They function just like a normal room, but you cannot see the walls or liquids. Items, doors, stairs, and the exit are still visible.
* __Torch__ - Allows you to see in a dark room. Represented by an orange pixel.
* __Energy__ - You must collect all energies to unlock the exit. Represented by a rainbow pixel.
* __Exit Door__ - Represented by a a rainbow colored door. Once you collect all energies in the dungeon, enter this door to win.

You win by going through the exit door. You should see a pixel art of a green hill and sky, along with a message that scrolls "You Win!" The game will then restart to the title screen so you can play another dungeon.

<br>

# Pause Screen:
| . | . | . | . | . | . | . | . |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| . | R | R | R | R | R | R | . |
| . | Y | Y | Y | Y | Y | Y | . |
| . | G | G | G | G | G | G | . |
| . | B | B | B | B | B | B | . |
| . | . | . | . | . | . | . | . |
| . | O | O | . | . | T | T | . |
| . | . | . | . | . | . | . | . |

* . = Empty Pixel
* R = Red keys Owned (0 to 6+)
* Y = Yellow Keys Owned (0 to 6+)
* G = Green Keys Owned (0 to 6+)
* B = Blue Keys Owned (0 to 6+)
* O = Colored in if you own the boots
* T = Colored in if you own the torch

Press the center button to exit the pause screen.

<br>

## Create More Dungeons:
Use the [Walls-Pi-Editor](https://github.com/ComprosoftCEO/Walls-Pi-Editor) to design your own dungeons for the game. Click on "File" -> "Export to Python" to generate the code needed to import a dungeon into the game. Copy and paste the code into Maps/PreBuilt.py (be sure to rename your dungeon), then add the dungeon to the "allLevels" variable at the bottom of the code file. Restart the game, and your dungeon will be ready to play!
