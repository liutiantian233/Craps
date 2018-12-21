###########################################################
#
#  Computer Project Craps
#
#  Define all the functions
#    display_game_rules():
#    get_bank_balance():
#    add_to_bank_balance(balance):
#    get_wager_amount():
#    is_valid_wager_amount(wager, balance):
#    roll_die():
#    calculate_sum_dice(die1_value, die2_value):
#    first_roll_result(sum_dice):
#    subsequent_roll_result(sum_dice, point_value):
#    continue_to():
#  Define the main function
#    Using all the functions
#      Using two while loops to determine if the game is over
#      Using three if statements to determine if the first game is over
#      Using a while loop to Play the game loop
#      Using three if statements according to the rules of the game
#      Use two if statements to nest
#       Determine the output at the end of the game
#      
###########################################################

from random import randint  # the real Python random

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

def main():
    """
Play with all the functions
No returns
    """
    con = '' # The character used to determine whether it is yes or no
    display_game_rules() # use function
    balance = get_bank_balance() # use function
    wager = get_wager_amount() # use function
    
    while is_valid_wager_amount(wager, balance) == False:
    # If the wager is large the balance, an error is prompted
        print("Error: wager > balance. Try again.")
        wager = get_wager_amount()
        
    while is_valid_wager_amount(wager, balance) == True and \
    con != 'no':
    # The input is legal and no is not entered
    
        die_1 = roll_die()
        die_2 = roll_die()
        print("Die 1:",die_1)
        print("Die 2:",die_2)
        print("Dice sum:",calculate_sum_dice(die_1,die_2))
        sum_dice = calculate_sum_dice(die_1,die_2)
        
        if first_roll_result(sum_dice) == 'win':
        # If win the first time
            print("Natural winner.")
            print("You WIN!")
            balance = balance + wager
            print("Balance:",balance)
            
            if continue_to() == False:
            # If input no
                con = 'no'
                break
            else:
                balance = add_to_bank_balance(balance)
                if balance == 0:
                # If the balance is 0 at this point
                    break
                wager = get_wager_amount()
            
        if first_roll_result(sum_dice) == 'loss':
        # If loss the first time
            print("Craps.")
            print("You lose.")
            balance = balance - wager
            print("Balance:",balance)
            
            if continue_to() == False:
            # If input no
                con = 'no'
                break
            else:
                balance = add_to_bank_balance(balance)
                if balance == 0:
                # If the balance is 0 at this point
                    break
                wager = get_wager_amount()
            
        if first_roll_result(sum_dice) == 'point':
            print("*** Point:",sum_dice)
            point_value = sum_dice
            die_1 = roll_die()
            die_2 = roll_die()
            sum_dice = calculate_sum_dice(die_1,die_2)
            
            while True:
                
            # going to loop after the first one
                if subsequent_roll_result(sum_dice, point_value) == 'neither':
                # If don't meet the criteria, continue the loop
                    print("Die 1:",die_1)
                    print("Die 2:",die_2)
                    print("Dice sum:",calculate_sum_dice(die_1,die_2))
                    die_1 = roll_die()
                    die_2 = roll_die()
                    sum_dice = calculate_sum_dice(die_1,die_2)
                
                if subsequent_roll_result(sum_dice, point_value) == 'loss':
                # If the loop is loss
                    print("Die 1:",die_1)
                    print("Die 2:",die_2)
                    print("Dice sum:",calculate_sum_dice(die_1,die_2))
                    print("You lose.")
                    balance = balance - wager
                    print("Balance:",balance)
                    
                    if continue_to() == False:
                    # If input no
                        con = 'no'
                        break
                    else:
                        balance = add_to_bank_balance(balance)
                        if balance == 0:
                        # If the balance is 0 at this point
                            break
                        wager = get_wager_amount()
                        break
                
                if subsequent_roll_result(sum_dice, point_value) == 'point':
                # If the loop is point
                    print("Die 1:",die_1)
                    print("Die 2:",die_2)
                    print("Dice sum:",calculate_sum_dice(die_1,die_2))
                    print("You matched your Point.")
                    print("You WIN!")
                    balance = balance + wager
                    print("Balance:",balance)
                    
                    if continue_to() == False:
                    # If input no
                        con = 'no'
                        break
                    else:
                        balance = add_to_bank_balance(balance)
                        if balance == 0:
                        # If the balance is 0 at this point
                            break
                        wager = get_wager_amount()
                        break
                    
    if con == 'no' or balance <= 0:
    # These are two cases
    
        if balance <= 0:
        # If the balance is 0 at this point
            print("You don't have sufficient balance to continue.")
            print("Game is over.")
        else:
            print("Game is over.")
        
if __name__ == "__main__":  # just the end
    main()
