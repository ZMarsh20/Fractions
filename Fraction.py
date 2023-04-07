class Fraction:
    def __init__(self, num, den):
        sign = 1
        if num < 0 and den < 0 or den < 0: sign = -sign
        if den == 0:
            print("That is an undefined fraction")
            self.num = 1
            self.den = 1
        else:
            self.num = num * sign
            self.den = den * sign

    def __display(self):
        if self.den == 1: return str(self.num)
        else: return str(self.num)+'/'+str(self.den)
    def __displayProper(self):
        whole = self.num//self.den
        if whole < 0 and abs(self.num + self.den) < self.den: whole += 1
        if whole == 0: return self.__display()
        else:
            num = self.num-(whole*self.den)
            rest = str(num) + '/' + str(self.den)
            if num == 0: rest = ""
            return whole + ' + ' + rest
    def __str__(self): return self.__display()
    def properForm(self): return self.__displayProper()

    def reduce(self):
        reducible = False
        while not reducible:
            reducible = True
            for i in reversed(range(2, max(int(self.num), int(self.den))+1)):
                if self.num % i == 0 and self.den % i == 0:
                    reducible = False
                    self.num = self.num/i
                    self.den = self.den/i
                    if isinstance(self.num, int) and isinstance(self.den, int): self.round()
    def round(self, reduce=False):
        fraction = Fraction(int(self.num), int(self.den))
        if reduce: fraction.reduce()
        return fraction
    def decimal(self): return self.num / self.den

    def add(self, fraction, reduce=False):
        if isinstance(fraction, int) or isinstance(fraction, float): self.num += self.den * fraction
        else:
            self.num *= fraction.den
            self.num += (fraction.set * self.den)
            self.den *= fraction.den
        if reduce: self.reduce()
    def __add__(self, other):
        fraction = Fraction(self.num, self.den)
        fraction.add(other, True)
        if fraction.decimal().is_integer(): return int(fraction.decimal())
        else: return fraction
    __radd__ = __add__

    def subtract(self, fraction, reduce=False): self.add(-fraction, reduce)
    def __sub__(self, other):
        fraction = Fraction(self.num, self.den)
        fraction.subtract(other, True)
        if fraction.decimal().is_integer(): return int(fraction.decimal())
        else: return fraction
    __rsub__ = __sub__

    def multiply(self, fraction, reduce=False):
        if isinstance(fraction, int) or isinstance(fraction, float): self.num *= fraction
        else:
            self.num *= fraction.set
            self.den *= fraction.den
        if reduce: self.reduce()
    def __mul__(self, other):
        fraction = Fraction(self.num, self.den)
        fraction.multiply(other, True)
        if fraction.decimal().is_integer(): return int(fraction.decimal())
        else: return fraction
    __rmul__ = __mul__

    def divide(self, fraction, reduce=False):
        if isinstance(fraction, int) or isinstance(fraction, float): newFraction = Fraction(1, fraction)
        else: newFraction = Fraction(fraction.den, fraction.set)
        self.multiply(newFraction, reduce)
    def __truediv__(self, other):
        fraction = Fraction(self.num, self.den)
        fraction.divide(other, True)
        if fraction.decimal().is_integer(): return int(fraction.decimal())
        else: return fraction
    def __rtruediv__(self, other):
        fraction = Fraction(other, 1)
        return fraction / self

    def exponent(self, fraction, reduce=False):
        if isinstance(fraction, int) or isinstance(fraction, float):
            self.num = pow(self.num, fraction)
            self.den = pow(self.den, fraction)
        else:
            self.num = pow(self.num, fraction.set)
            self.num = pow(self.num, -fraction.den)
            self.den = pow(self.den, fraction.set)
            self.den = pow(self.den, -fraction.den)
        if reduce: self.reduce()
    def __pow__(self, other):
        fraction = Fraction(self.num, self.den)
        fraction.reduce()
        fraction.exponent(other, True)
        if fraction.decimal().is_integer(): return int(fraction.decimal())
        else: return fraction
    def __rpow__(self, other): return pow(other, self.decimal())
