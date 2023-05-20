class Animal:
    def __init__(self, type):
        self.type = type

    def move(self):
        print("Moving...")


class Mammal(Animal):
    def __init__(self, legs):
        super().__init__(type="Mammal")
        self.legs = legs


class ColdBlood(Animal):
    def __init__(self, legs):
        super().__init__(type="ColdBlood")
        self.legs = legs


human = Mammal(4)
print(human.type)
raptor = ColdBlood(4)
print(raptor.legs)
raptor.move()
