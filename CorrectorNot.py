import random

# Brikti's function to generate and corrupt digit sequence
def generate_corrupted_sequence(level, num_corrupt):
    """Generates a random digit sequence and corrupts some digits to simulate a memory glitch.

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
    length = 3 + level
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
  
# Rohan Julien Function
def assess_guess(player_input, target_sequence):
    """ Compares the player's input to the sequence and generates result details.

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
  
# Conor Mchugh Function
def count_strikes(user_input, correct_sequence, current_strikes, max_strikes=3):
    """ Increments the strike count if the user's input is incorrect.

    Args:
        user_input (str): The sequence guessed by the user.
        correct_sequence (str): The correct sequence to match against.
        current_strikes (int): The user's current number of strikes.
        max_strikes (int, optional): The number of strikes allowed before game over. Default is 3.

    Returns:
        tuple:
            - updated_strikes (int): The updated number of strikes.
            - strike_added (bool): Whether a strike was added.
            - game_over (bool): Whether the maximum number of strikes has been reached.
    """
    if user_input != correct_sequence:
        updated_strikes = current_strikes + 1
        strike_added = True
    else:
        updated_strikes = current_strikes
        strike_added = False

    game_over = updated_strikes >= max_strikes
    return updated_strikes, strike_added, game_over

# Donovan Felix Function
def complex_sequence(level):
    """
    Generates a more complex sequence with digit corruption and optional shuffling.

    Arguments:
        level (int): Difficulty level affecting sequence length and corruption complexity.

    Returns:
        tuple:
            - original_sequence (list of str): The original digit sequence.
            - corrupted_sequence (list of str): The corrupted (and possibly shuffled) digit sequence.

    Side Effects:
        Uses randomness for sequence generation and corruption.
    """
    length = 3 + level
    num_corrupt = min(level, length // 2)
    original_sequence = [str(random.randint(0, 9)) for _ in range(length)]
    corrupted_sequence = original_sequence.copy()
    corrupt_indices = random.sample(range(length), num_corrupt)

    for index in corrupt_indices:
        original_digit = corrupted_sequence[index]
        new_digit = str(random.randint(0, 9))
        while new_digit == original_digit:
            new_digit = str(random.randint(0, 9))
        corrupted_sequence[index] = new_digit

    if level >= 5:
        start = random.randint(0, length - 3)
        sub = corrupted_sequence[start:start+3]
        random.shuffle(sub)
        corrupted_sequence[start:start+3] = sub

    return original_sequence, corrupted_sequence

def display_intro():
     """ Displays the game introduction message and waits for the user to start.

    Side Effects:
        Prints to the console and waits for user input.
    """
    print("Welcome to Correct Or Not!")
    print("Try to recall the original digit sequence shown before it's corrupted.")
    print("You have 3 strikes before the game ends.")
    input("Press Enter to begin...")

def main():
     """ Runs the main game loop for Correct or Not.

    Side Effects:
        - Interacts with the user via console input and output.
        - Manages game state including levels and strikes.
    """
    display_intro()
    level = 0
    strikes = 0
    max_strikes = 3

    while True:
        print(f"\nLevel {level + 1}")
        original, corrupted = complex_sequence(level)
        print(f"Memorize this sequence: {''.join(original)}")
        input("Press Enter when ready to see the corrupted version...")
        print("\n" * 50)  # Clear screen effect
        print(f"Corrupted sequence: {''.join(corrupted)}")

        guess = input("Enter your guess for the original sequence: ").strip()
        result = assess_guess(guess, ''.join(original))
        strikes, _, game_over = count_strikes(guess, ''.join(original), strikes)

        print(f"Correct: {result['correct']}")
        print(f"Feedback: {['✓' if match else '✗' for match in result['feedback']]}")
        print(f"Score: {result['score']:.2f}")
        if result['hints']:
            print(f"Hints: Wrong digits at positions {', '.join(map(str, result['hints']))}")

        if result["correct"]:
            print("Great job! Moving to the next level.")
            level += 1
        else:
            print(f"Strike {strikes}/{max_strikes}. Try again.")

        if game_over:
            print("Game Over! You've used all your strikes.")
            print(f"The correct sequence was: {''.join(original)}")
            break

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
