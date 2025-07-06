
import requests

# Generate a new (5 letter) word
def generate_word(url = "https://random-word-api.vercel.app/api?words=1&length=5"):
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return str(response.json()[0]) # The response is a list of {x} words

    else:
        raise RuntimeError(f"Failed to fetch word. Status code: {response.status_code}")

# Get and validate input from the user
def get_valid_input(prompt, validate_fn, target, error_message="Invalid input. Please try again."):
    while True:
        user_input = input(prompt)
        if validate_fn(user_input, target):
            return user_input
        else:
            print(error_message)

# Validate the input
def is_valid_word(guess, target):
    return len(guess.strip()) == len(target) and guess.isalpha()

# If hard mode: Check that the guess uses any previously discovered letters
def is_valid_hard_mode_guess(guess, correct_positions):
    for pos, char in correct_positions.items():
        if guess[pos] != char:
            return False, f"Letter '{char}' must be at position {pos + 1}"
    return True, ""

# Check how the guess matches the word
def check_guess(guess, target):
    result = []
    target_chars = list(target)
    guess_chars = list(guess)

    # Check if it's the correct word
    if guess == target:
        return 'Correct'

    # First pass: Is the character in the right position?
    for i in range(len(guess_chars)):
        if guess_chars[i] == target_chars[i]:
            result.append("!") # e.g. green
            target_chars[i] = None # Mark the letter as found
        else:
            result.append(None)

    # Second pass: Is the character in the wrong position?
    for i in range(len(guess_chars)):
        if result[i] is None:
            if guess_chars[i] in target_chars:
                result[i] = "?" # e.g. yellow
                target_chars[target_chars.index(guess_chars[i])] = None # Remove the letter
            else:
                result[i] = "x"
    
    #print(target_chars)
    return result

# Game loop
def new_round(hard_mode = False):
    # Generate a new word
    word = generate_word()
    guesses = 1
    correct_positions = {} # Example: {0: 't', 2: 'a'}

    while(guesses <= 6):

        guess = get_valid_input(f"Guess word ({len(word)} letters): ", is_valid_word, word)
        
        # Check that the guess passes the hard mode
        if hard_mode:
            while True:
                valid, message = is_valid_hard_mode_guess(guess, correct_positions)
                if valid:
                    break
                if not valid:
                    print("Invalid (Hard Mode):", message)
                    guess = get_valid_input(f"Guess word ({len(word)} letters): ", is_valid_word, word)

        # Compare guess with word
        res = check_guess(guess, word)
        
        if res == 'Correct':
            print(f"Congratulations! You guessed the correct word in {guesses} {'guess' if guesses == 1 else 'guesses'}")
            break
                
        elif guesses < 6:
            # Update correct_positions
            for i in range(len(guess)):
                if guess[i] == word[i]:
                    correct_positions[i] = guess[i]

            guesses += 1
            print(f'{res}\nYou have {6+1-guesses} guesses left')

        else:
            print(f'❌ Out of guesses. The correct word was: {word}')
            break

# Generic function to get valid user input
def get_input(valid_responses, query = "Enter input: "):
    while True:
        res = input(f"{query}").strip().lower()
        if res in valid_responses:
            return res
        else:
            print(f"Please enter one of: {', '.join(valid_responses)}")


# Run the game for as long as the player wants
while True:
    
    res = get_input(['y', 'n'], "Play another round? (y/n): ")
    if res == 'n':
        break
    
    else:
        hard_mode = get_input(['y', 'n'], "Enable hard mode? (y/n): ") == 'y'
        
    new_round(hard_mode)