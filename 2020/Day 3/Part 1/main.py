# 2020 | Day 3 | Part 1
# Python version: 3.9.4
# Date: 05.05.2021
# Made by Kamil Polit

# Gettng data from a file
with open("data.txt", 'r') as file:
    map = [line.strip() for line in file.readlines()]

treeCount = 0
row, col = 0, 0

while row + 1 < len(map):
    row += 1
    col += 3

    space = map[row][col % len(map[row])]
    if space == '#':
        treeCount += 1
print(treeCount)
