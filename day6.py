def get_input():
    in_file = open('in6.txt', 'r')
    fish = [int(num) for num in in_file.read().split(',')]
    in_file.close()
    return fish



def solve_a(fishes):
    fish_to_add = 0
    for day in range(80):
        fish_to_add = 0
        for i, fish in enumerate(fishes):
            if fish >= 1:
                fishes[i] -= 1
            else:
                fishes[i] = 6
                fish_to_add += 1
        for n in range(fish_to_add):
            fishes.append(8)
    return len(fishes)

def solve_b(fishes):
    fish_groups = {x:0 for x in range(9)}
    buffer_group = 0
    for fish in fishes:
        fish_groups[fish] += 1

    for day in range(256):
        for group in fish_groups.keys():
            if group == 0:
                buffer_group = fish_groups[group]
            else:
                fish_groups[group - 1] = fish_groups[group]
        fish_groups[6] += buffer_group
        fish_groups[8] = buffer_group

    return sum(fish_groups.values())

if __name__ == '__main__':
    print(solve_b(get_input()))