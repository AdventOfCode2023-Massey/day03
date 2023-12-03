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
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j] == '*':
                adjacent_numbers = []
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if (ni, nj) in numbers:
                            adjacent_numbers.append(numbers[(ni, nj)])
                if len(adjacent_numbers) == 2:
                    total += adjacent_numbers[0] * adjacent_numbers[1]

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])