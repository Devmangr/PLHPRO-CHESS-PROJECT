import re

file = ['a', 'b', 'c', 'd', 'e', 'f' ,'g' ,'h']
rank = ['8', '7', '6', '5', '4', '3', '2', '1']

moves_board = ['rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR']

def find_file_rank(piece, to_square):
    x = 'a1'
    return x

def find_file(piece, rank):
    x = 'a'
    return x

def find_rank(piece, file):
    x = '1'
    return x
    
#Μετατροπή SAN σε LAN
#SAN = Short Algebraic Notation
#LAN = Long Algebraic Notation
def san_to_lan(move, team, san):
    lan = {}
    if san[0] in ('K', 'Q', 'R', 'B', 'N'):
        if team == 'w': lan['p'] = san[0]
        else: lan['p'] = san[0].lower()
        if 'x' in san: # Qxe4
            lan['t'] = san[san.index('x')+1] + san[san.index('x')+2]
            if san.index('x') == 3:
               lan['f'] = san[1] + san[2]
            elif san.index('x') == 2:
                if san[1] in file:
                    lan['f'] = san[1] + find_rank(san[0], san[1])
                else:
                    lan['f'] = find_file(san[0], san[1]) + san[1]
            else:
                lan['f'] = find_file_rank(san[0], lan['t'])
        else:
            if len(san) == 3 or (len(san) == 4 and san[-1] in ('+', '#')):     # Qe4 Qe4+
                lan['t'] = san[1] + san[2]
                lan['f'] = find_file_rank(san[0], lan['t'])
            else:
                if len(san) >= 4:     # Q1e4 Qae4 Qa1e4 Qa1e4+
                    if san[1] in file and san[2] in rank:
                        lan['f'] = san[1] + san[2]
                        lan['t'] = san[3] + san[4]
                    elif san[1] in file:
                        lan['f'] = san[1] + find_rank(san[0], san[1])
                        lan['t'] = san[2] + san[3]
                    else:
                        lan['f'] = find_file(san[0], san[1]) + san[1]
                        lan['t'] = san[2] + san[3]
    else:
        lan['f'] = 'a1'
        lan['t'] = 'a3'
    
    return lan['f'] + lan['t']


#Εύρεση θέσης LAN σε ταμπλό
def find_pos(lan):
    pos=''
    for f in file:
        for r in rank:
            fr = f + r
            if fr == lan:
                pos = str(rank.index(r)) + str(file.index(f))
            else:
                pos = '11'
    return pos
    
#Μετατροπή LAN σε ταμπλό
def convert_to_board(lan):
    if len(moves_board) == 1:
        movelist = list(map(list,moves_board[0].split('/')))
    else:
        movelist = list(map(list,moves_board[-1].split('/')))
    pfrom = find_pos(lan[:2])
    pto = find_pos(lan[2:])
    movelist[int(pto[0])][int(pto[1])] = movelist[int(pfrom[0])][int(pfrom[1])]
    movelist[int(pfrom[0])][int(pfrom[1])] = '.'
    board_str = ''
    for rank in movelist:
        for file in rank:
            board_str += file
        board_str += '/'
    moves_board.append(board_str[:-1])
    return board_str[:-1]

#Μετατροπή SAN κίνησης και εισαγωγή σε ταμπλό
def move_to_board(move, team, san):
    lan = san_to_lan(move, team, san)
    board_str = convert_to_board(lan)
    return board_str

#Εμφάνιση ταμπλό
def show_board(move):
    rows = move.split('/')
    for rank in range(8):
        for file in range(8):
            print(f"{rows[rank][file]:2s}", end='')
        print('')
    print('')

