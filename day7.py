import statistics

def get_input():
    in_file = open('in7.txt', 'r')
    crabs = [int(num) for num in in_file.read().split(',')]
    in_file.close()
    return crabs

def calculate_costs(crabs, guess):
    cost = 0
    for crab in crabs:
        cost += abs(crab - guess)
    return cost

def calculate_costs_b(crabs, guess):
    cost = 0
    for crab in crabs:
        dist = abs(crab - guess)
        for c in range(1, dist + 1):
            cost += c
    return cost

def solve_b(crabs):
    guess = 1
    best_cost_guess = calculate_costs_b(crabs, guess)
    high_cost = calculate_costs_b(crabs, guess + 1)
    low_cost = calculate_costs_b(crabs, guess - 1)
    i = 2
    if high_cost < best_cost_guess:
        best_cost_guess = high_cost
    while high_cost <= best_cost_guess:
        high_cost = calculate_costs_b(crabs, guess + i)
        if high_cost < best_cost_guess:
            best_cost_guess = high_cost
        i += 1
    if low_cost < best_cost_guess:
        best_cost_guess = low_cost
    while low_cost <= best_cost_guess and i >= 0:
        low_cost = calculate_costs_b(crabs, guess - i)
        if low_cost < best_cost_guess:
            best_cost_guess = low_cost
        i += 1

    return best_cost_guess

def solve_a(crabs):
    guess = round(statistics.mean(crabs))
    best_cost_guess = calculate_costs(crabs, guess)
    high_cost = calculate_costs(crabs, guess + 1)
    low_cost = calculate_costs(crabs, guess - 1)
    i = 2
    while high_cost < best_cost_guess:
        high_cost = calculate_costs(crabs, guess + i)
        if high_cost < best_cost_guess:
            best_cost_guess = high_cost
        i += 1
    while low_cost <= best_cost_guess and i >= 0:
        low_cost = calculate_costs(crabs, guess - i)
        if low_cost < best_cost_guess:
            best_cost_guess = low_cost
        i += 1

    return best_cost_guess

if __name__ == '__main__':
    print(solve_b(get_input()))