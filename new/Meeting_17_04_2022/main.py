from utils import list_of_pgns, games_in_pgn
from moves import show_board

def user_demo():
    pgns = list_of_pgns("games")
    print(pgns)
    for i, pgn in enumerate(pgns):
        print(f"{i+1}. {pgn}")
    sel = input("Select pgn file: ")
    sel = int(sel) - 1
    
    games = games_in_pgn(pgns[sel])
    for i, game in enumerate(games):
        print(f"{i+1}. {game}")
    sel = input("Select game: ")
    sel = int(sel) - 1
    game = games[sel]
    print("GAME: ",  game)
    print("MOVES: ", game.moves)
    move_number = 1
    board_number =0
    for board in game.boards:
        if board_number == 0:
            print(f"Start Game")
            board_number += 1
        elif board_number % 2 != 0:
            print(f"Move #{move_number} - White")
            board_number += 1
        else:
            print(f"Move #{move_number} - Black")
            move_number += 1
            board_number += 1
        print(board)
        show_board(board)
        input("Press Enter to continue...")
    
if __name__=="__main__":
    user_demo()  
    
