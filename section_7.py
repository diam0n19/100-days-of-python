import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def hangman():
    word_list = ["baboon","ape","donkey","tricia"]
    chosen = random.choice(word_list)
    print(chosen)
    lives = 6
    display = []
    endgame = False
    for _ in range(len(chosen)):
        display += "_"
    while not endgame:
        guess = input("Guess a Letter: ").lower()

        for i in range(len(chosen)):
            letter = chosen[i]
            if letter == guess:
                display[i] = letter

        if guess not in chosen:
            lives -= 1
            if lives == 0:
                endgame = True
                print("You Lost")


    
        print (f"{' '.join(display)}")

        if "_" not in display:
            endgame = True
            print ("You Win!")
    
        print(stages[lives])


hangman()


