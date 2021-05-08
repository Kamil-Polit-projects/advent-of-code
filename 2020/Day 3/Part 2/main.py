# 2020 | Day 3 | Part 1
# Python version: 3.9.4
# Date: 05.05.2021
# Made by Kamil Polit

with open("data.txt", 'r') as file:
    map = [line.strip() for line in file.readlines()]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1

for slope in slopes:
    treeCount = 0
    row, col = 0, 0
    while row + 1 < len(map):
        row += slope[1]
        col += slope[0]

        space = map[row][col % len(map[row])]
        if space == '#':
            treeCount += 1
    
    total *= treeCount
print(total)
