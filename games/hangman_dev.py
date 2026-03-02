# import wordlist
# 
# # Function to get a random word from the word list
# def get_word():
#     word = wordlist.get_random_word()
#     return word.upper()
word = 'avery'
# Function to add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Function to draw the hangman
def draw_hangman(num_wrong):
    hangman_graphics = [
           
        "  _____\n       |   \n      \n      \n      \n      \n",
        "  _____\n       |   \n       o   \n      \n      \n      \n",
        "  _____\n       |   \n       o   \n       |   \n      \n      \n",
        "  _____\n       |   \n       o   \n      \|   \n      \n      \n",
        "  _____\n       |   \n       o   \n      \|/  \n      \n      \n",
        "  _____\n       |   \n       o   \n      \|/  \n       |   \n      \n",
        "  _____\n       |   \n       o   \n      \|/  \n       |   \n",
        "  _____\n       |   \n       o   \n      \|/  \n       |   \n      /  ",
        "  _____\n       |   \n       o   \n      \|/  \n       |   \n      / \ ",

]
    print(hangman_graphics[num_wrong])

# Function to draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    draw_hangman(num_wrong)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))

# Function to get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess
    

# The input/process/draw technique is common in game programming
def play_game():
#     word = get_word()
    
    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 6 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
           temp_display = list(displayed_word)
           for i in range(len(word)):
               if word[i] == guess:
                   temp_display[i]=guess
                   remaining_letters -= 1
            displayed_word = ''.join(temp_display)
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print("Congratulations! You got it in", 
               num_guesses, "guesses.")   
    else:    
        print("Sorry, you lost.")
        print("The word was:", word)

def main():
    print("Play the H A N G M A N game")
    print("_____ \n     | \n     o \n    \|/ \n     | \n    / \ ")     
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
