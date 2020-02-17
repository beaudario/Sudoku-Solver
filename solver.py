def Solve(bo):
    find = FindEmpty(bo)

    if not find(bo):
        return True
    else:
        row, col = find

    for i in range(1, 10):


def Valid(bo, num, pos):

    # check row
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check column
    for i in range(len(bo)):



def FindEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)       # row, col

    return None
