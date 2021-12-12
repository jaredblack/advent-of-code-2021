def get_input():
    in_file = open('test_in12.txt', 'r')
    lines = [line for line in in_file.read().split('\n')]
    cave_map = {}
    for line in lines:
        a, b = line.split('-')
        if a not in cave_map:
            cave_map[a] = []
        if b not in cave_map:
            cave_map[b] = []
        if b == 'start' or a == 'end':
            cave_map[b].append(a)
        else:
            if a != 'start' and b != 'end':
                cave_map[b].append(a)
            cave_map[a].append(b)
    return cave_map


def has_double(path):
    for cave in path.split(','):
        if str.islower(cave) and path.count(cave) > 1:
            return True
    return False


num_paths = 0


def visit_cave(current, path, cave_map):
    global num_paths
    path += ',' + current
    if current == 'end':
        # print(f'PATH {num_paths}: {path}')
        # print(path)
        num_paths += 1
    else:
        for adj_node in cave_map[current]:
            if str.islower(adj_node) and not has_double(path) and path.count(adj_node) == 1:
                # path = '`' + path
                visit_cave(adj_node, path, cave_map)
            elif str.isupper(adj_node[0]) or adj_node not in path:
                visit_cave(adj_node, path, cave_map)


def solve_a(cave_map):
    visit_cave('start', "", cave_map)
    return num_paths


if __name__ == '__main__':
    cave_map = get_input()
    print(solve_a(cave_map))
