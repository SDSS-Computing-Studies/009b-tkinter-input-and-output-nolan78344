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
eoutput = StringVar()

def Display():
    ADJECTIVE = entry1.get()


    ADJECTIVE2 = entry2.get()


    NOUN = entry3.get()


    NOUN2 = entry4.get()


    PLURALNOUN = entry5.get()


    GAME = entry6.get()


    PLURALNOUN2 = entry7.get()


    VING = entry8.get()


    VING2 = entry9.get()


    PLURALNOUN3 = entry10.get()

    VING3 = entry11.get()


    NOUN3 = entry12.get()


    PLANT = entry13.get()


    BODY = entry14.get()


    PLACE = entry15.get()


    VING4 = entry16.get()


    ADJECTIVE3 = entry17.get()

    NUM = entry18.get()


    PLURALNOUN4 = entry19.get()


    story ="A vacation is when you take a trip to some" + ADJECTIVE + "\nplace with your" + ADJECTIVE2 + "\nfamily. Usually you go to some place that is near a/an"+ NOUN + "\nor up on a/an" + NOUN2 + "\n. A good vacation place is one where you can ride" + PLURALNOUN + "\nor play" +  GAME + "\nor go hunting for" + PLURALNOUN2 + ". I like to spend my time" + VING + "\n or" + VING2 + "\n. When parents go on a vacation, they spend their time eating three" + PLURALNOUN3 +"\n a day, and fathers play golf, and mothers sit around" + VING3 +".\n Last summer, my little brother fell in a/an" + NOUN3 + "\nand got poison" + PLANT + "\nall over his" + BODY +"\n. My family is going to go to (the)" + PLACE + "\n, and I will practice" +  VING4 + "\n. Parents need vacations more than kids because parents are always very" + ADJECTIVE3 + "\nand because they have to work" + NUM + "\nhours every day all year making enough" + PLURALNOUN4 + "\nto pay for the vacation."
    eoutput.set(story)


ADJECTIVE = StringVar()
ADJECTIVE.set("ADJECTIVE")

ADJECTIVE2 = StringVar()
ADJECTIVE2.set("ADJECTIVE")

ADJECTIVE3 = StringVar()
ADJECTIVE3.set("ADJECTIVE")

NOUN = StringVar()
NOUN.set("NOUN")

NOUN2 = StringVar()
NOUN2.set("NOUN")

PLURALNOUN = StringVar()
PLURALNOUN.set("PLURAL NOUN")


PLURALNOUN2 = StringVar()
PLURALNOUN2.set("PLURAL NOUN")

PLURALNOUN3 = StringVar()
PLURALNOUN3.set("PLURAL NOUN")

PLURALNOUN4 = StringVar()
PLURALNOUN4.set("PLURAL NOUN")

NOUN3 = StringVar()
NOUN3.set("NOUN")

GAME = StringVar()
GAME.set("GAME")

VING = StringVar()
VING.set("VERB ENDING IN “ING")

VING2 = StringVar()
VING2.set("VERB ENDING IN “ING")

VING3 = StringVar()
VING3.set("VERB ENDING IN “ING")

VING4 = StringVar()
VING4.set("VERB ENDING IN “ING")

PLANT = StringVar()
PLANT.set("PLANT")

PLACE = StringVar()
PLACE.set("A PLACE")

PLACE2 = StringVar()
PLACE2.set("A PLACE")

BODY = StringVar()
BODY.set("A BODY PART")

NUM = StringVar()
NUM.set("NUMBER")


lable1 = tk.Label(window, text="A vacation is when you take a trip to some")
entry1 = tk.Entry(window,width=10, textvariable=ADJECTIVE)
lable2 = tk.Label(window, text="Place with your")
entry2 = tk.Entry(window,width=10, textvariable=ADJECTIVE2)
lable3 = tk.Label(window, text="family. Usually you go to some place that is near a/an")
entry3 = tk.Entry(window,width=10, textvariable=NOUN)
lable4 = tk.Label(window, text="or up on a/an")
entry4 = tk.Entry(window,width=10, textvariable=NOUN2)
lable5 = tk.Label(window, text="A good vacation place is one where you can ride")
entry5 = tk.Entry(window,width=10, textvariable=PLURALNOUN)
lable6 = tk.Label(window, text="or play")
entry6 = tk.Entry(window,width=10, textvariable=GAME)
lable7 = tk.Label(window, text="or go hunting for")
entry7 = tk.Entry(window,width=10, textvariable=PLURALNOUN2)
lable8 = tk.Label(window, text="I like to spend my time")
entry8 = tk.Entry(window,width=10, textvariable=VING)
lable9 = tk.Label(window, text="or")
entry9 = tk.Entry(window,width=10, textvariable=VING2)
lable10 = tk.Label(window, text="When parents go on a vacation, they spend their time eating three")
entry10 = tk.Entry(window,width=10, textvariable=PLURALNOUN3)
lable11 = tk.Label(window, text="a day, and fathers play golf, and mothers sit around")
entry11 = tk.Entry(window,width=10, textvariable=VING3)
lable12 = tk.Label(window, text="Last summer, my little brother fell in a/an")
entry12 = tk.Entry(window,width=10, textvariable=NOUN3)
lable13 = tk.Label(window, text="and got poison")
entry13 = tk.Entry(window,width=10, textvariable=PLANT)
lable14 = tk.Label(window, text="all over his")
entry14 = tk.Entry(window,width=10, textvariable=BODY)
lable15 = tk.Label(window, text="My family is going to go to (the)")
entry15 = tk.Entry(window,width=10, textvariable=PLACE2)
lable16 = tk.Label(window, text=", and I will practice")
entry16 = tk.Entry(window,width=10, textvariable=VING4)
lable17 = tk.Label(window, text="Parents need vacations more than kids because parents are always very")
entry17 = tk.Entry(window,width=10, textvariable=ADJECTIVE3)
lable18 = tk.Label(window, text="and because they have to work")
entry18 = tk.Entry(window,width=10, textvariable=NUM)
lable19 = tk.Label(window, text="hours every day all year making enough")
entry19 = tk.Entry(window,width=10, textvariable=PLURALNOUN4)
lable20 = tk.Label(window, text="to pay for the vacation.")
b1 = Button(window, text="Click", command=Display)
f1=Label(window,textvariable=eoutput)


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

b1.grid(row=10, column=4)

f1.grid(row=11,column=1,columnspan=4)


window.mainloop()