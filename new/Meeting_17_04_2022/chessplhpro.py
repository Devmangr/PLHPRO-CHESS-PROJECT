from string import whitespace
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import filedialog as fd


# class for building and managing the game board
class GameBoard():
    def __init__ (self,appwindow,width,height):
            
        self.width = width
        self.height = height

        self.canvas = tk.Canvas(appwindow, borderwidth=0, highlightthickness=0,width=self.width*2, height=self.height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        

        #Build the board
        color1 = 'white'
        color2 = 'grey'
        color = color1
        offsetx= 20   #Where to start drawing of the board in x axis
        offsety = 20  #Where to start drawing of the board in y axis
        square_size = 70
        for row in range(0,8):
            color = color1 if color==color2 else color2
            for col in range (0,8):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = color1 if color==color2 else color2
        #test to place a pawn
        self.placepiece(1,2,square_size,'b_pawn') #Place piece in coordinates, square_size, piece type

    def placepiece(self,row,col,square_size,piece): 
        x = (col * square_size) + int(square_size / 2)
        y = (row * square_size) + int(square_size / 2)

        if piece == 'b_pawn':
            self.image_to_place = tk.PhotoImage(file='C:/EAP/project/icons/b_pawn.png')
        
        self.canvas.create_image(x,y, image=self.image_to_place, tags="piece" ,anchor="c")
       



#class for building and managing the application window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('PLH PRO CHESS')
        self.geometry('1000x565')
        self.resizable('false','false')
        self.create_menu()
        self.board = GameBoard(self,500,500)

    def create_menu(self):
        self.menubar = Menu(self)
        self.config(menu=self.menubar)
    
        self.file_menu = Menu(self.menubar)
        self.file_menu = Menu(self.menubar, tearoff=False)

        self.file_menu.add_command(label='Open',command=self.select_file)
        self.file_menu.add_command(label='Exit',command=self.destroy)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def select_file(self):
        '''Open a select file dialogbox and returns the name of the file'''
        filetypes = (('PGN files', '*.pgn'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        showinfo(title='Selected File',message=filename)


if __name__ == "__main__":
    app = App()
    app.mainloop()