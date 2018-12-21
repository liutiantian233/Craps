# Craps - A popular dice game

**A popular dice game is Craps.** In this project you will handle the rolling of dice and wagers while a user plays the game. Wagering for craps is complicated; we use a simplified version here.

**The rules** A player rolls two dice. Each die has six faces. These faces contain 1, 2, 3, 4, 5, and 6 spots. After the dice have come to rest, the sum of the spots on the two upward faces is calculated. If the sum is 7 or 11 on the first throw, the player wins (this is called a “Natural win”). If the sum is 2, 3, or 12 on the first throw (called "craps"), the player loses (i.e. the "house" wins). If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, then the sum becomes the player's "point." To win, you must continue rolling the dice until you "make your point." The player loses by rolling a 7 before making the point.

**Learning Objectives**
- Functions
- iteration
- string

**The goal of this project is to play a simplified game of craps.**

-------------------

## Craps Introduction

> **Craps** is a dice game in which the players make wagers on the outcome of the roll, or a series of rolls, of a pair of dice. Players may wager money against each other (playing "street craps") or a bank (playing "casino craps", also known as "table craps", or often just "craps"). Because it requires little equipment, "street craps" can be played in informal settings. While shooting craps, players may use slang terminology to place bets and actions. -- [Wikipedia](https://en.wikipedia.org/wiki/Craps)

### Project Description

* Your program must prompt for an initial player’s bank balance (from which wagers will be subtracted or added). Note that all dollar amounts in this game will be ints.
* Before each game (i.e. before the first roll of the game) prompt the user for a wager. Wagers must be less than or equal to the bank balance. If not, keep asking for a wager until a valid one is entered. (use a while loop).
* One game is played with a sequence of two dice rolls. A game can end after one roll of the two dice (a 7 was rolled) or it can continue with an unlimited number of rolls (use a while loop). Note that the rules are different on the first roll of the game than on subsequent rolls. (use a Boolean to indicate that it is the first roll)
* After you play each game update the player’s bank balance by adding or subtracting the wager depending on whether they won or lost.
* Prompt the user to see if they want to play another game. If “yes”, play another game. (use a while loop).
* If the user is to play another game, prompt the user to see if they wish to add to their balance. If “yes”, then prompt for a value and update the player’s bank balance.
