class House:
    def __init__(self, width, length):
       self.width = width
       self.length = length

class House2(House):
    def __init__(self, width, length, height):
        super().__init__(width, length)
        self.height = height


h = House2(12,24,56)
print(h.width)