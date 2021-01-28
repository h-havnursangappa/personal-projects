import random
from word_list import word_list

def get_valid_word(word_list):
    word = random.choice(word_list)
    if "_" and " " and "-" not in word:
        return word

def play_hangman():
    word = get_valid_word(word_list)
    # word = "Expect"
    letter_list = list(word.upper())
    missing_letters = []

    for ii in range(4):
        index = random.randint(0, len(letter_list) - 1)
        if letter_list[index] == "_":
            continue
        else:
            missing_letters.append(list(word.upper())[index])
            letter_list[index] = "_"

    print("Guess the word")
    print(" ".join(letter_list))

    mistakes = 0
    while len(missing_letters) != 0:
        if mistakes < 3:
            guess = input(f"You have {3 - mistakes} attempts. Enter the missing letter: ").upper()
            if guess in missing_letters and guess in word.upper():
                idx = [jj for jj, kk in enumerate(list(word.upper())) if kk == guess]
                if len(idx) == 1:
                    letter_list[idx[0]] = guess
                    print(" ".join(letter_list))
                    missing_letters.remove(guess)
                else:
                    for ii in idx:
                        if letter_list[ii] == "_":
                            letter_list[ii] = guess
                            missing_letters.remove(guess)
                            # break
                        else:
                            continue
                    print(" ".join(letter_list))

            elif guess in letter_list:
                print("This letter already exists. Try a new one!")
                # mistakes += 1
            else:
                print("Wrong choice")
                mistakes += 1
        else:
            print(f"You have exhausted all your attempts. The correct word was {word.upper()}")
            break

    if mistakes < 3:
        print("Congrats! You have guessed the word correctly")


if __name__ == '__main__':
    play_hangman()
