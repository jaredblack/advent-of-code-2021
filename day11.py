def get_input():
    in_file = open('in11.txt', 'r')
    octopi = [[int(octopus) for octopus in line] for line in in_file.read().split('\n')]
    in_file.close()
    return octopi

def in_bounds(x, y):
    if x > 9 or x < 0 or y > 9 or y < 0:
        return False
    return True

flashes = 0

def flash(octopi, i, j):
    global flashes
    flashes += 1
    octopi[i][j] = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if not (x == i and y == j) and in_bounds(x,y) and octopi[x][y] != 0:
                octopi[x][y] += 1
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if not (x == i and y == j) and in_bounds(x,y):
                if octopi[x][y] > 9:
                    flash(octopi, x, y)



def solve_a(octopi):
    for step in range(100):
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                octopi[i][j] += 1
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                if octopus > 9:
                    flash(octopi, i, j)
    return flashes

def solve_b(octopi):
    prev_flashes = 0
    step_flashes = 0
    steps = 0
    while step_flashes < 100:
        steps += 1
        step_flashes = 0
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                octopi[i][j] += 1
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                if octopus > 9:
                    flash(octopi, i, j)
        step_flashes = flashes - prev_flashes
        prev_flashes = flashes
    return steps


if __name__ == '__main__':
    print(solve_b(get_input()))