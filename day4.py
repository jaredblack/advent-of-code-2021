import numbers

def get_input():
    in_file = open('in4.txt', 'r')
    nums_called = [int(num) for num in in_file.readline().split(',')]
    unstruct_boards = [int(x) for x in in_file.read().split()]
    boards = []
    board_index = -1
    i = 0
    j = 0
    for u_ind, num in enumerate(unstruct_boards):
        if u_ind % 25 == 0:
            boards.append([])
            board_index += 1
            boards[board_index].append([])
            j = 0
            i = 0
        elif u_ind % 5 == 0:
            boards[board_index].append([])
            i += 1
            j = 0
        boards[board_index][i].append(num)
        j += 1


    return nums_called, boards

def count_score(board):
    sum = 0
    for row in board:
        for value in row:
            if isinstance(value, numbers.Number):
                sum += value
    return sum

def solve_a(nums_called, boards):
    for num in nums_called:
        # update boards
        for b_ind, board in enumerate(boards):
            for i, row in enumerate(boards[b_ind]):
                for j, entry in enumerate(boards[b_ind][i]):
                    if entry == num:
                        boards[b_ind][i][j] = 'x'
                        break

        # check for victory
        for board in boards:
            for row in board:
                for j, entry in enumerate(row):
                    if entry != 'x':
                        break
                else:
                    print('we have a winner')
                    return(count_score(board) * num)
            for j in range(5):
                for i in range(5):
                    if board[i][j] != 'x':
                        break
                else:
                    print('we have a winner')
                    return (count_score(board) * num)

def solve_b(nums_called, boards):
    for num in nums_called:
        # update boards
        for b_ind, board in enumerate(boards):
            for i, row in enumerate(boards[b_ind]):
                for j, entry in enumerate(boards[b_ind][i]):
                    if entry == num:
                        boards[b_ind][i][j] = 'x'
                        break

        # check for victory
        for board in boards:
            check = True
            for row in board:
                for j, entry in enumerate(row):
                    if entry != 'x':
                        break
                else:
                    if len(boards) == 1:
                        return count_score(boards[0]) * num
                    print('we have a winner')
                    boards.remove(board)
                    check = False
                    break
            if check:
                for j in range(5):
                    for i in range(5):
                        if board[i][j] != 'x':
                            break
                    else:
                        if len(boards) == 1:
                            return count_score(boards[0]) * num
                        print('we have a winner')
                        boards.remove(board)
                        break




if __name__ == '__main__':
    nums_called, boards = get_input()
    print(solve_a(nums_called, boards))