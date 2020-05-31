board = [["wr","wn", "wb", "wq", "wk", "wb", "wn", "wr"],["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],["br","bn", "bb", "bq", "bk", "bb", "bn", "br"]]
def showboard(board):
    for i in range(7,-1,-1):
        print(board[i])

def move(row, column, newrow, newcolumn):
    piece = board[row][column]
    legalmoves = []
    if piece == "wp":
        pawn(board, row, column, newrow, newcolumn, legalmoves)
        
        movewrite(board, row, column, newrow, newcolumn, piece, legalmoves)
    if piece == "wn":
        knight(board, row, column, newrow, newcolumn, legalmoves)
        
        movewrite(board, row, column, newrow, newcolumn, piece, legalmoves)
    if piece == "wb":
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "topright")
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "topleft")
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "bottomright")
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "bottomleft")
        
        movewrite(board, row, column, newrow, newcolumn, piece, legalmoves)
    if piece == "wr":
        straight(board, row, column, newrow, newcolumn, legalmoves)

        movewrite(board, row, column, newrow, newcolumn, piece, legalmoves)

    if piece == "wq":
        straight(board, row, column, newrow, newcolumn, legalmoves)
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "topright")
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "topleft")
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "bottomright")
        diagonal(board, row, column, newrow, newcolumn, legalmoves, "bottomleft")

        movewrite(board, row, column, newrow, newcolumn, piece, legalmoves)

        






def diagonal(board, row, column, newrow, newcolumn, legalmoves, direction):
    dirdic = {
        "topright":(7,1,7,1),
        "topleft":(7,1,0,-1),
        "bottomright":(0,-1,7,1),
        "bottomleft":(0,-1,0,-1)
    }
    i = 0 
    j = 0
    rowdir = dirdic[direction][1]
    coldir = dirdic[direction][3]
    while i != dirdic[direction][0]-row and j != dirdic[direction][2]-column:
        legalmoves.append((row+i+rowdir,column+j+coldir))
        if board[row+i+rowdir][column+j+coldir] != "--":
            break    
        i += rowdir
        j += coldir

def knight(board, row, column, newrow, newcolumn, legalmoves):
    for i in range(1,3):
            legalmoves.append((row+2,column-1))
            legalmoves.append((row+2,column+1))
            legalmoves.append((row+1,column-2))
            legalmoves.append((row+1,column+2))
            legalmoves.append((row-1,column-2))
            legalmoves.append((row-1,column+2))
            legalmoves.append((row-2,column-1))
            legalmoves.append((row-2,column+1))

def pawn(board, row, column, newrow, newcolumn, legalmoves):
    if board[newrow][newcolumn] == "--" and newcolumn == column :
        legalmoves.append((row+1, column))
        if row == 1:
            legalmoves.append((row+2,column))
    if board[row+1][column-1] != "--" or board[row+1][column+1] != "--":
        legalmoves.append((row+1,column-1))
        legalmoves.append((row+1,column+1))

def movewrite(board, row, column, newrow, newcolumn, piece, legalmoves):
    if legalmoves.count((newrow,newcolumn)) == 1:
        board[newrow][newcolumn] = piece                
        board[row][column] = "--"



def straight(board, row, column, newrow, newcolumn, legalmoves):
    for i in range(7):
        try:
            legalmoves.append((row+ i + 1,column))
            if board[row+ i + 1][column] != "--":
                break
        except:
            break
    for i in range(0,-7):
        try:
            legalmoves.append((row+ i - 1, column))
            if board[row+ i - 1][column] != "--":
                break
        except:
            break
    for i in range(7):
        try:
            legalmoves.append((row, column+ i + 1))
            if board[row][column+ i + 1] != "--":
                break
        except:
            break
    for i in range(0,-7):
        try:
            legalmoves.append((row, column+ i - 1))
            if board[row][column+ i - 1] != "--":
                break
        except:
            break

def king(board, row, column, newrow, newcolumn, legalmoves):
    for i in range(row-1, row+2):
        for j in range(column-1,column+1):
            legalmoves.append()


showboard(board)
move(0,3,3,3)
showboard(board)
move(3,3,4,4)
showboard(board)

