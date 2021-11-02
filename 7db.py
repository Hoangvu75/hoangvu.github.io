from tkinter import *
from tkinter import font
from tkinter.font import BOLD, names
from typing import Sized
import random
import time
import pygame

score = 0

pygame.mixer.init()
def music():
    pygame.mixer.music.load("dbmusic.mp3")
    pygame.mixer.music.play(loops=100)   
def move_up(event) : 
    canvas.move(goku_canvas,0,-50)
def move_down(event) : 
    canvas.move(goku_canvas,0,50)
def frieza_appear() :
    listx = [500,600,700,800,900,1000,1100,1200,1300]
    listy = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850]
    frieza_canvas = canvas.create_image(listx[random.randint(0,8)],listy[random.randint(0,8)],image=frieza_image,tag="frieza")
    frieza_coords = canvas.coords(frieza_canvas)
    kame_canvas2 = canvas.create_image(frieza_coords[0],frieza_coords[1],image=yellowkame_image,tag="kame2")
    kame_coords2 = canvas.coords(kame_canvas2)
    window.update()
    
    def flying() :
        for i in range(37) :
            canvas.move(kame_canvas2,-50,0)
            window.update()
            kame_coords2[0] += -50
            window.after(20)
    flying()

    def kame(event) : 
        kame_canvas = canvas.create_image(x_goku,y_goku,image=kame_image,tag="kame")
        kame_coords = canvas.coords(kame_canvas)
        def flying() :
            global score
            for i in range(37) :
                canvas.move(kame_canvas,50,0)
                window.update()
                if kame_coords == frieza_coords :
                    canvas.delete("frieza")
                    score += 1
                    score_label.config(text="Score:{}".format(score))
                    window.after(500,cell_appear)
                kame_coords[0] += 50
                window.after(20)
        flying()
    window.bind("<o>",kame)
def cell_appear() :
    listy = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850]
    listx = [500,600,700,800,900,1000,1100,1200,1300]
    cell_canvas = canvas.create_image(listx[random.randint(0,8)],listy[random.randint(0,8)],image=cell_image,tag="cell")
    cell_coords = canvas.coords(cell_canvas)
    kame_canvas2 = canvas.create_image(cell_coords[0],cell_coords[1],image=yellowkame_image,tag="kame2")
    kame_coords2 = canvas.coords(kame_canvas2)
    window.update()
    
    def flying() :
        for i in range(37) :
            canvas.move(kame_canvas2,-50,0)
            window.update()
            kame_coords2[0] += -50
            window.after(20)
    flying()
    
    def kame(event) :  
        kame_canvas = canvas.create_image(x_goku,y_goku,image=kame_image,tag="kame")
        kame_coords = canvas.coords(kame_canvas)
        def flying() :
            global score
            for i in range(37) :
                canvas.move(kame_canvas,50,0)
                window.update()
                if kame_coords == cell_coords :
                    canvas.delete("cell")
                    score += 1
                    score_label.config(text="Score:{}".format(score))
                    window.after(500,buu_appear)
                kame_coords[0] += 50
                window.after(20)
        flying()
    window.bind("<o>",kame)
def buu_appear() :
    listy = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850]
    listx = [500,600,700,800,900,1000,1100,1200,1300]
    buu_canvas = canvas.create_image(listx[random.randint(0,8)],listy[random.randint(0,8)],image=buu_image,tag="buu")
    buu_coords = canvas.coords(buu_canvas)
    kame_canvas2 = canvas.create_image(buu_coords[0],buu_coords[1],image=yellowkame_image,tag="kame2")
    kame_coords2 = canvas.coords(kame_canvas2)
    window.update()
    
    def flying() :
        for i in range(37) :
            canvas.move(kame_canvas2,-50,0)
            window.update()
            kame_coords2[0] += -50
            window.after(20)
    flying()

    def kame(event) :  
        kame_canvas = canvas.create_image(x_goku,y_goku,image=kame_image,tag="kame")
        kame_coords = canvas.coords(kame_canvas)
        def flying() :
            global score
            for i in range(37) :
                canvas.move(kame_canvas,50,0)
                window.update()
                if kame_coords == buu_coords :
                    canvas.delete("buu")
                    score += 1
                    score_label.config(text="Score:{}".format(score))
                    window.after(500,frieza_appear)
                kame_coords[0] += 50
                window.after(20)
        flying()
    window.bind("<o>",kame)

window = Tk()
score_label = Label(window,text=f"score : {score}",font=("Arial",40))
score_label.pack()
canvas = Canvas(window,width=1920,height=1080)
canvas.pack()

bg_image = PhotoImage(file='bg.png')
background = canvas.create_image(0,0,image=bg_image,anchor=NW)

frieza_image = PhotoImage(file='frieza.png')
cell_image = PhotoImage(file='cell.png')
buu_image = PhotoImage(file='buu.png')

kame_image = PhotoImage(file='kamehameha.png')
yellowkame_image = PhotoImage(file='yellowkame.png')

window.bind("<w>",move_up)
window.bind("<s>",move_down)
goku_image = PhotoImage(file='goku.png')
goku_canvas = canvas.create_image(100,100,image=goku_image,tag="goku")

music()
frieza_appear()

while True :
    goku_coords = canvas.coords(goku_canvas)
    x_goku = goku_coords[0]
    y_goku = goku_coords[1]
    window.update()
    
window.mainloop()
