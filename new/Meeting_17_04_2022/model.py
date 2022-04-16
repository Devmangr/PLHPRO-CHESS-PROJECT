class PgnGame():
    def __init__(self, event, white, black, result, moves, boards):
        self.event = event
        self.white = white
        self.black = black
        self.result = result
        self.moves = moves
        self.boards = boards #ΠΡΟΣΘΗΚΗ ΟΛΩΝ ΤΩΝ ΤΑΜΠΛΟ
        
    def __str__(self):
        return f"{self.event} White: {self.white} Black: {self.black} Moves: {len(self.moves)} Result: {self.result}"
        