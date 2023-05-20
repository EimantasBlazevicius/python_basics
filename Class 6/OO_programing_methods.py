class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def walk(self):
        print(f"{self.name} is walking with its {self.legs} legs")


cat = Animal("Obi", 4)
dog = Animal("Pupa", 4)
duck = Animal("Scheldon", 2)

duck.walk()
