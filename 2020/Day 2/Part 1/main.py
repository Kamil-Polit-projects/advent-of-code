# 2020 | Day 2 | Part 1
# Python version: 3.9.4
# Date: 05.05.2021
# Made by Kamil Polit
# Question: How many passwords are valid according to their policies?


# Gettng data from a file
with open("data.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')

# Variables for elements
minimumNumberOfLetters = 0
maximumNumberOfLetters = 0
letter = ''
string = ""
count = 0

# Other variables
placeOfTheCursor = 0
numberOfCorrectLetters = 0
tmp = ''

# Main loop
for index, element in enumerate(data):
    # Reset variables
    placeOfTheCursor = 0
    numberOfCorrectLetters = 0
    minimumNumberOfLetters = 0
    maximumNumberOfLetters = 0
    letter = ''
    string = ""
    tmp = ''

    # Minimal number of letter
    for char in element:
        if char == '-':
            minimumNumberOfLetters = int(tmp)
            break
        else:
            tmp += char
            placeOfTheCursor += 1
    tmp = ''

    
    # Maximal number of letter
    for char in element[placeOfTheCursor+1:]:
        if char == ' ':
            maximumNumberOfLetters = int(tmp)
            break
        else:
            tmp += char
            placeOfTheCursor += 1
    tmp = ''

    # Letter
    for char in element[placeOfTheCursor+1:]:
        if char == ':':
            letter = tmp
            break
        tmp = char
    tmp = ''

    # Main loop
    for char in element[placeOfTheCursor+5:]:
        if char == letter:
            numberOfCorrectLetters += 1
    
    if numberOfCorrectLetters >= minimumNumberOfLetters and numberOfCorrectLetters <= maximumNumberOfLetters:
        print('Index:', index, 'Element:', element)
        count += 1

print('Result:', count)