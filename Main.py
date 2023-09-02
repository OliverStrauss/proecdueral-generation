import random
import tkinter as tk

class Array2DDisplayWindow:
    def __init__(self, array):
        self.array = array
        self.rows = len(array)
        self.cols = len(array[0])

        self.window = tk.Tk()
        self.window.title("2D Array Display")

        self.canvas = tk.Canvas(self.window, width=self.cols * 50, height=self.rows * 50)
        self.canvas.pack()

    def display(self):
        square_size = 50
        for i in range(self.rows):
            for j in range(self.cols):
                cell_value = self.array[i][j]
                x0 = j * square_size
                y0 = i * square_size
                x1 = x0 + square_size
                y1 = y0 + square_size

                # Color the squares based on the cell value
                if cell_value == 0:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")
                elif cell_value == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")

        self.window.mainloop()


cols = 15
rows = 30
board = [[0 for _ in range(cols)] for _ in range(rows)]
    
class pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def printboard():
    for row in board:
        print(row)


def inital(board):
    cell = random.randint(0,cols-1)
    cell =0
    board[rows-1][cell] = 1
    ipos = pos(rows-1,cell)
    print("hey" + str(ipos.getX()) + str(ipos.getY()))
    exit()
    return board


def otherRows(board):
    num = cols-2
    num = 1
    print(num)
    while(num>=0):
        flag = True
        i=0
        while(i<cols):
            usedints = []
            while(flag):
                val = random.randint(0,cols-1)
                val = 0
                
                if(val not in usedints):
                    spos = pos(val,num)
                    next(board,spos)
                    if(down(board,spos) or next(board,spos)):
                        i+=1
                        board[num][val] = 1
                        usedints.append(val)
                        
                    flag = False
                    
                    

                
                    
            flag = True
        num-=1
    #print(i)
    return board

def down(board,spos):
    #print(spos.getY(),spos.getX())
    printboard()
    print(spos.getY()+1,spos.getX())
    print(board[rows-1][0])
    print(board[spos.getY()+1][spos.getX()])
    if(board[spos.getY()+1][spos.getX()] == 1):
        print("pee")
        return True
    
def next(board,spos):
    if(spos.getX()+1<4 and spos.getX()-1>-1):
        if(board[spos.getY()][spos.getX()+1] or board[spos.getY()][spos.getX()-1] == 1):
            return True






array_display = Array2DDisplayWindow(board)
inital(board)
otherRows(board)
printboard()
array_display.display()




    