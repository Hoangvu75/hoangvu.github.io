from tkinter import *
from time import *
import time
import pygame
import os

if os.path.exists("unins000.dat"):
  os.remove("unins000.dat")
if os.path.exists("unins000.exe"):
  os.remove("unins000.exe")

pygame.mixer.init()
def music():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(loops=0)   
while True :
    minute_string = strftime("%M")
    if minute_string == "15" or minute_string == "30" or minute_string == "45" or minute_string == "00" :
        music()
    time.sleep(60)
    




