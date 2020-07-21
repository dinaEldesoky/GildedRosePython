from tkinter import *
from item import Item


window = Tk()


def buttonSimualte():
    """ handle button click event and output text from entry area"""
    print('hello')    # do here whatever you want

    listbox.delete(0, END)

    for item in tmp:
        if item.sell_in > 0:
            check(item)

    for item in tmp:
        listbox.insert(END, item)


window.title("Welcome to LikeGeeks app")

window.geometry('350x200')


def buttonAdd():
    """ handle button click event and output text from entry area"""
    print('hello from add')    # do here whatever you want
    name = eName.get()
    sell = eSell.get()
    quilaty = eQuality.get()
    newItem = Item(name, int(sell), int(quilaty))
    tmp.insert(0, newItem)
    listbox.insert(END, newItem)


def check(item):
    if item.name == "Aged Brie" or item.name == "Backstage passes" or item.name == "Conjured" or item.name == "Sulfuras":
        print("ok")
        if item.name == "Aged Brie":
            if item.quality + 1 <= 50:
                item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1

        elif item.name == "Conjured":
            if item.quality - 4 >= 0:
                item.quality = item.quality - 4
            else:
                item.quality = 0
            item.sell_in = item.sell_in - 1

        elif item.name == "Backstage passes":
            if item.sell_in <= 10 and item.quality + 2 <= 50:
                item.quality = item.quality + 2
            elif item.sell_in <= 5 and item.quality + 3 <= 50:
                item.quality = item.quality + 3
            elif item.sell_in == 0:
                item.quality = 0
            item.sell_in = item.sell_in - 1
    else:
        print("normal")
        if item.quality - 2 > 0:
            item.quality = item.quality - 2
            item.sell_in = item.sell_in - 1


listbox = Listbox(window)
listbox.pack()
item = Item("item1", 10, 5)
tmp = item.__seed__()

for item in tmp:
    listbox.insert(END, item)

btnSimulate = Button(window, text="Simulate", command=buttonSimualte)
btnAdd = Button(window, text="Add", command=buttonAdd)


btnSimulate.pack()

eName = Entry(window)
eSell = Entry(window)
eQuality = Entry(window)

eName.pack()
eSell.pack()
eQuality.pack()


btnAdd.pack()

window.mainloop()
