import random

# List of colors that the computer can choose from.
colorList = ['red', 'orange', 'yellow', 'green',
            'blue', 'indigo', 'violet',]
numberOfColors = 4

def makeAnswerList(list, len):
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
    for string in list:
        if list[len(list)-1] == string:
            print(string)
        else:
            print(string + ', ', end='')

def startGuessing(emptyList, len):
    '''Takes the input of the user and appends them to the emptyList
    for len amount of times.
    '''
    for x in range(len):
        guess = input('Enter your guess here: ')
        emptyList.append(guess.lower())

    return None

def congrats(guessCount):
    print('Congratulations! You matched all the colors! You won the game!')
    if guessCount == 1:
        print('It took you 1 guess to figure out the colours!\n')
    else:
        print('It took you ' + guessCount + ' guesses to figure out the colours!\n')

def wantRepeat():
    while True:
        x = input('\nWould you like to play again?(Y/n)\n') or 'y'
        if x.lower() in ['yes', 'y']:
            return True
        elif x.lower() in ['no', 'n']:
            return False
        else:
            print("I don't understand. Please type 'y' or 'n'")

def main():
    answer = makeAnswerList(colorList, numberOfColors)
    print('Here is the list of colors I will choose from: ')
    getList(colorList)
    print("\n\nLet's begin!")
    while True:
        guessCount = 0
        guesses = []
        guessCount += 1
        guesses = []
        # print(answer)
        corColCorPl = 0
        corColWrongPl = 0
        startGuessing(guesses, numberOfColors)
        guessesCopy = copyList(guesses)
        comparisonList = copyList(answer)
        print(f'{guesses} guesses list')
        print(f'{guessesCopy} guess copy list')
        print(f'{answer} answer list')
        print(f'{comparisonList} comparison list')

        # Checks for correct colors in the correct place.
        for colorIndex in range(numberOfColors):
            if guesses[colorIndex] == answer[colorIndex]:
                corColCorPl += 1
                comparisonList.remove(guesses[colorIndex])
                guessesCopy.remove(guesses[colorIndex])
        print(f'{comparisonList} comparison list')
        print(f'{guessesCopy} guesses list')

        # Checks for correct colors in the wrong place.
        for colorIndex in range(len(guessesCopy)):
            if guessesCopy[colorIndex] in comparisonList:
                    corColWrongPl += 1

        print('\nHere are your results for this attempt.')
        print('Correct colors in the correct place: ' + str(corColCorPl))
        print('Correct colors in the wrong place: ' + str(corColWrongPl) + '\n')
        if isMatch(guesses, answer):
            congrats(guessCount)
            print('This is the answer list: ')
            getList(answer)
            break
        else:
            print('Try again.')

    if wantRepeat():
        main()
    else:
        print('\nThanks for playing! Goodbye.')

print('''
Welcome to MastermindPy! The objective of the game is to guess 4 colors
in the correct order that I have randomly chosen from a list of colors.
Colors can be repeated. Each color that you guess must be entered once.
You can type 'help' at any time for a list of commands.
''')

main()
