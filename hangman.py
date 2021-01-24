import random


def hangman(correct_word):
    uniq = set()
    wrong = set()
    hint = "-" * len(correct_word)                                                                                           # hint =["-"] * len(correct_word)
    chances = 8
    while chances > 0:
        print()
        print(hint)                                                                                                       # print("".join(hint))
        guess_letter = input("Input a letter:")
        if guess_letter in wrong:
            print("You already typed this letter")
            continue

        if len(guess_letter) != 1:
            print("You should input a single letter")
            continue

        if guess_letter not in ('abcdefghijklmnopqrstuvwxyz'):
            print("It is not an ASCII lowercase letter")
            continue

        check = correct_word.find(guess_letter)
        if check == -1:
            chances -= 1
            wrong.update(guess_letter)
            print("No such letter in the word")
            continue

        if guess_letter in uniq:
            print("You already typed this letter")
            continue

        else:
            uniq.update(guess_letter)
            for i in range(len(correct_word)):
                if guess_letter == correct_word[i]:
                    hint = hint[:i] + guess_letter + hint[i + 1:]                                                         #hint[i] = guess_letter

        if hint == correct_word:                                                                                            #"".join(hint) == correct_word:
            break

    if hint == correct_word:                                                                                              #"".join(hint) == correct_word:
        print("You guessed the word " + correct_word + "!")
        print("You survived!")
    else:
        print("You are hanged!")


print('H A N G M A N')

names_list = ['python', 'java', 'kotlin', 'javascript']  # give list of words 
correct_word = random.choice(names_list)

while True:
    play_ornot = input('''Type "play" to play the game, "exit" to quit: ''')
    if play_ornot == "play":
        hangman(correct_word)
    elif play_ornot == "exit":
        break
    else:
        print('''Choose either "play" or "exit"''')

