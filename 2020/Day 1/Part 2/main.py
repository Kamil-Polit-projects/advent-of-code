# 2020 | Day 1 | Part 2
# Python version: 3.9.4
# Date: 05.05.2021
# Made by Kamil Polit


# Getting data from a file
with open("data.txt", 'r') as f:
    data = f.read()
    data = data.split()

# Main loop
for element1 in data:
    for element2 in data:
        for element3 in data:
            # Checking whether the sum of the elements is equal to 2020
            if int(element1) + int(element2) + int(element3) == 2020:
                # Pressing the result
                print(int(element1) * int(element2) * int(element3))
                exit(0)
