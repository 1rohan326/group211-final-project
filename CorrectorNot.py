import random

# Brikti's function to generate and corrupt digit sequence
def generate_corrupted_sequence(level, num_corrupt):
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
    print("Welcome to Correct Or Not!")
    print("Try to recall the original digit sequence shown before it's corrupted.")
    print("You have 3 strikes before the game ends.")
    input("Press Enter to begin...")

def main():
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
