import random

# List of colors that the computer can choose from.
colorList = ['red', 'orange', 'yellow', 'green',
                'blue', 'indigo', 'violet',]

numberOfColors = 4

# Number of correct colors in the correct place.
corColCorPl = 0

# Number of correct colors in the wrong place.
corColWrongPl = 0

# Generates a list of 4 random colors from colorList with repeats.
answer = random.choices(colorList, k=numberOfColors)
comparisonList = answer[:]
print(answer)
# Empty list to hold the values of user's guesses.
guesses = []

# Welcome message and premise.
print('''
Welcome to MastermindPy! The objective of the game is to guess 4 colors
in the correct order that I have randomly chosen from a list.
Colors can be repeated.''')

print('Here is the list: ')

for color in colorList:
    print(color + ', ', end='')

print("Let's begin!")


# Checks if guesses are equal to answer.
def isMatch(guesses, answer):
    return guesses == answer


# Appends each input of user into guesses list.
for x in range(numberOfColors):
    guess = input('Enter your guess here: ')
    guesses.append(guess.lower())

# Checks for correct colors in the wrong place.


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
