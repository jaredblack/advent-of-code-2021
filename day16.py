import math

pos = 0

def get_input():
    in_file = open('in16.txt', 'r')
    input = in_file.read()
    in_file.close()
    return input


def operate(type_id, subvalues):
    print(f'Operation type {type_id} on {subvalues}')
    if type_id == 0:
        return sum(subvalues)
    elif type_id == 1:
        return math.prod(subvalues)
    elif type_id == 2:
        return min(subvalues)
    elif type_id == 3:
        return max(subvalues)
    elif type_id == 5:
        return int(subvalues[0] > subvalues[1])
    elif type_id == 6:
        return int(subvalues[0] < subvalues[1])
    elif type_id == 7:
        return int(subvalues[0] == subvalues[1])

def parse_packet_a(binary):
    global pos
    version = int(binary[pos:pos + 3], 2)
    v_sum = version
    pos += 3
    type_id = int(binary[pos:pos + 3], 2)
    pos += 3
    # Check if packet contains a literal (4)
    if type_id == 4:
        prefix_one = True
        bits_list = []
        while prefix_one:
            prefix = int(binary[pos])
            pos += 1
            if not prefix:
                prefix_one = False
            bits_list.append(binary[pos:pos + 4])
            pos += 4
        literal = int(''.join(bits_list), 2)
        print(f'Literal packet: {literal}')
    else:
        type_id = int(binary[pos])
        pos += 1
        if type_id:
            num_subpackets = int(binary[pos:pos+11], 2)
            pos += 11
            print(f'Operator packet (type {type_id}), {num_subpackets} subpackets')
            for sp in range(num_subpackets):
                v_sum += parse_packet_a(binary)
        else:
            len_packets = int(binary[pos:pos+15],2)
            pos += 15
            print(f'Operator packet (type {type_id}), length {len_packets}')
            expected_pos = pos + len_packets
            while pos < expected_pos:
                v_sum += parse_packet_a(binary)
    return v_sum


def parse_packet_b(binary):
    global pos
    version = int(binary[pos:pos + 3], 2)
    pos += 3
    type_id = int(binary[pos:pos + 3], 2)
    pos += 3
    # Check if packet contains a literal (4)
    if type_id == 4:
        prefix_one = True
        bits_list = []
        while prefix_one:
            prefix = int(binary[pos])
            pos += 1
            if not prefix:
                prefix_one = False
            bits_list.append(binary[pos:pos + 4])
            pos += 4
        literal = int(''.join(bits_list), 2)
        print(f'Literal packet: {literal}')
        return literal
    else:
        len_type_id = int(binary[pos])
        subvalues = []
        pos += 1
        if len_type_id:
            num_subpackets = int(binary[pos:pos+11], 2)
            pos += 11
            print(f'Operator packet (type {type_id}), {num_subpackets} subpackets')
            for sp in range(num_subpackets):
                subvalues.append(parse_packet_b(binary))
        else:
            len_packets = int(binary[pos:pos+15],2)
            pos += 15
            print(f'Operator packet (type {type_id}), length {len_packets}')
            expected_pos = pos + len_packets
            while pos < expected_pos:
                subvalues.append(parse_packet_b(binary))
        result = operate(type_id, subvalues)
        return result


def solve_a(input):
    binary = bin(int(input, 16))[2:].zfill(len(input) * 4)
    return parse_packet_a(binary)


def solve_b(input):
    binary = bin(int(input, 16))[2:].zfill(len(input) * 4)
    return parse_packet_b(binary)

if __name__ == '__main__':
    print(solve_b(get_input()))