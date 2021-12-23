import functools

def get_input():
    in_file = open('in21.txt', 'r')
    fluff, p1start = in_file.readline().split(': ')
    fluff, p2start = in_file.readline().split(': ')
    return int(p1start), int(p2start)


def move_player(ppos, roll):
    for i in range(1, roll + 1):
        ppos += 1
        if ppos > 10:
            ppos = 1
    return ppos


def inc_die(die):
    die += 1
    if die > 100:
        die = 1
    return die


def solve_a(p1start, p2start):
    p1pos = p1start
    p2pos = p2start
    p1score = 0
    p2score = 0
    rolls = 0
    die = 1
    while p1score < 1000 and p2score < 1000:
        for i in range(3):
            p1pos = move_player(p1pos, die)
            die = inc_die(die)
            rolls += 1
        p1score += p1pos
        if p1score >= 1000:
            break
        for i in range(3):
            p2pos = move_player(p2pos, die)
            die = inc_die(die)
            rolls += 1
        p2score += p2pos
    return min(p1score, p2score) * rolls


@functools.cache
def play(p1, p2, s1, s2):
    if s2 >= 21:
        return 0, 1
    if s1 >= 21:
        return 1, 0
    w1, w2 = 0, 0
    for r1 in [1,2,3]:
        for r2 in [1,2,3]:
            for r3 in [1,2,3]:
                new_p1 = (p1 + r1 + r2 + r3) % 10 or 10
                new_s1 = s1 + new_p1
                wo1, wo2 = play(p2, new_p1, s2, new_s1)
                w1 += wo2
                w2 += wo1
    return w1, w2

def solve_b(p1start, p2start):
    return play(p1start, p2start, 0, 0)


if __name__ == '__main__':
    p1start, p2start = get_input()
    print(solve_b(p1start, p2start))