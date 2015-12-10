
class Fraction:

    def __init__(self, numerator, denominator):
        simplified = self._simplify(numerator, denominator)
        self.numerator = simplified[0]
        self.denominator = simplified[1]

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator + other.numerator
            if numerator == self.denominator:
                return 1
            else:
                return Fraction(self.numerator + other.numerator, self.denominator)

        elif max(self.denominator, other.denominator) % min(self.denominator, other.denominator) == 0:
            multiplicator = max(self.denominator, other.denominator) / min(self.denominator, other.denominator)
            if  min(self.denominator, other.denominator) == self.denominator:
                # self. fraction is min
                numerator_to_mult = self.numerator
                numerator_to_mult *= multiplicator
                self.numerator = numerator_to_mult
                self.denominator = other.denominator
            else:
                numerator_to_mult = other.numerator
                numerator_to_mult *= multiplicator
                other.numerator = numerator_to_mult
                other.denominator = self.denominator
        else:
            # mutually prime numbers
            self.numerator *= other.denominator
            other.numerator *= self.denominator
            new_numerator = self.numerator + other.numerator
            new_denom = self.denominator * other.denominator
            return Fraction(new_numerator, new_denom)

        return Fraction(self.numerator + other.numerator, self.denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator - other.numerator
            if numerator == self.denominator:
                return 1
            else:
                return Fraction(self.numerator - other.numerator, self.denominator)
        elif max(self.denominator, other.denominator) % min(self.denominator, other.denominator) == 0:
            multiplicator = max(self.denominator, other.denominator) / min(self.denominator, other.denominator)
            if  min(self.denominator, other.denominator) == self.denominator:

                # self. fraction is min
                numerator_to_mult = self.numerator
                numerator_to_mult *= multiplicator
                self.numerator = numerator_to_mult
                self.denominator = other.denominator
            else:
                numerator_to_mult = other.numerator
                numerator_to_mult *= multiplicator
                other.numerator = numerator_to_mult
                other.denominator = self.denominator
        else:
            # mutually prime numbers
                self.numerator *= other.denominator
                other.numerator *= self.denominator
                new_numerator = self.numerator - other.numerator
                new_denom = self.denominator * other.denominator
                return Fraction(new_numerator, new_denom)
        return Fraction(self.numerator - other.numerator, self.denominator)

    def __mul__(self, other):
        new_num = self.numerator*other.numerator
        new_denom = self.denominator*other.denominator
        return Fraction(new_num, new_denom)

    def __div__(self, other):
        new_num = self.numerator * other.denominator
        new_denom = self.denominator * other.numerator
        return Fraction(new_num, new_denom)

    def _gcd(self, x, y):
        while y != 0:
            # x = y; y = x % y
            (x, y) = (y, x % y)
        return x

    def _simplify(self, num, denom):
        common_div = self._gcd(num, denom)
        new_num = num / common_div
        new_denom = denom / common_div
        res = [new_num, new_denom]
        return res

a = Fraction(1, 3)
b = Fraction(2, 5)

print (a/ b)
