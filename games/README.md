🎮 Games
Command-line games built with Python, demonstrating functions, loops, randomization, input validation, and iterative development.

🪓 Hangman — Three Versions
One of the most instructive things about this folder is that Hangman went through three development stages, which you can trace through the files:
hangman_dev.py — Early Development Version
The first working prototype. The target word is hardcoded ('avery') to make testing easier without needing a word list module. Shows how developers isolate and test logic before wiring up external dependencies.

Concepts: Functions, string indexing, loops, basic input handling
Run: python hangman_dev.py


hangman_text.py — Text Version with Word List
The first complete version — connects to a wordlist module for random word selection, adds duplicate guess prevention, and cleans up the game loop. No graphics yet.

Concepts: Modular imports, string methods, while loops, function decomposition
Run: python hangman_text.py (requires wordlist.py in same directory)


hangman_graphic.py — Final Version with ASCII Art ⭐
The polished version. Adds a progressive ASCII hangman figure that builds with each wrong guess (7 stages). Also improves input validation to reject non-alphabetic characters.

Concepts: Multi-line strings, indexed ASCII art stages, input sanitization, if __name__ == "__main__" pattern
Run: python hangman_graphic.py (requires WordList.py in same directory)

Example output:
   ------
        |
        O
       /|\
       / \

Word: P _ T H _ N   Guesses: 7   Wrong: 4   Tried: A E I O

⚓ battleship.py — Battleship
A 5×5 grid Battleship game where ships are placed randomly at game start. The player enters coordinates (e.g., A3) to fire, and the board updates with hits (H) and misses (M) after each turn.

Concepts: 2D lists (grid), random placement, coordinate parsing, recursion, ord() for character-to-index conversion
Run: python battleship.py

Example board:
  1 2 3 4 5
A
B   H
C M
D
E

🃏 deck_of_cards.py — Deck of Cards
Builds a complete 52-card deck using a list comprehension with Unicode suit symbols (♥ ♦ ♠ ♣), shuffles it randomly, and deals (pops) the top card.

Concepts: List comprehensions, random.shuffle(), list.pop(), Unicode characters, join()
Run: python deck_of_cards.py

Sample output:
['2♥', '2♦', '2♠', '2♣', '3♥', ...]   ← full deck
['7♠', 'Q♥', 'A♦', ...]               ← shuffled
K♣                                     ← dealt card

💡 Key Concepts Across All Games

Modular design with clearly separated functions (get_word, draw_screen, play_game, main)
Input validation loops that reject bad input without crashing
The if __name__ == "__main__" pattern for reusable modules
Iterative development — Hangman shows how software improves across versions
