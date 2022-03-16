#Δημιουργία λεξικού με το ταμπλό της έναρξης
board = {0: {'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B',
'g1': 'N', 'h1': 'R','a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P',
'f2': 'P', 'g2': 'P', 'h2': 'P', 'a3': '.', '3b': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.',
'g3': '.', 'h3': '.', 'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
'a8': 'r', 'b8': 'n', 'c8': 'b' , 'd8': 'q', 'e8': 'k', 'f8': 'b',
'g8': 'n','h8': 'r'}}

#Εμφάνιση ταμπλό
def showBoard(board):
    print(f"{board['a8']:1s} {board['b8']:1s} {board['c8']:1s} {board['d8']:1s} {board['e8']:1s} {board['f8']:1s} {board['g8']:1s} {board['h8']:1s}")
    print(f"{board['a7']:1s} {board['b7']:1s} {board['c7']:1s} {board['d7']:1s} {board['e7']:1s} {board['f7']:1s} {board['g7']:1s} {board['h7']:1s}")
    print(f"{board['a6']:1s} {board['b6']:1s} {board['c6']:1s} {board['d6']:1s} {board['e6']:1s} {board['f6']:1s} {board['g6']:1s} {board['h6']:1s}")
    print(f"{board['a5']:1s} {board['b5']:1s} {board['c5']:1s} {board['d5']:1s} {board['e5']:1s} {board['f5']:1s} {board['g5']:1s} {board['h5']:1s}")
    print(f"{board['a4']:1s} {board['b4']:1s} {board['c4']:1s} {board['d4']:1s} {board['e4']:1s} {board['f4']:1s} {board['g4']:1s} {board['h4']:1s}")
    print(f"{board['a3']:1s} {board['3b']:1s} {board['c3']:1s} {board['d3']:1s} {board['e3']:1s} {board['f3']:1s} {board['g3']:1s} {board['h3']:1s}")
    print(f"{board['a2']:1s} {board['b2']:1s} {board['c2']:1s} {board['d2']:1s} {board['e2']:1s} {board['f2']:1s} {board['g2']:1s} {board['h2']:1s}")    
    print(f"{board['a1']:1s} {board['b1']:1s} {board['c1']:1s} {board['d1']:1s} {board['e1']:1s} {board['f1']:1s} {board['g1']:1s} {board['h1']:1s}")
    print()

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
    print(f'{check_piece} -> {positions}')


print('Start Game')
showBoard(board[0])

#first move
addMoveToBoard(1, 'P', 'e2', 'e4')
addMoveToBoard(2, 'p', 'e7', 'e5')

print('#1 Move')
showBoard(board[1])

#second move
addMoveToBoard(3, 'N', 'g1', 'f3')
addMoveToBoard(4, 'n', 'b8', 'c6')

print('#2 Move')
showBoard(board[2])

findCurrentPositions(board[2],"N")




