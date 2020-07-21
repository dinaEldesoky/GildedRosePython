from tkinter import *
from item import Item


class GildedRose(object):

    def __init__(self, items):
        self.items = items


window = Tk()


window.title("Welcome to LikeGeeks app")

window.geometry('350x200')


def buttonClick():
    """ handle button click event and output text from entry area"""
    print('hello')    # do here whatever you want

    listbox.delete(0, END)

    for item in tmp:
        item.sell_in = item.sell_in-1
        item.quality = item.quality-1

    for item in tmp:
        listbox.insert(END, item)


btn = Button(window, text="simulate", command=buttonClick)

btn.pack()
listbox = Listbox(window)
listbox.pack()
item = Item("item1", 10, 5)
tmp = item.__seed__()

for item in tmp:
    listbox.insert(END, item)
window.mainloop()
