# 1. Display the number 0.5 in the form of ½ - the correct implementation of str and repr is required.
# 2. The float method should return a decimal number, and int should be similar to its counterpart in the case of float numbers. Additionally, the invert method should be used.
# 3. The comparison methods (eq, lt, gt, le, ge, cmp) should take ½ = 2/4.
# 4. The operators +, -, *, / should be implemented correctly and return a new object of this class.
# 5. It should be possible to save the current result to a file and load it.
#
# The class should always try to keep the abbreviated version of the fraction.


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # -------------Task1---------------

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        pass

    # -------------Task2---------------
    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __invert__(self):
        return Rational(self.denominator, self.numerator)

    # -------------Task3---------------

    def __eq__(self, other):
        if self.numerator / self.denominator == other.numerator / other.denominator:
            return True
        return False

    def __gt__(self, other):
        if self.numerator / self.denominator > other.numerator / other.denominator:
            return True
        return False

    def __lt__(self, other):
        if self.numerator / self.denominator < other.numerator / other.denominator:
            return True
        return False

    def __ge__(self, other):
        if self.numerator / self.denominator >= other.numerator / other.denominator:
            return True
        return False

    def __le__(self, other):
        if self.numerator / self.denominator <= other.numerator / other.denominator:
            return True
        return False
    # -------------Task4---------------

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return numerator/denominator

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return numerator/denominator

    def __mul__(self, other):
        return Rational(self.numerator*other.numerator, self.denominator* other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator/other.numerator, self.denominator / other.denominator)
    # -----------Task 5-----------------

    def save(self):
        with open("example_task_file.txt", "w") as f:
            f.write(f"{self.numerator},{self.denominator}")

    def load(self):
        with open("example_task_file.txt", "r") as f:
            read_value=f.readline().split(',')
            self.numerator = int(read_value[0])
            self.denominator = int(read_value[1])

    def add(self):
        self.denominator += 5


number = Rational(1, 2)
number2 = Rational(1, 2)
print(number)
number.save()
number.add()
print(number)
number.load()
print(number)
