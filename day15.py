from math import inf


def get_input():
    in_file = open('in15.txt', 'r')
    lines = [line for line in in_file.read().split('\n')]
    matrix = [[int(entry) for entry in line] for line in lines]
    in_file.close()

    return matrix


def edge_weight(matrix, u, v):
    if u == (v[0] - 1, v[1]) or\
        u == (v[0] + 1, v[1]) or\
        u == (v[0], v[1] - 1) or\
        u == (v[0], v[1] + 1):
        return matrix[v[0]][v[1]]
    return inf


def in_bounds(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return False
    return True


def make_big_matrix(small_matrix):
    L = len(small_matrix)
    matrix = [row * 5 for row in small_matrix]
    for _ in range(4):
        for i in range(L):
            matrix.append(list(matrix[i]))
    for i in range(L * 5):
        for j in range(L * 5):
            if i >= L:
                matrix[i][j] = matrix[i - L][j] + 1
            elif j >= L:
                matrix[i][j] = matrix[i][j - L] + 1
            if matrix[i][j] == 10:
                matrix[i][j] = 1
    return matrix


def solve_a(matrix):
    S = set()
    Lv = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            Lv[(i,j)] = inf
    Lv[(0,0)] = 0
    while len(S) < len(matrix) * len(matrix[0]):
        minimum = inf
        for vertex in Lv:
            if vertex not in S:
                if Lv[vertex] < minimum:
                    minimum = Lv[vertex]
                    u = vertex
        S.add(u)
        for i in range(u[0]-1,u[0]+2):
            for j in range(u[1]-1,u[1]+2):
                if in_bounds(matrix, i, j) and (i,j) not in S:
                    if Lv[u] + edge_weight(matrix, u, (i, j)) < Lv[(i,j)]:
                        Lv[(i,j)] = Lv[u] + edge_weight(matrix, u, (i,j))

    # for k in Lv:
    #     print(f'{k}: {Lv[k]}')
    return Lv[(len(matrix)-1,len(matrix[0])-1)]

def solve_b(matrix):
    S = set()
    Lv = {}
    make_big_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            Lv[(i,j)] = inf
    Lv[(0,0)] = 0
    while len(S) < len(matrix) * len(matrix[0]):
        minimum = inf
        for vertex in Lv:
            if vertex not in S:
                if Lv[vertex] < minimum:
                    minimum = Lv[vertex]
                    u = vertex
        S.add(u)
        for i in range(u[0]-1,u[0]+2):
            for j in range(u[1]-1,u[1]+2):
                if in_bounds(matrix, i, j) and (i,j) not in S:
                    if Lv[u] + edge_weight(matrix, u, (i, j)) < Lv[(i,j)]:
                        Lv[(i,j)] = Lv[u] + edge_weight(matrix, u, (i,j))
        if u == (len(matrix) - 1, len(matrix[0]) - 1):
            print('point reached')
            # break
    return Lv[(len(matrix)-1,len(matrix[0])-1)]



if __name__ == '__main__':
    input = get_input()
    matrix = make_big_matrix(input)
    print(solve_a(matrix))