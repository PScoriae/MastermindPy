import random


colorList = ['red', 'orange', 'yellow', 'green',
            'blue', 'indigo', 'violet',]
numberOfColors = 4

def getList(list):
    '''Prints list in an easy to read format.'''
    print(*list, sep=', ')
    print()

def guessCol(emptyList, len):
    '''Takes the input of the user and appends them to the emptyList
    for len amount of times.
    '''
    for x in range(len):
        guess = input('Enter your guess here: ').strip()
        if guess == 'exit':
            return exit
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

def goodbye():
    '''Prints a goodbye message for the user.'''
    print('Thanks for playing! Goodbye.')

def playAgain():
    '''Asks if the user would like to replay.'''
    while True:
        x = input('\nWould you like to play again?(Y/n)\n').strip() or 'y'
        if x.lower() in ['yes', 'y']:
            return True
        elif x.lower() in ['no', 'n', 'exit']:
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'")

def main():
    answer = random.choices(colorList, k=numberOfColors)
    print("\nLet's begin!")
    guessCount = 0
    while True:
        print('\nHere is the list of colors I will choose from: ')
        getList(colorList)
        guesses, corColCorPl, corColWrongPl = [], 0, 0
        if guessCol(guesses, numberOfColors) == exit:
            goodbye()
            break
        guessCount += 1
        print('\nThis is what you guessed: ')
        getList(guesses)
        guessesCopy, comparisonList = guesses[:], answer[:]
        # Checks for correct colors in the correct place.
        for colorIndex in range(numberOfColors):
            if guesses[colorIndex] == answer[colorIndex]:
                corColCorPl += 1
                comparisonList.remove(guesses[colorIndex])
                guessesCopy.remove(guesses[colorIndex])
        comparisonList2 = comparisonList[:]

        # Checks for correct colors in the wrong place.
        for colorIndex in range(len(guessesCopy)):
            if guessesCopy[colorIndex] in comparisonList2:
                comparisonList2.remove(guessesCopy[colorIndex])
        corColWrongPl = len(comparisonList) - len(comparisonList2)

        print('Here are your results for this attempt.')
        print('Correct colors in the correct place: ' + str(corColCorPl))
        print('Correct colors in the wrong place: ' + str(corColWrongPl))
        if guesses == answer:
            congrats(guessCount)
            print('This is the answer list: ')
            getList(answer)
            if playAgain():
                main()
            else:
                goodbye()
                break
        else:
            print('Try again.')

print('''Welcome to MastermindPy! The objective of the game is to guess 4 colors
in the correct order that I have randomly chosen from a list of colors.
Colors can be repeated. Each color that you guess must be entered once.
You can type 'exit' at any time to leave the game.
''')

main()
