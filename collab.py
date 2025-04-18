import random
 
 # function for updating length of sequence and corrupted sequence
 
 
 # Function will cause an error because it hasn't been initialized
 length = 3 + level
 sequence = [str(random.randint(0,9))for _ in range(length)]
     return sequence

#Conor McHugh Function
def count_strikes(user_input, correct_sequence, current_strikes, max_strikes=3):
    """
    Compares user input to the correct sequence and updates strike count.

    Parameters:
        user_input (str or list): The user's submitted answer.
        correct_sequence (str or list): The correct answer to compare against.
        current_strikes (int): The number of strikes the user already has.
        max_strikes (int): The maximum number of strikes allowed before failure.

    Returns:
        tuple: (updated_strikes, strike_added, game_over)
            - updated_strikes (int): The new strike count.
            - strike_added (bool): True if a strike was added, else False.
            - game_over (bool): True if max strikes reached, else False.
    """
    if user_input != correct_sequence:
        updated_strikes = current_strikes + 1
        strike_added = True
    else:
        updated_strikes = current_strikes
        strike_added = False

    game_over = updated_strikes >= max_strikes
    return updated_strikes, strike_added, game_over