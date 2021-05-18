import random
import string
from words import words

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()
  

def hangman():

    word=get_valid_word(words)
    alphabet=set(string.ascii_uppercase)
    word_letters=set(word) #letters in the word
    used_letters=set()     #letters guessed by the user
    lives=10
    
    while len(word_letters)>0 and lives>0:

       user_letter=input("Guess a letter: ").upper()
       lives=lives-1
       

       if user_letter in alphabet-used_letters:  #letter is valid and has not been used yet
           used_letters.add(user_letter)
           if user_letter in word:               #letter is present in the word
              word_letters.remove(user_letter)

       elif user_letter in used_letters:
           print("Sorry! You have already used it")

       else:
           print("Invalid")

       print()
       print("Letters you have already guessed: ",' '.join(used_letters))  #' '.join(['a','b','c']) ---> 'a b c'
       current_word=[letter if letter in used_letters else '-' for letter in word]
       print("Current word: ",' '.join(current_word))
       print(f"You have {lives} lives left")
       print()
           
    if len(word_letters)==0:
       print("Congrats! Your guess is right. The word is "+word)

    else:
       print("You Lost! The correct word is "+word)

print("Welcome to Hangman..")
print("You get 8 lives to guess the right word")
hangman()
