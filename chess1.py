import re

class ChessGame:
    def __init__(self,game_no,game_event,game_date,white_player,black_player,game_result,game_moves):
        self.number = game_no
        self.event = game_event
        self.date = game_date
        self.white = white_player
        self.black = black_player
        self.result = game_result
        self.moves = game_moves
        
    def __str__(self):
        return f"Game No:{self.number:5d}\nEvent:{self.event:20s}\nDate:{self.date:10s}\nWhite Player:{self.white:10s}\nBlack Player:{self.black:10s}\nGame Result:{self.result:10s}\nMoves:{self.moves}\n"
class Control:
    games_dict = {}
    def __init__(self):
        self.findMoves()
    def show_games(self):
        for id, info in Control.games_dict.items():
            no = id
            event=info['event']
            white=info['white']
            black=info['black']
            date = info['date']
            result = info['result']
            moves = info['moves']
            s = ChessGame(no,event,date,white,black,result,moves)
            print(s)
    def findMoves(self):
        with open("C:\chess\WijkaanZee2022.pgn", "r") as fp:
            in_moves_data = False
            moves = ""
            self.whitep, self.black_player, self.date, self.event = "","","",""
            j=0 #ΕΛΕΓΧΟΣ ΟΤΑΝ J=2 ΑΛΛΑΖΕΙ ΤΟ ΠΑΙΧΝΙΔΙ
            no = 1 #ΜΕΤΡΗΤΗΣ ΓΙΑ ΤΟΝ ΑΡΙΘΜΟ ΠΑΙΧΝΙΔΙΩΝ 
            for line in fp:
                if line.strip() == "":
                    j+=1
                    continue
                if j == 2:
                    j = 0
                    in_moves_data = False
####  Προσθήκη λεξικού με moves στο games_dict
                    moves_dict = Control.movesDict(moves)
                    Control.games_dict[no] = {'event':self.event,'date':self.date,'white':self.whitep.replace(",",""),
                                                'black':self.black_player.replace(",",""),'result':self.res,'moves':moves_dict}
                    no += 1
                    self.show_games()
                    moves = ""
                if re.findall('\[Event."',line):
                    self.event = line.split('"')[1]
                if re.findall('\[White."',line):
                    self.whitep = line.split('"')[1]
                if re.findall('\[Black."',line):
                    self.black_player = line.split('"')[1]
                if re.findall('\[Date."',line):
                    self.date = line.split('"')[1]
                if re.findall('\[Result."',line):
                    self.res = line.split('"')[1]
                    in_moves_data = True
                    continue
                if in_moves_data and j==1:
                    moves += line

### Δημιουργία λεξικού απο κείμενο moves
    def movesDict(self):
        moves_dict = {}
        for m, w, b in re.findall(r'(\d+)\.\s(\S+)\s+(\S+)', self): #Έυρεση κινήσεων
            if b[0] in ('0','1'): #Αν η δεύτερη κίνηση είναι Result τότε μόνο η κίνηση των λευκών να καταγραφεί ως κίνηση
                moves_dict[m] = [w]
            else:
                moves_dict[m] = [w, b]
        for m, c in re.findall(r'(\d+)\.\s\S+\s+\S+\s\{(.+)\}', self):#Έυρεση σχολίων της κίνησης και προσθήκη στην συγκεκριμένη κίνηση
            moves_dict[m] = moves_dict.get(m) + [c]
        return(moves_dict)



if __name__ == "__main__":
    Control()