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

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        pass

    def __float__(self):
        return self.numerator/self.denominator

    def __int__(self):
        return self.numerator//self.denominator

    def __invert__(self):
        return Rational(self.denominator, self.numerator)


number = Rational(1, 2)
print(float(number))
print(int(number))
print(~number)
