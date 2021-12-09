def get_input():
    in_file = open('in9.txt', 'r')
    lines = [x for x in in_file.read().split('\n')]
    heightmap = [[int(x) for x in line] for line in lines]
    return heightmap


def in_bounds(i, j, m, n):
    if i < 0 or j < 0 or i >= m or j >= n:
        return False
    return True

def solve_a(heightmap):
    risk_sum = 0
    m = len(heightmap)
    n = len(heightmap[0])
    for i in range(m):
        for j in range(n):
            if in_bounds(i - 1, j, m, n):
                if heightmap[i - 1][j] <= heightmap[i][j]:
                    continue
            if in_bounds(i, j - 1, m, n):
                if heightmap[i][j - 1] <= heightmap[i][j]:
                    continue
            if in_bounds(i, j + 1, m, n):
                if heightmap[i][j + 1] <= heightmap[i][j]:
                    continue
            if in_bounds(i + 1, j, m, n):
                if heightmap[i + 1][j] <= heightmap[i][j]:
                    continue
            risk_sum += heightmap[i][j] + 1


    return risk_sum

def check_sq(h, i, j):
    if in_bounds(i, j, len(h), len(h[0])):
        if h[i][j] == 9:
            return 0
        else:
            h[i][j] = 9
            return 1 + check_sq(h, i - 1, j) + check_sq(h, i + 1, j) \
                   + check_sq(h, i, j - 1) + check_sq(h, i, j + 1)
    return 0

def solve_b(heightmap):
    basins = []
    # checked_field = [[False for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            basins.append(check_sq(heightmap, i, j))
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == '__main__':
    print(solve_b(get_input()))