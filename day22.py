import collections

def get_input():
    in_file = open('in22.txt', 'r')
    in_str = in_file.read().replace(' ', ',')
    commands = []
    for line in in_str.split('\n'):
        sections = line.split(',')
        cmd = sections[0]
        x_axis, numbers = sections[1].split('=')
        x1, x2 = numbers.split('..')
        y_axis, numbers = sections[2].split('=')
        y1, y2 = numbers.split('..')
        z_axis, numbers = sections[3].split('=')
        z1, z2 = numbers.split('..')
        commands.append((cmd, (int(x1), int(x2)), (int(y1), int(y2)), (int(z1), int(z2))))
    in_file.close()
    return commands


def solve_a(commands):
    cube = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    for cmd in commands[:20]:
        s = 0
        if cmd[0] == 'on':
            s = 1
        if abs(cmd[1][0]) <= 50:
            for i in range(cmd[1][0], cmd[1][1] + 1):
                for j in range(cmd[2][0], cmd[2][1] + 1):
                    for k in range(cmd[3][0], cmd[3][1] + 1):
                        cube[i][j][k] = s
    count = 0
    for side in cube:
        for row in side:
            for entry in row:
                if entry:
                    count += 1
    return count


def generate_overlap(cuboid, cmd):
    # sign = -1 if cuboid[0] > 0 else 1
    x = (max(cuboid[0][0], cmd[1][0]), min(cuboid[0][1], cmd[1][1]))
    y = (max(cuboid[1][0], cmd[2][0]), min(cuboid[1][1], cmd[2][1]))
    z = (max(cuboid[2][0], cmd[3][0]), min(cuboid[2][1], cmd[3][1]))
    # return (sign*abs((x[1] - x[0] + 1)*(y[1] - y[0] + 1)*(z[1] - z[0] + 1))), x, y, z
    return x, y, z


def cubize(x, y, z):
    return x, y, z

def volume(x, y, z):
    return abs((x[1] - x[0] + 1)*(y[1] - y[0] + 1)*(z[1] - z[0] + 1))


def solve_b(commands):
    cuboids = collections.Counter()
    for i, cmd in enumerate(commands):
        overlaps = collections.Counter()
        for cuboid, sign in cuboids.items():
            overlap = generate_overlap(cuboid, cmd)
            if overlap[0][0] <= overlap[0][1] and overlap[1][0] <= overlap[1][1] and overlap[2][0] <= overlap[2][1]:
            # if volume(overlap[0], overlap[1], overlap[2]) != 0:
                    overlaps[overlap] -= sign
        cb = cmd[1], cmd[2], cmd[3]
        if cmd[0] == 'on':
            cuboids[cb] += 1
        else:
            pass
            # overlaps[cb] -= 1
        cuboids.update(overlaps)


        print(f'Processed cmd {i}, cuboid list size {len(cuboids)}')
    sum = 0
    for cuboid, sign in cuboids.items():
        sum += volume(cuboid[0], cuboid[1], cuboid[2]) * sign
    return sum


if __name__ == '__main__':
    print(solve_b(get_input()))