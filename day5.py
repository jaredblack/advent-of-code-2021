import numbers

def get_input():
    in_file = open('in5.txt', 'r')
    full_in = in_file.read().replace(' -> ',',').replace('\n',',')
    coord_list = []
    counter = 0
    for c in full_in.split(','):
        if counter % 4 == 0 and (coord_list == [] or coord_list[-1] != []):
            coord_list.append([])
        if c.isdigit():
            coord_list[-1].append(int(c))
            counter += 1
    in_file.close()
    return coord_list

def solve_a(coord_list):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for coord_pair in coord_list:
        if coord_pair[0] < coord_pair[2] and coord_pair[1] == coord_pair[3]:
            for i in range(coord_pair[0], coord_pair[2] + 1):
                grid[i][coord_pair[1]] += 1
        elif coord_pair[0] > coord_pair[2] and coord_pair[1] == coord_pair[3]:
            for i in range(coord_pair[2], coord_pair[0] + 1):
                grid[i][coord_pair[1]] += 1
        elif coord_pair[1] < coord_pair[3] and coord_pair[0] == coord_pair[2]:
            for j in range(coord_pair[1], coord_pair[3] + 1):
                grid[coord_pair[0]][j] += 1
        elif coord_pair[1] > coord_pair[3] and coord_pair[0] == coord_pair[2]:
            for j in range(coord_pair[3], coord_pair[1] + 1):
                grid[coord_pair[0]][j] += 1
    overlap = 0
    for row in grid:
        for entry in row:
            if entry > 1:
                overlap += 1
    return overlap


def solve_b(coord_list):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for coord_pair in coord_list:
        if coord_pair[0] < coord_pair[2] and coord_pair[1] == coord_pair[3]:
            for i in range(coord_pair[0], coord_pair[2] + 1):
                grid[i][coord_pair[1]] += 1
        elif coord_pair[0] > coord_pair[2] and coord_pair[1] == coord_pair[3]:
            for i in range(coord_pair[2], coord_pair[0] + 1):
                grid[i][coord_pair[1]] += 1
        elif coord_pair[1] < coord_pair[3] and coord_pair[0] == coord_pair[2]:
            for j in range(coord_pair[1], coord_pair[3] + 1):
                grid[coord_pair[0]][j] += 1
        elif coord_pair[1] > coord_pair[3] and coord_pair[0] == coord_pair[2]:
            for j in range(coord_pair[3], coord_pair[1] + 1):
                grid[coord_pair[0]][j] += 1
        else:
            x_step = 0
            if coord_pair[0] < coord_pair[2]:
                x_step = 1
            else:
                x_step = -1
            y_step = 0
            if coord_pair[1] < coord_pair[3]:
                y_step = 1
            else:
                y_step = -1

            x_coords = [x for x in range(coord_pair[0], coord_pair[2] + x_step, x_step)]
            y_coords = [y for y in range(coord_pair[1], coord_pair[3] + y_step, y_step)]
            coords_to_mark = [(x_coords[i], y_coords[i]) for i in range(len(x_coords))]
            for x, y in coords_to_mark:
                grid[x][y] += 1
    overlap = 0
    for row in grid:
        for entry in row:
            if entry > 1:
                overlap += 1
    return overlap

if __name__ == '__main__':
    input = get_input()
    print(solve_a(input))