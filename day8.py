def get_input():
    in_file = open('in8.txt', 'r')
    entries = [x for x in in_file.read().split('\n')]
    e_list = []
    for entry in entries:
        signals, output = entry.split('|')
        s_list = [''.join(sorted(x)) for x in signals.split()]
        o_list = [''.join(sorted(x)) for x in output.split()]
        e_list.append([])
        e_list[-1].append(s_list)
        e_list[-1].append(o_list)
    return e_list

def solve_a(entries):
    count = 0
    for entry in entries:
        output = entry[1]
        for o in output:
            if len(o) == 2 or len(o) == 4 or len(o) == 3 or len(o) == 7:
                count += 1
    return count

def is_in(a, b):
    for c in a:
        if c not in b:
            return False
    return True

def solve_b(entries):
    num_to_code = {}
    sum = 0
    for entry in entries:
        signals, output = entry
        for signal in signals:
            if len(signal) == 2:
                num_to_code[1] = signal
            elif len(signal) == 3:
                num_to_code[7] = signal
            elif len(signal) == 4:
                num_to_code[4] = signal
            elif len(signal) == 7:
                num_to_code[8] = signal
        for signal in signals:
            if len(signal) == 6:
                if is_in(num_to_code[4], signal):
                    num_to_code[9] = signal
                elif is_in(num_to_code[7], signal):
                    num_to_code[0] = signal
                else:
                    num_to_code[6] = signal
        for signal in signals:
            if len(signal) == 5:
                if is_in(num_to_code[1], signal):
                    num_to_code[3] = signal
                elif is_in(num_to_code[9], ''.join(sorted(num_to_code[1] + signal))):
                    num_to_code[5] = signal
                else:
                    num_to_code[2] = signal

        code_to_num = {num_to_code[k]: k for k in num_to_code}
        o_str = ''
        for o in output:
            o_str += str(code_to_num[o])
        sum += int(o_str)
    return sum


if __name__ == '__main__':
    entries = get_input()
    print(solve_b(entries))