class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __seed__ (self):
        i1 = Item("item1", 10 , 5)
        i1 = Item("item2", 5 , 32)
        i2 = Item("item3", 20 , 22)
        i3 = Item("item4", 34 ,3)
        i4 = Item("item5", 4, 2)


