board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#print the board for better visulization
def printBoard(board):
    # function to place a line separater after every 3 lins
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - -") 

        # function to make 3*3 squares in a 9*9 board
        for j in range(len(board[0])):
            '''to print a vertical bar to separate a 3*3 square without moving to the next line'''
            if j % 3 == 0:
                print(" | ", end="")

            # to move to the next linwe    
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end=" ")


# function to check if the given board is valid or not
def validBoard(board, num, pos):

    #check rows 

    ''' the loop moves to the next column in the same row for every iteration'''
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i: # checks if the entered number already exists in that row or not
            return False

    #check columns

    ''' the loop moves to the next row in the same column for every iteration '''

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i: # checks if the entered number already exists in that column or not
            return False

    #chekc for 3*3 square

    ''' returns the position of the box as a tuple of 2 coordinates
    '''
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    for i in range(box_y * 3,box_y * 3 + 3):
       for j in range(box_x * 3,box_x * 3 + 3):
        if board[i][j] == num and (i,j) != pos:
            return False

    return True



# find a empty square on the board
''' the function checks for every single position the on the board and returns the address of the square that is empty or contains zero
'''
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # returns (row number,col number)
    return None 


#function to solve the board using recursive function
def solveBoard(board):

    #print(board) # prints the whole board for each and every iteration
    ''' to begin if the board has any empty squares or not and if not found return true stating the board is solved
    '''
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find 

    #tries to put the number between 1 to 9 at the empty position
    for i in range(1,10):
        if validBoard(board, i, (row, col)): # check if i is valid at empty position and assing the empty position to i
            board[row][col] = i

            if solveBoard(board): #recursive call to check the number
                return True

            board[row][col] = 0 # if board is not solved assing 0 again to the empty box and try again
        
    return False

printBoard(board)
print('shgvyfiasdf')
solveBoard(board)
print('tasfvtuF')
printBoard(board)