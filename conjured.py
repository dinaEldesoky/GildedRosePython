
from item import Item


class Conjured(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def Update(self):
        if self.quality - 4 >= 0:
            self.quality = self.quality - 4
        else:
            self.quality = 0
        self.sell_in = self.sell_in - 1
