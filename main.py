import random

# help function incomplete
colorList = ['red', 'orange', 'yellow', 'green',
            'blue', 'indigo', 'violet',]
numberOfColors = 4

def randList(list, len):
    '''Returns a list of random strings from a list.'''
    return random.choices(list, k=len)

def copyList(list):
    '''Makes a copy of a list for comparison.'''
    return list[:]

def isMatch(guesses, answer):
    '''Checks if two lists are equal.'''
    return guesses == answer

def getList(list):
    '''Prints list in an easy to read format.'''
    print(*list, sep=', ')
    print()

def guessCol(emptyList, len):
    '''Takes the input of the user and appends them to the emptyList
    for len amount of times.
    '''
    for x in range(len):
        guess = input('Enter your guess here: ')
        while guess.lower() not in colorList:
            print('Error, that is not in my color list.')
            guess = input('Enter your guess here: ')
        emptyList.append(guess.lower())

def congrats(guessCount):
    '''Congratulates user.'''
    print('Congratulations! You matched all the colors! You won the game!')
    if guessCount == 1:
        print('It took you 1 guess to figure out the colours!\n')
    else:
        print('It took you ' + str(guessCount) + ' guesses to figure out the colours!\n')

def playAgain():
    '''Asks if the user would like to replay.'''
    while True:
        x = input('\nWould you like to play again?(Y/n)\n') or 'y'
        if x.lower() in ['yes', 'y']:
            return True
        elif x.lower() in ['no', 'n']:
            return False
        else:
            print("I don't understand. Please type 'y' or 'n'")

def main():
    answer = randList(colorList, numberOfColors)
    print("\nLet's begin!")
    guessCount = 0
    while True:
        print('\nHere is the list of colors I will choose from: ')
        getList(colorList)
        guessCount += 1
        guesses = []
        corColCorPl = 0
        corColWrongPl = 0
        guessCol(guesses, numberOfColors)
        print('\nThis is what you guessed: ')
        getList(guesses)
        guessesCopy = copyList(guesses)
        comparisonList = copyList(answer)
        # Checks for correct colors in the correct place.
        for colorIndex in range(numberOfColors):
            if guesses[colorIndex] == answer[colorIndex]:
                corColCorPl += 1
                comparisonList.remove(guesses[colorIndex])
                guessesCopy.remove(guesses[colorIndex])
        comparisonList2 = copyList(comparisonList)

        # Checks for correct colors in the wrong place.
        for colorIndex in range(len(guessesCopy)):
            if guessesCopy[colorIndex] in comparisonList2:
                comparisonList2.remove(guessesCopy[colorIndex])

        corColWrongPl = len(comparisonList) - len(comparisonList2)

        print('Here are your results for this attempt.')
        print('Correct colors in the correct place: ' + str(corColCorPl))
        print('Correct colors in the wrong place: ' + str(corColWrongPl))
        if isMatch(guesses, answer):
            congrats(guessCount)
            print('This is the answer list: ')
            getList(answer)
            break
        else:
            print('Try again.')

    if playAgain():
        main()
    else:
        print('\nThanks for playing! Goodbye.')

print('''Welcome to MastermindPy! The objective of the game is to guess 4 colors
in the correct order that I have randomly chosen from a list of colors.
Colors can be repeated. Each color that you guess must be entered once.
You can type 'help' at any time for a list of commands.
''')

main()
