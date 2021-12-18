import math
import re

def get_input():
    in_file = open('in18.txt', 'r')
    lines = [line for line in in_file.read().split('\n')]
    in_file.close()
    numbers = []
    for line in lines:
        numbers.append([])
        for c in line:
            if c.isdigit():
                numbers[-1].append(int(c))
            else:
                numbers[-1].append(c)

    return numbers


def pn(number):
    for c in number:
        print(c, end='')
    print()


def explode(number):
    unclosed_lefts = 0
    last_rn_ind = -1
    i = 0
    while i < len(number):
        if number[i] == '[':
            unclosed_lefts += 1
        elif number[i] == ']':
            unclosed_lefts -= 1
        elif isinstance(number[i], int):
            if unclosed_lefts > 4:
                if last_rn_ind != -1:
                    number[last_rn_ind] += number[i]
                i += 2
                for j in range(i + 1, len(number)):
                    if isinstance(number[j], int):
                        number[j] += number[i]
                        break
                number[i - 3 : i + 2] = [0]
                last_rn_ind = i - 1
                unclosed_lefts -= 2
                break
            else:
                last_rn_ind = i
        i += 1
    else:
        return False
    # pn(number)
    return True


def split(number):
    for i, c in enumerate(number):
        if isinstance(c, int) and c >= 10:
            half = c / 2
            number[i:i+1] = ['[', math.floor(half), ',', math.ceil(half) , ']']
            break
    else:
        return False
    # pn(number)
    return True


def magnitude(number):
    # convert to string
    n_str = ''.join((str(c) for c in number))
    match = True
    while match:
        match = re.search(r'\[[0-9]+,[0-9]+]', n_str)
        if match:
            simple_pair = match.group()
            values = tuple(int(x) for x in re.findall('[0-9]+', simple_pair))
            mag = 3 * values[0] + 2 * values[1]
            n_str = n_str.replace(match.group(), str(mag))
    return int(n_str)


def solve_a(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result.insert(0, '[')
        result.append(',')
        result.extend(numbers[i])
        result.append(']')
        eos = True
        while eos:
            eos = explode(result)
            if not eos:
                eos = split(result)
    return magnitude(result)


def solve_b(numbers):
    max_mag = 0
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j:
                result = list(num1)
                result.insert(0, '[')
                result.append(',')
                result.extend(num2)
                result.append(']')
                eos = True
                while eos:
                    eos = explode(result)
                    if not eos:
                        eos = split(result)
                mag = magnitude(result)
                if mag > max_mag:
                    max_mag = mag
    return max_mag




if __name__ == '__main__':
    print(solve_b(get_input()))