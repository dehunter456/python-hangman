import random

# Global variables

hangmen = open("hangmen.txt").read().split(",\n") # Creates a list with the hangman poses for each stage of the game.
words = open("words.txt").read().split("\n") # Creates a list of words from words.txt

word = random.choice(words) # Chooses a word from words.txt
tries = 0
used_words = []
used_letters = []

# Important functions

def get_letter():
  """ 
  Returns a single lowercase letter from the English alphabet, chosen by the user. 
  """
  answer = raw_input(" # Enter a letter: ")
  while not is_valid_answer(answer):
    answer = raw_input(" # Invalid input. Enter an unused letter: ")
  return answer.lower()

def get_word():
  """ Returns a word chosen by the user. """
  answer = raw_input(" # Enter a word: ")
  while not is_valid_answer(answer, True):
    answer = raw_input(" # Invalid input. Enter an unused word: ")
  return answer.lower()

def is_valid_answer(answer, is_word = False):
  """ Returns a boolean, which determines whether a user input is valid or not.
      The validity of an input depends on whether it is a word or letter. A letter is only valid if it is one character long, unused, and in the English alphabet. A word is valid if it is unused.
      
      Parameters:
      # answer -> A string.
      # is_word -> A boolean which decides the conditions used to test the string, answer. Is false by default.
  """
  if is_word:
    return len(answer) != 0 and answer not in used_words
  else:
    is_valid_len = len(answer) == 1
    is_valid_char = ord(answer) >= 97 and ord(answer) < 123
    is_unused = answer not in used_letters
    return is_valid_len and is_valid_char and is_unused

def process_letter(answer):
  """ Adds a user-given letter to the used_letters list and checks whether letter is in the variable, word. """
  global tries
  if answer not in word:
    tries += 1
  used_letters.append(answer)

def process_word(answer):
  """ Adds a user-given word to the used_words list and checks whether the user answer is correct. """
  global tries
  if answer != word:
    tries += 1
  used_words.append(answer)

def has_won():
  """ Checks whether the current game has been won. """
  if word in used_words:
    return True
  for char in word.replace(" ", ""):
    if char not in used_letters:
      return False
  return True

def display_output():
  """ Displays the current hangman sprite, the used_letters and used_words list, the amount of wrong answers left, and the current word that needs to be solved. """
  print "\n" + hangmen[tries] + "\n"
  
  print "Tries: " + str(7 - tries)
  
  print "Used letters: "
  for l in used_letters:
    print l + " ",
  print "\n"
  
  print "Used words: "
  for w in used_words:
    print w + " ",
  print "\n"
  
  print ""
  for c in word:
    if c in used_letters or c == " " or word in used_words:
      print c + " ",
    else:
      print "_ ",
  print "\n"
  
  print "\n----------------------------------------------------"

def game():
  """ The actual game of hangman itself. """
  while not has_won():
    display_output()
    
    word_or_letter = raw_input("Answer a word or letter? Type \"w\" for word or \"l\" for letter: ") 
    
    while word_or_letter != "w" and word_or_letter != "l":
      word_or_letter = raw_input("Invalid input! Answer a word or letter? Type \"w\" for word or \"l\" for letter: ")
    
    if word_or_letter.lower() == "w":
      guess = get_word()
      process_word(guess)
    elif word_or_letter.lower() == "l":
      guess = get_letter()
      process_letter(guess)
  
  display_output()
  if tries >= 7:
    print "Game over! The word was " + word + "."
  else:
    print "You won!"

# Running code.

play_again = "y"
while play_again == "y":
  word = random.choice(words) # Chooses a word from words.txt
  tries = 0
  used_words = []
  used_letters = []
  
  game()
  play_again = raw_input("Play again? Press \"y\" for yes or \"n\" for no: ").lower()
  while play_again != "y" and play_again != "n":
    play_agaih = raw_input("Invalid input! Press \"y\" to play again or \"n\" to not: ").lower()

print "\nBye!"