# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# display=[]
# word_length = len(chosen_word)
# for _ in range(chosen_word):
#   display+='_'


# guess = input("Guess a letter: ").lower()
  
# for position in range(word_length):
#   letter = chosen_word[position]
#     #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#   if letter == guess:
#     display[position] = letter
  
# # for x in chosen_word:
# #   if x== guess:
# #     print("Right")
# #   else:
# #     print("Wrong")
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# print(display)
#Step 2
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


import random
from hungman_names import word_list
from drawings import stages,logo
# from replit import clear

chosen_word = random.choice(word_list)

print(logo)

print(f'Pssst, the solution is {chosen_word}.')


display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

lives = 6
true = True
while true:
    guess = input("Guess a letter: ").lower()
    # lives-=1
    # clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives-=1
        print(f"\nYou guessed {guess}, That's not in the word.")
        if lives == 0:
            print("Out of chances")
            true = False
        
    if '_' not in display:
        print("You Win!")
        true = False

    print(stages[lives])