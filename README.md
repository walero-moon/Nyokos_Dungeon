This is a text based game made on Python. Originally a school project, but I ended up writing a tiny library (1 file) that deals with dynamic creation of text in the middle of ASCII characters and deals with strings, and that is the main purpose I am sharing this project. 

Please note that this was done in the early stages of my programming journey. The code is messy and needlessly long.

If you do not wish to play or know about the game, and only wish to look at the dynamic ASCII aspects, please head to the **What the tiny "library" currently has** section.

# Nyoko's Dungeon
![Nyoko's title screen](https://i.imgur.com/PnbVu68.png)

In this game you have multiple different levels. On each level you'll be faced with a different amount of monsters, each of which will have their own levels. There are 4 "stats" to the player of this game, all of which increase as you progress through the levels:
#### Game stats
* AP, which stands for attack power and determines how much damage you deal.
* HP, which is your health
  > Monsters also have AP and HP, but do not have critical damage.
* Crit chance, the chance you have of dealing critical damage to an enemy (on a critical hit you deal double your AP as damage).
* Gold, which can be used in the shop to buy healing potions, more damage, and more crit chance.

#### Player actions
* [A]ttack, prompts you to choose a monster to attack and deals your current AP as damage to the monster.
> When you attack, the monster counter attacks, and you take damage equal to its AP.
* [B]lock, blocks a random monster and only takes 30% damage of its AP. You counter attack with 50% of your AP.
* [S]hop, takes you to the shop where you can spend gold buy healing potions, damage items and crit chance items.
> You get gold as you kill enemies and progress through the levels. Items in the shop restock after every round.

## What the tiny "library" currently has
The library referenced throughout this project is the "text_utils.py" file. It has most of the functions used for making the text and the ASCII in the game.

**text_utils.clear_console**
> Clearing the console. This detects the Operating System the user is running the code and clears the console (currently only supports Windows and Linux)

**text_utils.health_bar**
> Health bar creation. This function allows the user to change the characters and other aspects of the health_bar.
> 
> ![Example of health bar function in use](https://i.imgur.com/X2ehsX7.png)

**text_utils.get_str_length**
> Longest string's length. This returns the longest string's length in a list of strings

**text_utils.scrollify**
> This function takes a list of strings and put them inside a pretty scroll. Default justification is centering ('^').
> 
> ![Example of scrollify](https://i.imgur.com/Km5BaFz.png)

**text_utils.nyoko_scroll**
> Nyoko's Scroll. Same as scrollify but with Nyoko on top.
> 
> ![Example of nyoko_scroll in use](https://i.imgur.com/uQN7tJA.png)

**text_utils.blockify**
> Similar to scrollify, except that it looks different.
> 
> ![Example of blockify](https://i.imgur.com/SbSiwhN.png)

**text_utils.longest_line_len**
> Returns the length of the longest line in a string

**text_utils.centerfy**
> This function takes a list of strings and centers them relative to each other. It is used throughout the entire game.
> 
> ![Example of centerfy 1](https://i.imgur.com/bKO78Of.png)

**text_utils.nyoko_talks**
> This function takes a list of string and returns a string with Nyoko and the strings inside a bubble
> 
> ![Example of nyoko_talks](https://i.imgur.com/t7cpkU4.png)

**text_utils.side_by_side**
> This function takes multiple strings and puts them side by side in a single string. Used when putting the ASCII art of the enemies side by side, as an example.
> 
> ![Example of side_by_side](https://i.imgur.com/dCAmURo.png)

## Licensing
This code is licensed under the **GNU General Public License v3.0**. You may modify and distribute this code but it must be kept under the same license.
For more information check the **![LICENSE](LICENSE)** file.
