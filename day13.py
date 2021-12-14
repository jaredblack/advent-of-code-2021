import numpy as np

def get_input():
    in_file = open('in13.txt', 'r')
    coords = []
    folds = []
    in_str = in_file.read()
    for line in in_str.split('\n'):
        if len(line) == 0:
            continue
        if line[0] != 'f':
            coords.append(tuple(map(int, line.split(','))))
        else:
            left, right = line.split('=')
            folds.append((left[-1], int(right)))
    in_file.close()
    return coords, folds

def solve_a(coords, folds):
    x_max = max([first for first, second in coords])
    y_max = max([second for first, second in coords])
    matrix = np.zeros((x_max + 1, y_max + 1))
    for coord in coords:
        matrix[coord] = 1
    for axis, line in folds:
        if axis == 'x':
            # fold is either UP or LEFT
            left_half = matrix[:line, :]
            right_half = np.flipud(matrix[line + 1:, :])
            matrix = left_half + right_half
        else:
            print(matrix[:,line])
            top_half = matrix[:, :line]
            bottom_half = np.fliplr(matrix[:, line + 1:])
            if len(bottom_half[0]) < len(top_half[0]):
                bottom_half = np.hstack([np.zeros((len(bottom_half), 1)), bottom_half])
            matrix = bottom_half + top_half
    matrix = np.transpose(matrix)
    for row in matrix:
        for entry in row:
            if entry > 0:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    return np.count_nonzero(matrix)


if __name__ == '__main__':
    coords, folds = get_input()
    print(solve_a(coords, folds))