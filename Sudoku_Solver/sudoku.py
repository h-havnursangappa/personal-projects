# board = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#     ]

board = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]


def solve(bo):
    find = return_zeros(bo)
    if not find:
        return True
    else:
        row, col = find

    for nn in range(1, 10):
        if is_valid(bo, nn, (row, col)):
            bo[row][col] = nn

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def is_valid(bo, num, pos):
    # Check row
    for r in range(len(bo[0])):
        if bo[pos[0]][r] == num and pos[1] != r:
            return False

    # Check column
    for c in range(len(bo)):
        if bo[c][pos[1]] == num and pos[0] != c:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for ro in range(box_y * 3, box_y * 3 + 3):
        for co in range(box_x * 3, box_x * 3 + 3):
            if bo[ro][co] == num and (ro, co) != pos:
                return False

    return True


def print_board(bo):
    for ii in range(len(bo)):
        if ii % 3 == 0 and ii != 0:
            print("---------------------")

        for jj in range(len(bo[0])):
            if jj % 3 == 0 and jj != 0:
                print(" | ", end="")

            if jj == 8:
                print(str(bo[ii][jj]))
            else:
                print(str(bo[ii][jj]) + " ", end="")


def return_zeros(bo):
    for rr in range(len(bo)):
        for cc in range(len(bo[0])):
            if bo[rr][cc] == 0:
                return (rr, cc)
    return None


print_board(board)
print("\n\n")
solve(board)
print_board(board)
