# hangman
# in this application i have a list of predifined words. each time user has to guess a word considering its length and shown like password.
# user has to choose letter by letter. cant have duplicate letter. we counte the steps.

import random
from pip._vendor.html5lib._ihatexml import letter

def get_word():
    words = ['choose','list','iran','behboudi','italia','instagram','facebook','war','likeit','motivation','crazy','dirty','love','hate','trump','who','mom','water','torta','kill','no','fardin']
    return random.choice(words).upper()

word = get_word()
word_letter = list(word)

def check(word,guesses,guess):
    status = ''
    match = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "*"
 
        if letter == guess:
            match += 1
    if match > 1 :
        print 'you have gussed ', match, 'letter truly "'+ guess +'"'+'\'s'
    elif match == 1:
        print 'you have gussed 1 letter truly', guess 
    else:
        print 'Entered input does not exist in the word '
    return status

def main():
    #print word_letter
    num_of_guess = 0
    guesses = []
    guessed = False
    test = '*' * len(word_letter)
    print 'welcome!!! the word is \"', test , '\" and it has ', len(word_letter),' you should guess it now :)' 
    while not guessed:
        guess = raw_input('please input your letter or word  ')
        guess = guess.upper()
        if  len(guess) == 1 or  len(guess) == len(word_letter):
            num_of_guess += 1 
            if guess in guesses:
                print 'you already guessed ',guess
            elif len(guess) == len(word):
                guesses.append(guess)
                if guess == word :
                    guessed = True 
                 
                else:
                    print 'sorry not currect'
            elif len(guess) == 1: 
                guesses.append(guess)
                result = check(word, guesses, guess)
                if '*' not in result :
                    guessed = True 
                else:
                    print result
        else:
            print 'you should enter only 1 letter or a word with length? ', len(word_letter),' please enter again    ' 
    print 'you found the the word: ', word ,':) in ',num_of_guess,'steps'  
main()
