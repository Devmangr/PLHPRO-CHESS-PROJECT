# παράδειγμα ανάγνωσης αρχείου pgn ως αρχείου κειμένου
# εντοπισμός πληροφοριών π.χ. παίκτες, κινήσεις
import re

class ChessGame:
    pass


the_game = ChessGame()
def findMoves(moves):
    # εύρεση πλήθους κινήσεων
    res1 = re.findall(r'(\d+)\.', moves)
    print(f'Πλήθος κινήσεων = {res1[-1]}')

    # απομόνωση κινήσεων
    for m, w, b in re.findall(r'(\d+)\.\s(\S+)\s+(\S+)', moves):
        print(f'{m} {w}, {b}')

with open("c:\chess\game.pgn", "r") as fp:
    in_moves_data = False
    moves = ""
    for line in fp:
        if line.strip() == "":
            continue
        if "white" in line.lower():
            the_game.white_player = line.split('"')[1]
        if "black" in line.lower():
            the_game.black_player = line.split('"')[1]
        if "[result" in line.lower():
            in_moves_data = True
            continue
        if in_moves_data:
            moves += line

print(f"White: {the_game.white_player}")
print(f"Black: {the_game.black_player}")
findMoves(moves)
