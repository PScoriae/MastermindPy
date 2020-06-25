import random

# List of colors that the computer can choose from.
colorList = ['red', 'orange', 'yellow', 'green',
                'blue', 'indigo', 'violet',]

def makeAnswerList(list, len):
    '''Returns a list of random strings from a list. Uses random.choices.
    len is the length of the new list.
    '''
    return random.choices(list, k=len)

def makeComparisonList(list):
    '''Makes a copy of a list for future comparison.'''
    return list[:]

def isMatch(guesses, answer):
    '''Checks if guesses list is equal to answer list.'''
    return guesses == answer

def getList(list):
    '''Prints list in an easy to read format.'''
    for string in list:
        if list[-1] == string:
            print(string)
        else:
            print(string + ', ', end='')


# Welcome message and premise.
print('''
Welcome to MastermindPy! The objective of the game is to guess 4 colors
in the correct order that I have randomly chosen from a list of colors.
Colors can be repeated. Each color that you guess must be entered once.
You can type 'help' at any time for a list of commands.
''')

print('Here is the list: ')

getList(colorList)

print("\n\nLet's begin!")

while True:
    # Number of colors to be chosen for answer list.
    numberOfColors = 4

    # Number of correct colors in the correct place.
    corColCorPl = 0

    # Number of correct colors in the wrong place.
    corColWrongPl = 0

    # Empty list to hold the values of user's guesses.
    guesses = []

    answer = makeAnswerList(colorList)
    print(answer)
    comparisonList = makeComparisonList(answer)
    startGuessing(guesses, numberOfColors)


def startGuessing(emptyList, len):
    '''Takes the input of the user and appends them to the emptyList
    for len amount of times.
    '''
    for x in range(len):
        guess = input('Enter your guess here: ')
        emptyList.append(guess.lower())

# Checks for correct colors in the correct place.
for colorIndex in range(numberOfColors):
    if guesses[colorIndex] == answer[colorIndex]:
        corColCorPl += 1
        comparisonList.remove(guesses[colorIndex])

# Checks for correct colors in the wrong place.
for colorIndex in range(numberOfColors):
    if guesses[colorIndex] in comparisonList:
            corColWrongPl += 1

print('Here are your results for this attempt.')
print('Correct colors in the correct place: ' + str(corColCorPl))
print('Correct colors in the wrong place: ' + str(corColWrongPl))
