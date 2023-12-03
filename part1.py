# Advent of Code 2023 Day 3 Part 1
# Code by Github Copilot Chat
# Editing by Bart Massey

import sys

def main(filename):
    with open(filename, 'r') as file:
        schematic = [list(line.strip()) for line in file]

    total = 0

    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit() == False and schematic[i][j] != '.':
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(schematic) and 0 <= nj < len(schematic[i]) and schematic[ni][nj].isdigit():
                            total += int(schematic[ni][nj])
    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
