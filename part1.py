# Advent of Code 2023 Day 3 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys
import re

def main(filename):
    with open(filename, 'r') as file:
        schematic = [list(line.strip()) for line in file]

    numbers = {}
    for i in range(len(schematic)):
        line = ''.join(schematic[i])
        for match in re.finditer(r'\d+', line):
            for j in range(match.start(), match.end()):
                numbers[(i, j)] = int(match.group())

    total = 0
    counted = set()

    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit() == False and schematic[i][j] != '.':
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if (ni, nj) in numbers and numbers[(ni, nj)] not in counted:
                            total += numbers[(ni, nj)]
                            counted.add(numbers[(ni, nj)])

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
