#Eight queens solution
#David Martínek, 2022

#Function searching for queens in row, column and diagonals
def LineChecker(row,column):
    for i in range(QUEENS_NUM):
        if board[row][i] == "Q":
            return False

    for i in range(QUEENS_NUM):
        for j in range(QUEENS_NUM):
            if board[i][j] == "Q":
                if abs(i - row) == abs(j - column):
                    return False
    return True

#Fuction placing queens on board using backtracking
def Placement(column):
    if column >= QUEENS_NUM:
        return True

    for i in range(QUEENS_NUM):
                if LineChecker(i, column):
                    board[i][column] = "Q"
                    if Placement(column + 1) == True:
                        return True
                    board[i][column] = "-"
    return board

#Initial variables and creation of board [8x8]
QUEENS_NUM = 8
board = [["-"]*QUEENS_NUM for i in range(QUEENS_NUM)]

#Placement
Placement(0)

#Board print
for i in range(QUEENS_NUM):
    for j in range(QUEENS_NUM):
        print(board[i][j], end=" ")
    print("")