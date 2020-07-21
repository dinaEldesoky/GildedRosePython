from item import Item


class Backstage(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def Update(self):
        print("in Backstage")
        if self.sell_in <= 10 and self.quality + 2 <= 50:
            self.quality = self.quality + 2
        elif self.sell_in <= 5 and self.quality + 3 <= 50:
            self.quality = self.quality + 3
        elif self.sell_in == 0:
            self.quality = 0
        self.sell_in = self.sell_in - 1
