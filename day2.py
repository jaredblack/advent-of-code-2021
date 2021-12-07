def filein():
    in_file = open('in2.txt', 'r')
    file_in = [x for x in in_file.read().split()]
    in_file.close()
    return file_in


def solve(filein):
    i = 0
    h_pos = 0
    v_pos = 0
    aim = 0
    while i < len(filein) - 1:
        command = filein[i]
        amount = int(filein[i + 1])
        if command == 'forward':
            h_pos += amount
            v_pos += aim * amount
        elif command == 'down':
            aim += amount
        elif command == 'up':
            aim -= amount
        i += 2
    return h_pos * v_pos

if __name__ == "__main__":
    print(solve(filein()))