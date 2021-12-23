def get_input():
    in_file = open('in20.txt', 'r')
    algorithm, lines = in_file.read().split('\n\n')
    in_file.close()
    grid = [[entry for entry in line] for line in lines.split('\n')]
    return algorithm, grid


def pg(grid):
    for row in grid:
        for entry in row:
            print(entry, end='')
        print()


def on_edge(x, y, grid):
    H = len(grid)
    L = len(grid[0])
    if x == 0 or L - x == 1 or y == 0 or H - y == 1:
        return True
    return False


def augment_grid(grid):
    extra_dots = ['.' for _ in range(99)]
    augmented_grid = []
    for i in range(len(grid)):
        line = list(extra_dots)
        line.extend(grid[i])
        line.extend(extra_dots)
        augmented_grid.append(line)
    dots_row = ['.' for _ in range(len(augmented_grid[0]))]
    for _ in range(99):
        augmented_grid.insert(0, dots_row)
        augmented_grid.append(dots_row)
    return augmented_grid


def solve_a(algorithm, grid):
    grid = augment_grid(grid)
    output = [['.' for j in range(len(grid[0]))] for i in range(len(grid))]
    # output = []
    # for row in grid:
    #     output.append(list(row))
    # pg(output)
    for _ in range(50):
        output = [['.' for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                bin_str = ''
                if on_edge(i, j, grid):
                    if grid[i][j] == '.':
                        bin_str = '0' * 9
                    else:
                        bin_str = '1' * 9
                else:
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if grid[k][l] == '.':
                                bin_str += '0'
                            else:
                                bin_str += '1'
                index = int(bin_str, 2)
                output[i][j] = algorithm[index]
        grid = output
    # pg(grid)
    # print('~~~~~~~~~')
    # pg(output)
    lit = 0
    for row in output:
        for entry in row:
            if entry == '#':
                lit += 1
    return lit


if __name__ == '__main__':
    algorithm, grid = get_input()
    print(solve_a(algorithm, grid))
