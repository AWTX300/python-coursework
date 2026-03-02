import WordList

# Get a random word from the word list
def get_word():
    word = WordList.get_random_word()
    return word.upper()

# Add spaces between letters
def add_spaces(word):
    return " ".join(word)

# Draw the hangman figure
def draw_hangman(num_wrong):
    hangman_stages = [
        """
           ------
                |
                
                
                
                
        ==========""",
        """
           ------
                |
                0 
                
                
                
        ==========""",
        """
           ------
                |    
                O    
                |    
                
                
        ==========""",
        """
           ------
                |    
                O    
               /|    
                
                
        ==========""",
        """
           ------
                |    
                O    
               /|\\  
                
                
        ==========""",
        """
           ------
                |    
                O    
               /|\\  
               /    
                
        ==========""",
        """
           ------
                |    
                O    
               /|\\  
               / \\  
                
        ==========""",
        """
           ------
                |    
                O    
               /|\\  
               / \\  
                
        =========="""]
#         """
#            ------
#            |    
#           [O]   
#           /|\\  
#           / \\  
#                 
#         ==========""",
#         """
#            ------
#            |    |
#           [O]_  |
#           /|\\  |
#           / \\  |
#                 |
#         ==========""",
#         """
#            ------
#            |    |
#          _[O]_  |
#           /|\\  |
#           / \\  |
#                 |
#         =========="""
#     ]
    print(hangman_stages[num_wrong])

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    draw_hangman(num_wrong)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
        if guess == "" or len(guess) > 1 or not guess.isalpha():
            print("Invalid entry. Please enter one and only one letter.")
        elif guess in guessed_letters:
            print("You already tried that letter.")
        else:
            return guess

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
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

        if guess in word:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"
        else:
            num_wrong += 1

        num_guesses += 1
        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remaining_letters == 0:
        print("Congratulations! You got it in", num_guesses, "guesses.")
    else:
        print("Sorry, you lost.")
        print("The word was:", word)

def main():
    print("Play the H A N G M A N game")
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
