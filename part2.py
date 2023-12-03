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
            number = int(match.group())
            for j in range(match.start(), match.end()):
                numbers[(i, j)] = number

    total = 0
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j] == '*':
                adjacent_numbers = set()
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if (ni, nj) in numbers:
                            adjacent_numbers.add(numbers[(ni, nj)])
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers.pop() * adjacent_numbers.pop()

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
