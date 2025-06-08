
import requests

# URL of the API call
# Call to generate (list of) words of a specified length
url = "https://random-word-api.vercel.app/api?words=1&length=5"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    word = str(response.json()[0]) # The response is a list of {x} words
    print(f"Word fetched: {word}")

else:
    print(f"Failed to fetch word. Status code: {response.status_code}")

# Get and validate input from the user
def get_valid_input(prompt, validate_fn, error_message="Invalid input. Please try again."):
    while True:
        user_input = input(prompt)
        if validate_fn(user_input):
            return user_input
        else:
            print(error_message)

# Validate the input
def is_valid_word(w):
    return len(w.strip()) == len(word)

# Get guess from user
guess = get_valid_input(f"Guess word ({len(word)} letters): ", is_valid_word)

'''
Compare the guess with the word according to the following rules:
-> ! If the letter is in the right place
-> ? If the letter is in the wrong place
-> X If the letter is not found
'''

# Check how the guess matches the word
def check_guess(guess, target):
    result = []
    target_chars = list(target)
    guess_chars = list(guess)

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
    
    print(target_chars)
    return result

print(check_guess(guess, word))