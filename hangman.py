 # Hangman game
 # click run to start the game
 # the computer selects a word randomly from a wordlist
 # you have 8 guesses to solve the puzzle
 # previously guessed letters don't add to your guess count

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for e in lettersGuessed:
        if e in secretWord:
            secretWord = secretWord.replace(e,'')
            if secretWord is '': 
                return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    newString = ''
    if lettersGuessed == []:
        for char in secretWord:
            newString += '_ '
            
    for e in secretWord:
        if e in lettersGuessed:
            newString += e
        else:
            newString += '_ '
    return newString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = string.ascii_lowercase
    newString = ''
    if lettersGuessed == []:
        return alpha
    
    for l in lettersGuessed:
        alpha = alpha.replace(l,"")
    return alpha
  

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    lettersGuessed = []
    GuessCount = 8
    while GuessCount > 0:
        print 'You have ' + str(GuessCount) + '  guesses left'
        print 'Available letters:' + str(getAvailableLetters(lettersGuessed))
        guess = str(raw_input('Please guess a letter: ')) #accepts a guess
        guessLowerCase = guess.lower() #change guess to lowercase
        lettersGuessed += guessLowerCase #collect guesses in list
    
        if guessLowerCase in lettersGuessed[:-1]:
            print 'Oops! You have already guessed that letter: '+str(getGuessedWord(secretWord,lettersGuessed))
        else:
            if guessLowerCase in secretWord:
                print 'Good guess:' + str(getGuessedWord(secretWord,lettersGuessed))
            else: 
                print 'Oops! That letter is not in my word:' +str(getGuessedWord(secretWord,lettersGuessed))
            GuessCount -= 1
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations you won' 
            break
        if GuessCount == 0:
            print 'Sorry you ran out of guesses. The word was :' +  str(secretWord)
            break
        



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
