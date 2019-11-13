def getGuessedWord(secretWord, lettersGuessed):
    for elements in secretWord:
        if elements not in str(lettersGuessed):
            secretWord=secretWord.replace(elements,'_')
            return secretWord
        
