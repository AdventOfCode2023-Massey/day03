# Advent of Code 2023 Day 3 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys
import re

def main(filename):
    with open(filename, 'r') as file:
        schematic = [line.strip() for line in file]

    numbers = {}
    for i in range(len(schematic)):
        for match in re.finditer(r'\d+', schematic[i]):
            for j in range(match.start(), match.end()):
                numbers[(i, j)] = int(match.group())

    symbols = set(['*', '#', '+', '$'])
    total = 0

    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j] in symbols:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if (ni, nj) in numbers:
                            total += numbers[(ni, nj)]
                            break
                    else:
                        continue
                    break

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
