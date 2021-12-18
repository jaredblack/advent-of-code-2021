def get_input():
    in_file = open('in17.txt', 'r')
    input = in_file.read()
    in_file.close()
    x = tuple(map(int, input[input.find('x') + 2 : input.find(',')].split('..')))
    y = tuple(map(int, input[input.find('y') + 2 :].split('..')))

    return x, y


def on_target(pos, x_range, y_range):
    if pos[0] in range(x_range[0], x_range[1] + 1) and pos[1] in range(y_range[0], y_range[1] + 1):
        return True
    return False


def past_target(pos, x_range, y_range):
    if pos[0] > x_range[1] or pos[1] < y_range[0]:
        return True
    return False


def solve_a(x_range, y_range):
    y_max = 0
    for sx_vel in range(2, 100):
        for sy_vel in range(1, 1000):
            x_vel = sx_vel
            y_vel = sy_vel
            ix = sx_vel
            iy = sy_vel

            pos = (0, 0)
            local_y_max = 0
            while not past_target(pos, x_range, y_range):
                if on_target(pos, x_range, y_range):

                    print(f'got to target at {pos} with x_vel: {ix}, y_vel: {iy}')
                    if local_y_max > y_max:
                        y_max = local_y_max
                    break
                pos = (pos[0] + x_vel, pos[1] + y_vel)
                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1
                y_vel -= 1
                if pos[1] > local_y_max:
                    local_y_max = pos[1]
            # print(f'final pos: {pos}')
    return y_max


def solve_b(x_range, y_range):
    count = 0
    for sx_vel in range(2, 400):
        for sy_vel in range(-500, 500):
            x_vel = sx_vel
            y_vel = sy_vel

            pos = (0, 0)
            while not past_target(pos, x_range, y_range):
                if on_target(pos, x_range, y_range):
                    print(f'got to target at {pos} with x_vel: {sx_vel}, y_vel: {sy_vel}')
                    count += 1
                    break
                pos = (pos[0] + x_vel, pos[1] + y_vel)
                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1
                y_vel -= 1
            # print(f'final pos: {pos}')
    return count


if __name__ == '__main__':
    t1, t2 = get_input()
    print(solve_b(t1, t2))