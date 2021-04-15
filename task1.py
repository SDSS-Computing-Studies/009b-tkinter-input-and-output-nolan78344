"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()

def Display():
    d1 = e1.get()
    
    entry1.delete(0,END)
    entry1.insert(0,d1)

    d2 = e2.get()
    
    entry2.delete(0,END)
    entry2.insert(0,d2)

    d3 = e3.get()
    
    entry3.delete(0,END)
    entry3.insert(0,d3)

    d4 = e4.get()
    
    entry4.delete(0,END)
    entry4.insert(0,d4)

    d5 = e5.get()
    
    entry5.delete(0,END)
    entry5.insert(0,d5)

    d6 = e6.get()
    
    entry6.delete(0,END)
    entry6.insert(0,d6)

    d7 = e7.get()
    
    entry7.delete(0,END)
    entry7.insert(0,d7)

    d8 = e8.get()
    
    entry8.delete(0,END)
    entry8.insert(0,d8)

    d9 = e9.get()
    
    entry9.delete(0,END)
    entry9.insert(0,d9)

    d10 = e10.get()
    
    entry10.delete(0,END)
    entry10.insert(0,d10)

    d11 = e11.get()
    
    entry11.delete(0,END)
    entry11.insert(0,d11)

e1 = Entry(window, width = 15)
e2 = Entry(window, width = 15)
e3 = Entry(window, width = 15)
e4 = Entry(window, width = 15)
e5 = Entry(window, width = 15)
e6 = Entry(window, width = 15)
e7 = Entry(window, width = 15)
e8 = Entry(window, width = 15)
e9 = Entry(window, width = 15)
e10 = Entry(window, width = 15)
e11 = Entry(window, width = 15)

ADJECTIVE = StringVar()
ADJECTIVE.set("ADJECTIVE")

NOUN = StringVar()
NOUN.set("NOUN")

PLURALNOUN = StringVar()
PLURALNOUN.set("PLURAL NOUN")

NOUN = StringVar()
NOUN.set("NOUN")

GAME = StringVar()
GAME.set("GAME")

VING = StringVar()
VING.set("VERB ENDING IN “ING")

PLANT = StringVar()
PLANT.set("PLANT")

PLACE = StringVar()
PLACE.set("A PLACE")

BODY = StringVar()
BODY.set("A BODY PART")

NUM = StringVar()
NUM.set("NUMBER")

lable1 = tk.Label(window, text="A vacation is when you take a trip to some")
entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=ADJECTIVE)
lable2 = tk.Label(window, text="Place with your")
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=ADJECTIVE)
lable3 = tk.Label(window, text="family. Usually you go to some place that is near a/an")
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=NOUN)
lable4 = tk.Label(window, text="or up on a/an")
entry4 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=NOUN)
lable5 = tk.Label(window, text="A good vacation place is one where you can ride")
entry5 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=PLURALNOUN)
lable6 = tk.Label(window, text="or play")
entry6 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=GAME)
lable7 = tk.Label(window, text="or go hunting for")
entry7 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=PLURALNOUN)
lable8 = tk.Label(window, text="I like to spend my time")
entry8 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=VING)
lable9 = tk.Label(window, text="or")
entry9 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=VING)
lable10 = tk.Label(window, text="When parents go on a vacation, they spend their time eating three")
entry10 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=PLURALNOUN)
lable11 = tk.Label(window, text="a day, and fathers play golf, and mothers sit around")
entry11 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=VING)
lable12 = tk.Label(window, text="Last summer, my little brother fell in a/an")
entry12 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=NOUN)
lable13 = tk.Label(window, text="and got poison")
entry13 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=PLANT)
lable14 = tk.Label(window, text="all over his")
entry14 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=BODY)
lable15 = tk.Label(window, text="My family is going to go to (the)")
entry15 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=PLACE)
lable16 = tk.Label(window, text=", and I will practice")
entry16 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=VING)
lable17 = tk.Label(window, text="Parents need vacations more than kids because parents are always very")
entry17 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=ADJECTIVE)
lable18 = tk.Label(window, text="and because they have to work")
entry18 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=NUM)
lable19 = tk.Label(window, text="hours every day all year making enough")
entry19 = tk.Entry(window,text="Entry widgets can be typed in", width=10, textvariable=PLURALNOUN)
lable20 = tk.Label(window, text="to pay for the vacation.")


lable1.grid(row = 1, column = 1)

entry1.grid(row = 1, column = 2)

lable2.grid(row = 1, column = 3)

entry2.grid(row = 1, column = 4)

lable3.grid(row = 2, column = 1)

entry3.grid(row = 2, column = 2)

lable4.grid(row = 2, column = 3)

entry4.grid(row = 2, column = 4)

lable5.grid(row = 3, column = 1)

entry5.grid(row = 3, column = 2)

lable6.grid(row = 3, column = 3)

entry6.grid(row = 3, column = 4)

lable7.grid(row = 4, column = 1)

entry7.grid(row = 4, column = 2)

lable8.grid(row = 4, column = 3)

entry8.grid(row = 4, column = 4)

lable9.grid(row = 5, column = 1)

entry9.grid(row = 5, column = 2)

lable10.grid(row = 5, column = 3)

entry10.grid(row = 5, column = 4)

lable11.grid(row = 6, column = 1)

entry11.grid(row = 6, column = 2)

lable12.grid(row = 6, column = 3)

entry12.grid(row = 6, column = 4)

lable13.grid(row = 7, column = 1)

entry13.grid(row = 7, column = 2)

lable14.grid(row = 7, column = 3)

entry14.grid(row = 7, column = 4)

lable15.grid(row = 8, column = 1)

entry15.grid(row = 8, column = 2)

lable16.grid(row = 8, column = 3)

entry16.grid(row = 8, column = 4)

lable17.grid(row = 9, column = 1)

entry17.grid(row = 9, column = 2)

lable18.grid(row = 9, column = 3)

entry18.grid(row = 9, column = 4)

lable19.grid(row = 10, column = 1)

entry19.grid(row = 10, column = 2)

lable20.grid(row = 10, column = 3)

b1 = Button(window, text="Click", command=Display)



window.mainloop()