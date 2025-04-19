import random


# Brikti's function to generate and corrupt digit sequence
def generate_corrupted_sequence(level, num_corrupt):
    """
    Generates a random digit sequence and corrupts some digits to simulate a memory glitch.

    Parameters:
        level (int): Determines the length of the original sequence.
        num_corrupt (int): Number of digits to corrupt in the sequence.

    Returns:
        tuple: (original_sequence, corrupted_sequence)
            - original_sequence (list of str): The correct sequence.
            - corrupted_sequence (list of str): The sequence with some digits changed.

    Raises:
        ValueError: If inputs are invalid (e.g. negative level or too many corruptions).
    """
    if level < 0:
        raise ValueError("Level must be non-negative.")
    if num_corrupt < 0:
        raise ValueError("Number of corrupt digits must be non-negative.")

    length = 3 + level  # base length + level scaling
    if num_corrupt > length:
        raise ValueError("Cannot corrupt more digits than exist in the sequence.")

    original_sequence = [str(random.randint(0, 9)) for _ in range(length)]
    corrupted_sequence = original_sequence.copy()

    corrupt_indices = random.sample(range(length), num_corrupt)

    for index in corrupt_indices:
        original_digit = corrupted_sequence[index]
        new_digit = str(random.randint(0, 9))
        while new_digit == original_digit:
            new_digit = str(random.randint(0, 9))
        corrupted_sequence[index] = new_digit

    return original_sequence, corrupted_sequence



# Function will cause an error because it hasn't been initialized
length = 3 + level
sequence = [str(random.randint(0,9))for _ in range(length)]
    return sequence
    
#Rohan Julien Function
def assess_guess(player_input, target_sequence):
    """
    Compares the player's input to the sequence and generates result details.

    Parameters:
        player_input: The input provided by the player int.
        target_sequence: The correct answer to evaluate against int.

    Returns:
        dict: Contains:
            - 'correct': True if entire guess is right.
            - 'feedback': List of per digit match.
            - 'hints': hints where mismatches occurred.
            - 'score': Ratio of correct digits to total.
    """
    if len(player_input) != len(target_sequence):
        raise ValueError("Input and target must be of same length.")


    feedback = [a == b for a, b in zip(player_input, target_sequence)]
    correct_count = sum(feedback)
    hints = [i for i, matched in enumerate(feedback) if not matched]

    return {
        "correct": correct_count == len(target_sequence),
        "feedback": feedback,
        "hints": hints,
        "score": correct_count / len(target_sequence)
    }


# Mock data
target = "1234"  # The correct sequence to guess
guesses = ["1234", "1245", "1334", "1111", "5678"]  # A list of player's guesses

# Iterate through each guess and evaluate using the function
for guess in guesses:
    print(f"Guess: {guess}")
    result = assess_guess(guess, target)
    print(f"Result: {result}")
    print("-" * 30)

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
