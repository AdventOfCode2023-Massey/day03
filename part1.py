import sys

def main(filename):
    with open(filename, 'r') as file:
        schematic = [list(line.strip()) for line in file]

    symbols = set(['*', '#', '+', '$'])
    total = 0

    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit():
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(schematic) and 0 <= nj < len(schematic[i]) and schematic[ni][nj] in symbols:
                            total += int(schematic[i][j])
                            break
    print(total)

if __name__ == "__main__":
    main(sys.argv[1])