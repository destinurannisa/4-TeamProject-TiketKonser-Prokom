from ctypes import resize
import tkinter
import math
import sqlite3
import csv
import tkinter.messagebox
import os
from tkinter import *
import sys
import tkinter as tk
from turtle import width
from PIL import ImageTk, Image
import pandas as pd

window = Tk()
text = Text(window)

image = Image.open("stage.png")
#resize_image = image.resize((50,50))
img = ImageTk.PhotoImage(image)
poster = Label(window,image = img)
poster.image = img
poster.grid(column=0,row=0,sticky = "NW")
wrapper = LabelFrame(window)
wrapper.grid(column=0,row=1)

Button(wrapper, 
    bg="gold", 
    fg="navy", 
    text="VVIP", 
    command=print("Terclick"),
    width=10, 
    height=7).grid(column=0,row=0,padx=10)
Button(wrapper, 
    bg="silver", 
    fg="navy", 
    text="VIP", 
    command=print("Terclick"),
    width=10, 
    height=7).grid(column=1,row=0,padx=10)
Button(wrapper, 
    bg="green", 
    fg="navy", 
    text="A", 
    command=print("Terclick"),
    width=10, 
    height=7).grid(column=2,row=0,padx=10)
Button(wrapper, 
    bg="red", 
    fg="navy", 
    text="B", 
    command=print("Terclick"),
    width=10, 
    height=7).grid(column=3,row=0,padx=10)
Button(wrapper, 
    bg="light blue", 
    fg="navy", 
    text="C", 
    command=print("Terclick"),
    width=10, 
    height=7).grid(column=4,row=0,padx=10)

window.geometry("730x610")
window.resizable(False,False)
window.mainloop()
