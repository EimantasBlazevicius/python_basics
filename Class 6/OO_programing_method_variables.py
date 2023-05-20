class Addition:
    def __init__(self):
        self.number = 0

    def add(self, number_to_add):
        self.number += number_to_add

    def state(self):
        print(self.number)


instance1 = Addition()
instance2 = Addition()
instance3 = Addition()

instance1.add(5)
instance2.add(2)


instances = [instance1, instance2, instance3]
for instance in instances:
    instance.state()
