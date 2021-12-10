import statistics

def get_input():
    in_file = open('in10.txt', 'r')
    lines = [x for x in in_file.read().split('\n')]
    in_file.close()
    return lines

def solve_a(input):
    lefts = '([{<'
    rights = ')]}>'
    pts = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137
    }
    sum = 0
    stack = []
    corrupted_indices = []
    for i, line in enumerate(input):
        for c in line:
            if c in lefts:
                stack.append(c)
            else:
                left = stack[-1]
                if left == '(' and c != ')':
                    sum += pts[c]
                    corrupted_indices.append(i)
                    break
                elif left == '{' and c != '}':
                    sum += pts[c]
                    corrupted_indices.append(i)
                    break
                elif left == '[' and c != ']':
                    sum += pts[c]
                    corrupted_indices.append(i)
                    break
                elif left == '<' and c != '>':
                    sum += pts[c]
                    corrupted_indices.append(i)
                    break
                else:
                    stack.pop()
    for i in reversed(corrupted_indices):
        input.pop(i)

    completion_scores = []
    for i, line in enumerate(input):
        score = 0
        stack = []
        for c in line:
            if c in lefts:
                stack.append(c)
            else:
                left = stack[-1]
                if left == '(' and c == ')' \
                        or (left == '{' and c == '}')\
                        or (left == '[' and c == ']')\
                        or (left == '<' and c == '>')\
                        or (left == '(' and c == ')'):
                    stack.pop()
        for c in reversed(stack):
            score *= 5
            if c == '{':
                score += 3
            elif c == '[':
                score += 2
            elif c == '(':
                score += 1
            elif c == '<':
                score += 4
        completion_scores.append(score)

    return statistics.median(completion_scores)

if __name__ == '__main__':
    print(solve_a(get_input()))