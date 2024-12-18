import random
from word import words
import string

#randomly selected word is chosen and formatted in secret
def word_maker():
    for i in range (0,len(new_word)):
        print ("_ ", end="")

#set created to store previous guesses
lives = 7
used_letters = set()
new_word = random.choice(words)
hidden_word = word_maker()

#set word list to an underscore to meet the while loop
word_list = "_"

#loop will break either lives reaching 0 or no more '_' present in word_list
while lives > 0 and "_" in word_list:
    
    guess = input("guess your letter. ")

    if guess in new_word:
        
        #alert the user same guess type has been inputted again
        if guess in used_letters:
            print(f"{guess} has alreeady been guessed, try again ")
            
        
        else: 
            used_letters.add(guess)
            #if a letter has been used it is included as it is
            #if letter has not been guessed yet, it is replaced with and underscore
            word_list = [letter if letter in used_letters else "_" for letter in new_word]
            
            #correctly stored letters from guess are shown
            print(f"you have guessed a letter correctly. {word_list}")
            
            
            
            print("the letters that you have used are", used_letters)
    
    
    #implement character limit
    elif len(guess) > 1:
        print(f"{guess} surpasses more than one character, try again.")


    else:   
        
        if guess in used_letters:
            print(f"{guess} has already been guessed, try again")   
        
        else:
            lives = lives -1
            used_letters.add(guess)
            print(f"the word does not contain the letter {guess}, you have {lives} lives remaining.")
            print("the letters that you have used are", used_letters)





if lives == 0:
    print(f"unfortunately you have lost. the word was {new_word}")

else:
    print("well done! you have beat hangman.")