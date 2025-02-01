import random

stages = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]


word_list=["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=""
num=len(chosen_word)
for i in range(num):
    placeholder+="_"
print(placeholder)
correct_letters=[]
game_over=False
lives=6
while not game_over:
    guess=input("Guess a letter:").lower()
    display=""

    for char in chosen_word:
        if char==guess:
            display+=char
            correct_letters.append(char)
        elif char in correct_letters:
            display+=char
        else:
            display+="_"

    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You loose")
    
    if "_" not in display:
        game_over=True
        print("You Win")

    print(stages[lives])