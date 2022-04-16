import os
import re

from model import PgnGame
from moves import move_to_board


def list_of_pgns(gamesdir):
    pgns = []
    for fn in os.listdir(gamesdir):
        if fn.endswith(".pgn"):
            pgns.append(os.path.join(gamesdir, fn))
    return pgns        

def games_in_pgn(fn):
    with open(fn, "r") as fp:
        txt = fp.read() 
    games = []
    games_txt = ["[Event " + x for x in re.split(r"\[Event\s", txt) if x.strip() !='']
    for game_txt in games_txt:
        game_txt = game_txt.replace("\n", " ").strip()
        event = re.search(r"\[Event\s+(.*?)\]", game_txt).group(1)
        white = re.search(r"\[White\s+(.*?)\]", game_txt).group(1)
        black = re.search(r"\[Black\s+(.*?)\]", game_txt).group(1)
        result = re.search(r"\[Result\s+(.*?)\]", game_txt).group(1)
        moves_txt= re.search(r"\]\s*(1.*)$", game_txt).group(1)
        moves = []
        # ΠΡΟΣΘΗΚΗ ΑΡΧΙΚΟΥ ΤΑΜΠΛΟ ΣΤΗΝ ΛΙΣΤΑ ΜΕ ΤΑ ΤΑΜΠΛΟ
        boards = ['rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR']
        for move, wsan, bsan in re.findall(r'(\d+)\.\s(\S+)\s+(\S+)', moves_txt):
            moves.append((move, wsan, bsan)) # οι κινήσεις ως τριάδες (αριθμός κίνησης, κίνηση λευκών, κίνηση μαύρων)
            boards.append(move_to_board(move, 'w', wsan)) # ΠΡΟΣΘΗΚΗ ΤΑΜΠΛΟ ΜΕ ΤΗΝ ΚΙΝΗΣΗ ΤΩΝ ΛΕΥΚΩΝ
            boards.append(move_to_board(move, 'b', bsan)) # ΠΡΟΣΘΗΚΗ ΤΑΜΠΛΟ ΜΕ ΤΗΝ ΚΙΝΗΣΗ ΤΩΝ ΜΑΥΡΩΝ
        game = PgnGame(event,white,black,result,moves,boards)
        games.append(game)
    return games



