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

* The Useful function
> **display_game_rules()**
>
> **get_bank_balance()** Prompt the player for an initial bank balance (from which wagering will be added or subtracted). The player-entered bank balance is returned as an int.
>
> **add_to_bank_balance(balance)** Prompts the player for an amount to add to the balance. The balance is returned as an int.
>
> **get_wager_amount()** Prompts the player for a wager on a particular roll. The wager is returned as an int.
>
> **is_valid_wager_amount(wager, balance)** Checks that the wager is less than or equal to the balance; returns True if it is; False otherwise.
>
> **roll_die()** Rolls one die. This function should randomly generate a value between 1 and 6 inclusively and returns that value as an int. Use the randint() function called as randint(1,6) for this project. We provide the import at the top of the file.
>
> **calculate_sum_dice(die1_value, die2_value)** Sums the values of the two die and returns the sum as an int.
>
> **first_roll_result(sum_dice)** The function determines the result on the first roll of the pair of dice. A string is returned. You are required to use at least one Boolean operator “or” or “and” in this function.
>>1. If the sum is 7 or 11 on the roll, the player wins and "win" is returned.
>>2. If the sum is 2, 3, or 12 on the first throw (called "craps"), the player loses (the "house" wins) and "loss" is returned.
>>3. If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, then the sum becomes the player's "point" and "point" is returned.
>
> **subsequent_roll_result(sum_dice, point_value)** The function determines the result on the subsequent rolls of the pair of dice. A string is returned.
>>1. If **sum_dice** is the **point_value**, then “point” is returned.
>>2. If **sum_dice** is 7, then “loss” is returned.
>>3. If sum_dice is 7, then “loss” is returned.
>
> **main()** Takes no input. Returns nothing. Call the functions from here. That, the game is played in this function.

## The All Function
```python
@TianTian
def display_game_rules():
    """
Output the rules of the game
    """
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

def get_bank_balance():
    """
Prompt for the initial balance
Returns: The number of balance in value (int)
    """
    balance = input('Enter an initial bank balance (dollars): ')
    balance = int(balance)
    return balance

def add_to_bank_balance(balance):
    """
Determine if the player wants to increase the balance
Prompt for the balance to addition
    If the player needs to increase the balance (boolean)
        balance: Players have balance, each game will change (int)
        add: The player needs to increase the balance (int)
Returns: The number of balance in value (int)
    """
    add = input('Do you want to add to your balance? ')
    if add == 'yes':
        balance_add = input('Enter how many dollars to add to your balance: ')
        balance_add = int(balance_add)
        balance += balance_add
        print("Balance:",balance)
    return balance

def get_wager_amount():
    """
Prompt for the wager that players want to use
Returns: The number of wager in value (int)
    """
    wager = input('Enter a wager (dollars): ')
    wager = int(wager)
    return wager

def is_valid_wager_amount(wager, balance):
    """
To determine whether the balance is less than or equal to the wager
    If the wager is less than or equal to the balance
        Returns true
    Otherwise,
        Returns false
Returns: The boolean value (boolean)
    """
    if wager <= balance:
        return True
        
    else:
        return False

def roll_die():
    """
Random scrolling to get the num of the dice
    Random values
Returns: The number of num in value (int)
    """
    num = randint(0,0)
    return num

def calculate_sum_dice(die1_value, die2_value):
    """
Add up the num of the first two dice
    die1_value: The first random value
    die2_value: The second random value
Returns: The number of sum in value (int)
    """
    sum_dice = int(die1_value) + int(die2_value)
    return sum_dice

def first_roll_result(sum_dice):
    """
Compare the total number of first dice
    If the sum is 7 or 11
        Return to win
    If the sum is 2 or 3
        Return loss
    Otherwise,
        Return to the point
Returns: The boolean value (boolean)
    """
    if sum_dice == 7 or sum_dice == 11:
        return 'win'
        
    elif sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        return 'loss'
        
    else:
        return 'point'

def subsequent_roll_result(sum_dice, point_value):
    """
rotate again and again to compare the total number of dice
    If the sum is equal to the first value
        Return to the point
    If the sum is equal to 7
        Return loss
    Otherwise,
        Return to neither
Returns: The boolean value (boolean)
    """
    if sum_dice == point_value:
        return 'point'
        
    elif sum_dice == 7:
        return 'loss'
        
    else:
        return 'neither'
    
def continue_to():
    """
Determine if the game continues
    The input character
        If the character is yes
            Returns true
        If the character is no
            Returns false
Returns: The boolean value (boolean)
    """
    to = input('Do you want to continue? ')
    
    if to == 'yes':
        return True
        
    if to == 'no':
        return False
```

## Feedback and suggestions
- E-mail：<liutia20@msu.edu>

---------
Thanks for reading this help document
