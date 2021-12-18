def get_input():
    in_file = open('in14.txt', 'r')
    template = in_file.readline().strip()
    lines = [line for line in in_file.read().split('\n')]
    lines.pop(0)
    rules = {}
    for line in lines:
        left, right = line.split(' -> ')
        rules[left] = right
    return template, rules


def solve_a(template, rules):
    polymer = list(template)
    for _ in range(10):
        i = 0
        while i < len(polymer) - 1:
            comp = polymer[i] + polymer[i + 1]
            if comp in rules:
                polymer.insert(i + 1, rules[comp])
                i += 1
            i += 1
        print(''.join(polymer))
    occurences = {}
    for e in polymer:
        if e not in occurences:
            occurences[e] = 1
        else:
            occurences[e] += 1
    return max(occurences.values()) - min(occurences.values())


def solve_b(template, rules):
    pair_rules = {}
    occurrences = {}
    char_occ = {}
    # Initialize occurrences
    for rule in rules:
        pair_rules[rule] = (rule[0] + rules[rule], rules[rule] + rule[1])
        char_occ[rule[0]] = 0
        char_occ[rule[1]] = 0
    for pr in pair_rules:
        occurrences[pr] = 0
        occurrences[pair_rules[pr][0]] = 0
        occurrences[pair_rules[pr][1]] = 0
    for c in template:
        char_occ[c] += 1
    for i in range(len(template) - 1):
        if template[i] + template[i + 1] in occurrences:
            occurrences[template[i] + template[i + 1]] += 1
        else:
            occurrences[template[i] + template[i + 1]] = 1
    old_occurrences = occurrences.copy()
    for it in range(40):
        for pair in old_occurrences:
            if old_occurrences[pair] > 0 and pair in pair_rules:
                x, y = pair_rules[pair]
                occurrences[x] += old_occurrences[pair]
                occurrences[y] += old_occurrences[pair]
                char_occ[rules[pair]] += old_occurrences[pair]
                occurrences[pair] -= old_occurrences[pair]
        old_occurrences = occurrences.copy()

    # counts = {}
    # for pair in occurrences:
    #     if pair[0] in counts:
    #         counts[pair[0]] += occurrences[pair]
    #     else:
    #         counts[pair[0]] = occurrences[pair]

    return max(char_occ.values()) - min(char_occ.values())



if __name__ == '__main__':
    template, rules = get_input()
    print(solve_b(template, rules))