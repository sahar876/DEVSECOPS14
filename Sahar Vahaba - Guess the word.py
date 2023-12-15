import random
import time

# List of phrases
phrases = [
    "Go Home Now",
    "Maccabi Tel Aviv",
    "Never look back",
    "Nothing is Impossible",
    "You are stupid",
    "What you want",
    "Always be honest",
    "Be the change",
    "Believe you can"
    "Trust the process"
    "Yes you can"
    "Remember to Live"

]


# choose a random phrase from the list
def choose_phrase():
    return random.choice(phrases)


# Function to initialize the game
def initialize_game(phrase):
    return ['_' if char.isalpha() else char for char in phrase]


# Function to display the current state of the phrase
def display_phrase(phrase_state):
    print(' '.join(phrase_state))


# Function to play the game
def play_game():
    phrase = choose_phrase().upper()
    phrase_state = initialize_game(phrase)
    guessed_letters = set()
    score = 0
    start_time = time.time()

    while '_' in phrase_state:
        display_phrase(phrase_state)

        guess = input("Try to guess a letter: ").upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(guess)

            if guess in phrase:
                print("Correct guess!")
                score += 5
                for i in range(len(phrase)):
                    if phrase[i] == guess:
                        phrase_state[i] = guess
            else:
                print("Incorrect guess. Please try again.")
                score -= 1

        else:
            print("Invalid input. Please enter a single letter.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    display_phrase(phrase_state)
    print(f"Well Done! You guessed the phrase in {elapsed_time:.2f} seconds.")
    print(f"Your score is: {score} points")

    if elapsed_time < 30:
        bonus_points = 100
        score += bonus_points
        print(f"Bonus points for completing the game in less than 30 seconds: {bonus_points}")
        print(f"Total score with bonus: {score} points")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    while play_again not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        play_again = input("Do you want to play again? (y/n): ").strip().lower()

    if play_again == 'y':
        print("Let's play again!")
        play_game()  # Call play_game() recursively for a new game
    elif play_again == 'n':
        print("Thank you for playing, GoodBye until next time.")


# Start the game
play_game()
