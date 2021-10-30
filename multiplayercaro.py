from tkinter import *
from tkinter import font
from tkinter.font import BOLD, names
from typing import Sized

count = 1

def rc_multi():

    rc_window = Tk()
    rc_window.geometry("+600+100")

    def multiple_window():

        row = int(entry1.get())
        column = int(entry2.get())

        lista = []
        lista = [[0]*column*2 for i in range(row*2)]

        new_window = Tk()
        new_window.geometry("+600+100")

        if row<10 or column<10:
            alert_window = Tk()
            alert_window.geometry("+600+100")
            alert_label = Label(alert_window,text="PLEASE LET ROW>=10 AND COLUMN>=10")
            alert_label.pack()
            new_window.destroy()

        class TableButton(Button):

            def selfPosition(self, row, col):

                self.row = row
                self.col = col  

            def click(self):

                global count

                if count%2==0 :
                    self.config(text="X",
                                font=('Arial',9),
                                state=DISABLED,
                                disabledforeground="white")
                    lista[self.row-1][self.col-1] = "X"

                if count%2==1 :
                    self.config(text="O",
                                font=('Arial',9),
                                state=DISABLED,
                                disabledforeground="white")
                    lista[self.row-1][self.col-1] = "O"

                count = count + 1
                
                listXO = ["X","O"]

                def endingfunc():
                    win_window = Tk()
                    win_label = Label(win_window,text=f"{t} win") 
                    win_label.pack()
                    win_window.geometry("+600+100")
                    new_window.destroy()
                
                
                for i in range(0,row):
                    for k in range(0,column):
                        for t in listXO:
                            try :
                                if lista[i][k] == lista[i+1][k+1] == lista[i+2][k+2] == lista[i+3][k+3] == lista[i+4][k+4] == t :
                                    if lista[i-1][k-1] == lista[i+5][k+5] != 0 and lista[i-1][k-1] != lista[i][k] :
                                        pass
                                    else : 
                                        endingfunc()
                            except IndexError : 
                                pass
                

                for i in range(0,row):
                    for k in range(0,column):
                        for t in listXO:
                            try :
                                if lista[i][k] == lista[i][k+1] == lista[i][k+2] == lista[i][k+3] == lista[i][k+4] == t :
                                    if lista[i][k-1] == lista[i][k+5] != 0 and lista[i][k-1] != lista[i][k] :
                                        pass 
                                    else:
                                        endingfunc()
                            except IndexError : 
                                pass

                for i in range(0,row):
                    for k in range(0,column):
                        for t in listXO:
                            try :
                                if lista[i][k] == lista[i+1][k] == lista[i+2][k] == lista[i+3][k] == lista[i+4][k] == t :
                                    if lista[i-1][k] == lista[i+5][k] != 0 and lista[i-1][k] != lista[i][k] :
                                        pass
                                    else : 
                                        endingfunc()
                            except IndexError : 
                                pass

                for i in range(0,row):
                    for k in range(0,column):
                        for t in listXO:
                            try :
                                if lista[i][k] == lista[i-1][k+1] == lista[i-2][k+2] == lista[i-3][k+3] == lista[i-4][k+4] == t : 
                                    if lista[i+1][k-1] == lista[i-5][k+5] != 0 and lista[i+1][k-1] != lista[i][k] :
                                        pass
                                    else :
                                        endingfunc()
                            except IndexError : 
                                pass

        for c in range(1,column+1):
            for r in range(1,row+1):
                button = TableButton(new_window,
                                     width=2,
                                     height=1,
                                     bg="black",
                                     fg="red",
                                     name=f"{r}:{c}")
                button.grid(row=r,column=c)
                button.selfPosition(r, c)
                button["command"]= button.click

        rc_window.destroy()

    frame1 = Frame(rc_window,
                   bg="pink",
                   bd=5,
                   relief=RAISED)
    frame1.pack()

    entry1 = Entry(frame1,
                   font=("Arial",50,BOLD),
                   width=4)
    entry1.pack(side=RIGHT)

    label1 = Label(frame1,
                   text="ROW : ",
                   font=("Arial",50,BOLD))
    label1.pack(side=LEFT)

    frame2 = Frame(rc_window,
                   bg="pink",
                   bd=5,
                   relief=RAISED)
    frame2.pack()

    entry2 = Entry(frame2,
                   font=("Arial",50,BOLD),
                   width=4)
    entry2.pack(side=RIGHT)

    label2 = Label(frame2,
                   text="COLUMN : ",
                   font=("Arial",50,BOLD))
    label2.pack(side=LEFT)

    submit = Button(rc_window,
                    text="SUBMIT",
                    bg="black",
                    fg="white",
                    font=("Arial",30),
                    command=multiple_window)
    submit.pack()

    old_window.destroy()

h = 1
while h == 1 :
    old_window = Tk()

    multiple_player = Button(old_window,
                             text="MULTIPLE PLAYERS",
                             font=('Arial',20),
                             command=rc_multi,
                             bg="black",
                             fg="white",
                             width=20,
                             height=5)
    multiple_player.pack()

    def closegame():
        global h
        h = h+1
        old_window.destroy()

    close_game = Button(old_window,
                        text="CLOSE",
                        font=('Arial',20),
                        bg="black",
                        fg="white",
                        width=20,
                        height=5,
                        command=closegame)
    close_game.pack()

    old_window.geometry("+600+100")

    old_window.mainloop()