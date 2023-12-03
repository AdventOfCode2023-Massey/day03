# Advent of Code 2023 Day 3 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys
import re

def main(filename):
    with open(filename, 'r') as file:
        schematic = [list(line.strip()) for line in file]

    symbol_adjacent = set()
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit() == False and schematic[i][j] != '.':
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(schematic) and 0 <= nj < len(schematic[i]):
                            symbol_adjacent.add((ni, nj))

    total = 0
    for i in range(len(schematic)):
        line = ''.join(schematic[i])
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            for j in range(match.start(), match.end()):
                if (i, j) in symbol_adjacent:
                    total += number
                    break

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
