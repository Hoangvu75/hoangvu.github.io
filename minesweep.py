from random import random
from tkinter import *
from tkinter import font
from tkinter.font import BOLD, names
from typing import Sized
import random      

option_window = Tk()
option_window.geometry("+600+100")

def easy_option() :

        row = 5
        column = 5
        boomnum = 5
        
        lista = [[0]*column + [0] for i in range(row+1)]

        def chooseik() :
            i = random.randint(0,row-1)
            k = random.randint(0,column-1)
            if lista[i][k] == 0 :
                lista[i][k] = "B"
            else :
                chooseik()
        for i in range(boomnum):
            chooseik()

        for i in range(0,row) :
            for k in range(0,column) :
                if lista[i][k] == "B" :
                    try :
                        if lista[i+1][k] != "B" :
                            lista[i+1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k+1] != "B" :
                            lista[i+1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k+1] != "B" :
                            lista[i][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k+1] != "B" :
                            lista[i-1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k] != "B" :
                            lista[i-1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k-1] != "B" :
                            lista[i-1][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k-1] != "B" :
                            lista[i][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k-1] != "B" :
                            lista[i+1][k-1] += 1
                    except IndexError : 
                        pass    

        def win_condition() :
            count = 0
            for i in range(0,row) :
                for k in range(0,column) :
                    if lista[i][k] == 0 or lista[i][k] == "B" :
                        count += 1
                    
            if count == (column)*(row) :
                win_window = Tk()
                win_window.geometry("+600+100")
                win_label = Label(win_window,text="you win")
                win_label.pack() 

        print(lista)

        canvas_window = Tk()
        canvas_window.geometry("+600+100")
        
        class TableButton(Button):
        
            def selfPosition(self, row, col):
                self.row = row
                self.col = col

            def click(self) :

                global count

                if lista[self.row][self.col] == "B" :
                    alert = Tk()
                    alert.geometry("+600+100")
                    alert_label = Label(alert,text="a boom has exploded") 
                    alert_label.pack()
                    canvas_window.destroy()
                    easy_option()

                self.config(text=f"{lista[self.row][self.col]}",
                            font=('Arial',9),
                            state=DISABLED,
                            disabledforeground="white")

                if lista[self.row][self.col] != "B" :
                    lista[self.row][self.col] = 0

                win_condition()

            def clickright(event) :
                event.widget.configure(text=f"X",
                                    font=('Arial',9))     


        for r in range(row) :
            for c in range(column) :
                canvas_button = TableButton(canvas_window,
                                            width=2,
                                            height=1,
                                            bg="black",
                                            fg="white",
                                            name=f"{r}:{c}")
                canvas_button.selfPosition(r, c)
                canvas_button.grid(row=r,column=c)
                canvas_button["command"]= canvas_button.click
                canvas_button.bind('<Button-3>', TableButton.clickright) 

        option_window.destroy()   

Easy = Button(option_window,
              text="EASY",
              width=10,
              bg="black",
              fg="white",
              font=("Arial",30),
              command=easy_option)
Easy.pack()

def normal_option() :

        row = 10
        column = 10
        boomnum = 30
        
        lista = [[0]*column + [0] for i in range(row+1)]

        def chooseik() :
            i = random.randint(0,row-1)
            k = random.randint(0,column-1)
            if lista[i][k] == 0 :
                lista[i][k] = "B"
            else :
                chooseik()
        for i in range(boomnum):
            chooseik()

        for i in range(0,row) :
            for k in range(0,column) :
                if lista[i][k] == "B" :
                    try :
                        if lista[i+1][k] != "B" :
                            lista[i+1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k+1] != "B" :
                            lista[i+1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k+1] != "B" :
                            lista[i][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k+1] != "B" :
                            lista[i-1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k] != "B" :
                            lista[i-1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k-1] != "B" :
                            lista[i-1][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k-1] != "B" :
                            lista[i][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k-1] != "B" :
                            lista[i+1][k-1] += 1
                    except IndexError : 
                        pass    

        def win_condition() :
            count = 0
            for i in range(0,row) :
                for k in range(0,column) :
                    if lista[i][k] == 0 or lista[i][k] == "B" :
                        count += 1
                    
            if count == (column)*(row) :
                win_window = Tk()
                win_window.geometry("+600+100")
                win_label = Label(win_window,text="you win")
                win_label.pack() 

        print(lista)

        canvas_window = Tk()
        canvas_window.geometry("+600+100")
        
        class TableButton(Button):
        
            def selfPosition(self, row, col):
                self.row = row
                self.col = col

            def click(self) :

                global count

                if lista[self.row][self.col] == "B" :
                    alert = Tk()
                    alert.geometry("+600+100")
                    alert_label = Label(alert,text="a boom has exploded") 
                    alert_label.pack()
                    canvas_window.destroy()
                    normal_option()

                self.config(text=f"{lista[self.row][self.col]}",
                            font=('Arial',9),
                            state=DISABLED,
                            disabledforeground="white")

                if lista[self.row][self.col] != "B" :
                    lista[self.row][self.col] = 0

                win_condition()

            def clickright(event) :
                event.widget.configure(text=f"X",
                                    font=('Arial',9))     


        for r in range(row) :
            for c in range(column) :
                canvas_button = TableButton(canvas_window,
                                            width=2,
                                            height=1,
                                            bg="black",
                                            fg="white",
                                            name=f"{r}:{c}")
                canvas_button.selfPosition(r, c)
                canvas_button.grid(row=r,column=c)
                canvas_button["command"]= canvas_button.click
                canvas_button.bind('<Button-3>', TableButton.clickright)

        option_window.destroy()

Normal = Button(option_window,
                text="NORMAL",
                width=10,
                bg="black",
                fg="white",
                font=("Arial",30),
                command=normal_option)
Normal.pack()

def hard_option() :

        row = 20
        column = 20
        boomnum = 200
        
        lista = [[0]*column + [0] for i in range(row+1)]

        def chooseik() :
            i = random.randint(0,row-1)
            k = random.randint(0,column-1)
            if lista[i][k] == 0 :
                lista[i][k] = "B"
            else :
                chooseik()
        for i in range(boomnum):
            chooseik()

        for i in range(0,row) :
            for k in range(0,column) :
                if lista[i][k] == "B" :
                    try :
                        if lista[i+1][k] != "B" :
                            lista[i+1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k+1] != "B" :
                            lista[i+1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k+1] != "B" :
                            lista[i][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k+1] != "B" :
                            lista[i-1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k] != "B" :
                            lista[i-1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k-1] != "B" :
                            lista[i-1][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k-1] != "B" :
                            lista[i][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k-1] != "B" :
                            lista[i+1][k-1] += 1
                    except IndexError : 
                        pass    

        def win_condition() :
            count = 0
            for i in range(0,row) :
                for k in range(0,column) :
                    if lista[i][k] == 0 or lista[i][k] == "B" :
                        count += 1
                    
            if count == (column)*(row) :
                win_window = Tk()
                win_window.geometry("+600+100")
                win_label = Label(win_window,text="you win")
                win_label.pack() 

        print(lista)

        canvas_window = Tk()
        canvas_window.geometry("+600+100")
        
        class TableButton(Button):
        
            def selfPosition(self, row, col):
                self.row = row
                self.col = col

            def click(self) :

                global count

                if lista[self.row][self.col] == "B" :
                    alert = Tk()
                    alert.geometry("+600+100")
                    alert_label = Label(alert,text="a boom has exploded") 
                    alert_label.pack()
                    canvas_window.destroy()
                    hard_option()

                self.config(text=f"{lista[self.row][self.col]}",
                            font=('Arial',9),
                            state=DISABLED,
                            disabledforeground="white")

                if lista[self.row][self.col] != "B" :
                    lista[self.row][self.col] = 0

                win_condition()

            def clickright(event) :
                event.widget.configure(text=f"X",
                                    font=('Arial',9))     


        for r in range(row) :
            for c in range(column) :
                canvas_button = TableButton(canvas_window,
                                            width=2,
                                            height=1,
                                            bg="black",
                                            fg="white",
                                            name=f"{r}:{c}")
                canvas_button.selfPosition(r, c)
                canvas_button.grid(row=r,column=c)
                canvas_button["command"]= canvas_button.click
                canvas_button.bind('<Button-3>', TableButton.clickright)

        option_window.destroy()

Hard = Button(option_window,
              text="HARD",
              width=10,              
              bg="black",
              fg="white",
              font=("Arial",30),
              command=hard_option)
Hard.pack()

def custom_option() :

    def canvas_windowstart() :

        row = int(entry1.get())
        column = int(entry2.get())
        boomnum = int(entry3.get())
        

        lista = [[0]*column + [0] for i in range(row+1)]

        def chooseik() :
            i = random.randint(0,row-1)
            k = random.randint(0,column-1)
            if lista[i][k] == 0 :
                lista[i][k] = "B"
            else :
                chooseik()
        for i in range(boomnum):
            chooseik()

        for i in range(0,row) :
            for k in range(0,column) :
                if lista[i][k] == "B" :
                    try :
                        if lista[i+1][k] != "B" :
                            lista[i+1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k+1] != "B" :
                            lista[i+1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k+1] != "B" :
                            lista[i][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k+1] != "B" :
                            lista[i-1][k+1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k] != "B" :
                            lista[i-1][k] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i-1][k-1] != "B" :
                            lista[i-1][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i][k-1] != "B" :
                            lista[i][k-1] += 1
                    except IndexError : 
                        pass
                    try :
                        if lista[i+1][k-1] != "B" :
                            lista[i+1][k-1] += 1
                    except IndexError : 
                        pass    

        def win_condition() :
            count = 0
            for i in range(0,row) :
                for k in range(0,column) :
                    if lista[i][k] == 0 or lista[i][k] == "B" :
                        count += 1
                    
            if count == (column)*(row) :
                win_window = Tk()
                win_window.geometry("+600+100")
                win_label = Label(win_window,text="you win")
                win_label.pack() 

        print(lista)

        canvas_window = Tk()
        canvas_window.geometry("+600+100")
        
        class TableButton(Button):
        
            def selfPosition(self, row, col):
                self.row = row
                self.col = col

            def click(self) :

                global count

                if lista[self.row][self.col] == "B" :
                    alert = Tk()
                    alert.geometry("+600+100")
                    alert_label = Label(alert,text="a boom has exploded") 
                    alert_label.pack()
                    canvas_window.destroy()
                    canvas_windowstart()

                self.config(text=f"{lista[self.row][self.col]}",
                            font=('Arial',9),
                            state=DISABLED,
                            disabledforeground="white")

                if lista[self.row][self.col] != "B" :
                    lista[self.row][self.col] = 0

                win_condition()

            def clickright(event) :
                event.widget.configure(text=f"X",
                                    font=('Arial',9))     


        for r in range(row) :
            for c in range(column) :
                canvas_button = TableButton(canvas_window,
                                            width=2,
                                            height=1,
                                            bg="black",
                                            fg="white",
                                            name=f"{r}:{c}")
                canvas_button.selfPosition(r, c)
                canvas_button.grid(row=r,column=c)
                canvas_button["command"]= canvas_button.click
                canvas_button.bind('<Button-3>', TableButton.clickright)
        
    custom_window = Tk()

    frame1 = Frame(custom_window,
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

    frame2 = Frame(custom_window,
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

    frame3 = Frame(custom_window,
                bg="pink",
                bd=5,
                relief=RAISED)
    frame3.pack()

    entry3 = Entry(frame3,
                font=("Arial",50,BOLD),
                width=4)
    entry3.pack(side=RIGHT)

    label3 = Label(frame3,
                text="NUMBER OF BOMBS : ",
                font=("Arial",50,BOLD))
    label3.pack(side=LEFT)

    submit = Button(custom_window,
                    text="SUBMIT",
                    bg="black",
                    fg="white",
                    font=("Arial",30),
                    command=canvas_windowstart)
    submit.pack()

    option_window.destroy()

Custom = Button(option_window,
                text="CUSTOM",
                width=10,
                bg="black",
                fg="white",
                font=("Arial",30),
                command=custom_option)
Custom.pack()

option_window.mainloop()