from words import word_list
import random

def get_word():
    random.shuffle(word_list)
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_c = "_"* len(word)             #initialising word_c to length
    guessed = False
    g_letters = []
    g_words = []
    tries = 6
    print("Let's Try not to hang the man!")
    print(word_c)
    print("\n")

    #loop for guessing
    while not guessed and tries >0:
        guess = input('Guess a letter or a word! ').upper()

        #letter is guessed
        if len(guess)==1 and guess.isalpha():
            if guess in g_letters:
                print("you have already guessed letter'"+guess+"'\n")
            elif guess not in word:
                print(guess,"is not in the word, try again!")
                tries-=1
                print(disp_hm(tries))
                g_letters.append(guess)
            else:
                print("your guess is correct!")
                g_letters.append(guess)
                word_al= list(word_c)
                indices = [i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_al[index]= guess
                word_c = "".join(word_al)
                print(word_c)
                if tries<6:
                    print(disp_hm(tries))
                print("\n")
                if "_" not in word_c:
                    guessed = True

        #word is guessed
        elif len(guess)==len(word) and guess.isalpha():
            if guess in g_words:
                print("you have already guessed word'"+guess+"'\n")
            elif guess not in word:
                print(guess,"is not the word, try again!")
                tries-=1
                print(disp_hm(tries))
                g_words.append(guess)
            else:
                print("your guess is correct!")
                g_words.append(guess)
                word_c=word
                print(word_c)
                if tries<6:
                    print(disp_hm(tries))
                guessed=True

        #wrong word or value not alphabetic
        else:
            print("not a valid guess..")
            print(word_c)
            print("\n")
        #end of loop

    #winner's/loser's screen
    if guessed==True: print("Congractulations! You Saved the Man")
    else:
        print("you failed to guess the word! Try again later.")
        print("the word was :",word)


#hangman visual
def disp_hm(tries):
    stages = [ """

                -------------
                |          |
                |          O
                |        \\\|//
                |          |
                |        //|\\
                -
               """
                ,
               """
                -------------
                |          |
                |          O
                |        \\\|//
                |          |
                |        //|
                -
               """
               ,
               """
                -------------
                |          |
                |          O
                |        \\\|//
                |          |
                |
                -
               """
                ,
               """
                -------------
                |          |
                |          O
                |        \\\|//
                |
                |
                -
               """
                ,
               """
                -------------
                |          |
                |          O
                |        \\\|
                |
                |
                -
               """
                ,
               """
                -------------
                |          |
                |          O
                |
                |
                |
                -
               """
              ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N):").upper()=='Y':
        word = get_word();
        play(word)


if __name__ == "__main__":
    main()
