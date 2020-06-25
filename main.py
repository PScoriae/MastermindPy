import random

# List of colors that the computer can choose from.
colorList = ['red', 'orange', 'yellow', 'green',
                'blue', 'indigo', 'violet',]

# Generates a list of 4 random colors from colorList with repeats.
answer = [random.choices(colorList, k=4)]
