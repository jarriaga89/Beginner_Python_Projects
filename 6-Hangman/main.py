print("Welcome to Josh's hangman! Building this thing was fun!")
print("A random word will be chosen. Your job is to guess it before your stickman runs out of luck.")
hangman_status = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel", "computer", "skyscrapper", "battleship", "serendipity", "washington", "television", "artifact", "tsunami", "elegance", "antagonist", "mesmerizing", "fireworks", "xenomorph"]
import random
from replit import clear
chosen_word = list(random.choice(word_list))
wrongletters_used = []

empty_spaces = "_"
for count_spaces in range(1, (len(chosen_word))):
    empty_spaces += "_"
word_guess_status = list(empty_spaces)
print("".join(word_guess_status))

game_state = "Ongoing"
lives_left = 7 
win = False
hangman_position_check = (0)

def askguess():
    global guess
    print(hangman_status[hangman_position_check])
    guess = input("Try to guess a letter in the word. ").lower()
    clear()
    validateinput()

def lose_life():
    clear()
    global word_guess_status
    global hangman_position_check
    hangman_position_check += 1
    print("".join(word_guess_status))
    global lives_left
    lives_left -= 1 #If you fail to guess, you lose a life.
    global wrongletters_used
    wrongletters_used.append(guess)
    wrongused = ", ".join(wrongletters_used)
    print(f"The following letters are not in the word: {wrongused}")
        

def validateinput():
    global wrongletters_used
    valid_counter = 0
    letter_position_check = (- 1)
    for current_check in chosen_word:
        letter_position_check += 1 
        if guess in current_check:
            word_guess_status[letter_position_check] = guess
            valid_counter += 1
    print("".join(word_guess_status))
    print(f"The following letters are not in the word: {wrongletters_used}")
    if valid_counter == 0:
        lose_life()

while lives_left > 0 and win == False:
    if "".join(word_guess_status) == "".join(chosen_word):
        win = True
        print("You win!")
    elif "".join(word_guess_status) != "".join(chosen_word) and lives_left > 0: 
        askguess()
    if lives_left == 0:
        winword = "".join(chosen_word)
        print(f'You lose. The word was "{winword}".')