#Δημιουργία λεξικού με το ταμπλό της έναρξης - Κίνηση 0
board = {0:{
(1,1): 'R', (2,1): 'N', (3,1): 'B', (4,1): 'Q', (5,1): 'K', (6,1): 'B', (7,1): 'N', (8,1): 'R',
(1,2): 'P', (2,2): 'P', (3,2): 'P', (4,2): 'P', (5,2): 'P', (6,2): 'P', (7,2): 'P', (8,2): 'P',
(1,3): '.', (2,3): '.', (3,3): '.', (4,3): '.', (5,3): '.', (6,3): '.', (7,3): '.', (8,3): '.',
(1,4): '.', (2,4): '.', (3,4): '.', (4,4): '.', (5,4): '.', (6,4): '.', (7,4): '.', (8,4): '.',
(1,5): '.', (2,5): '.', (3,5): '.', (4,5): '.', (5,5): '.', (6,5): '.', (7,5): '.', (8,5): '.',
(1,6): '.', (2,6): '.', (3,6): '.', (4,6): '.', (5,6): '.', (6,6): '.', (7,6): '.', (8,6): '.',
(1,7): 'p', (2,7): 'p', (3,7): 'p', (4,7): 'p', (5,7): 'p', (6,7): 'p', (7,7): 'p', (8,7): 'p',
(1,8): 'r', (2,8): 'n', (3,8): 'b', (4,8): 'q', (5,8): 'k', (6,8): 'b', (7,8): 'n', (8,8): 'r',
}}


#Εμφάνιση ταμπλό
def showBoard(board):
    for r in range(8,0,-1):
        for f in range(1,9):
            print(f"{board[f,r]:2s}", end='')
        print('')
    print('')

#Προσθήκη στο λεξικό του ταμπλό της νέας κίνησης (υπολεξικό)
def addMoveToBoard(move, piece, from_square, to_square):
    board[move] = board[move-1] #Αντιγραφή απο το ταμπλό της προηγούμενης κίνησης
    board[move].update({from_square: '.'}) #Άδειασμα του τετραγώνου Αναχώρησης
    board[move].update({to_square: piece}) #Ενημέρωση του τετραγώνου Προορισμού

def findCurrentPositions(board, check_piece):
    #find the positions of a piece
    positions = []
    for position, piece in board.items():
        if piece == check_piece:
            positions.append(position)
    print(f'{check_piece} possible position/s -> {positions}')
    return(positions)

def find_from_wking(move,to_square):
    fr = findCurrentPositions(board[move-1],"K")
    possible_pos = []
    for y in range(fr[0][0]-1,fr[0][0]+2):
        for x in range(fr[0][1]-1,fr[0][1]+2):
            possible_pos.append((y,x))
    if to_square in possible_pos:
        print(f"White King was in {fr[0]}")

def find_from_wrook(move,to_square):
    fr = findCurrentPositions(board[move-1],"R")
    possible_pos1 = []
    for y in range(-7,8):
        possible_pos1.append((y,fr[0][0]))
    for x in range(-7,8):
        possible_pos1.append((fr[0][0],x))

    possible_pos2 = []
    for y in range(-7,8):
        possible_pos2.append((y,fr[1][0]))
    for x in range(-7,8):
        possible_pos2.append((fr[1][0],x))

    if to_square in possible_pos1:
        print(f"White Rook was in {fr[0]}")
    elif to_square in possible_pos2:
        print(f"White Rook was in {fr[1]}")
       
        
        
print('Start Game')
showBoard(board[0])

#first move
addMoveToBoard(1, 'P', (5,2), (5,4))
addMoveToBoard(2, 'p', (5,7), (5,5))

print('Move #1')
showBoard(board[1])

#second move
addMoveToBoard(3, 'N', (7,1), (6,3))
addMoveToBoard(4, 'n', (2,8), (3,6))

print('Move #2')
showBoard(board[2])

find_from_wking(4,(5,2))

find_from_wrook(4,(1,3))




