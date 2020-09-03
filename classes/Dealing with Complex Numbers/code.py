import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def mod(self):
        return math.sqrt(self.real*self.real + self.imaginary*self.imaginary)
    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imaginary + c2.imaginary) 
    def __sub__(self, c2):
        return Complex(self.real - c2.real, self.imaginary - c2.imaginary) 
    def __mul__(self, c2):
        return Complex(self.real*c2.real - self.imaginary*c2.imaginary, self.imaginary*c2.real + self.real*c2.imaginary)
    def __truediv__(self, c2):
        c2_mod2 = float(c2.real*c2.real + c2.imaginary*c2.imaginary)
        return Complex((self.real*c2.real + self.imaginary*c2.imaginary)/c2_mod2, 
                    (self.imaginary*c2.real - self.real*c2.imaginary)/c2_mod2);
    def conjugate(self):
        return Complex(self.real, -self.imaginary)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, str(round(x.mod(),2))+"+0.00i", "0.00+"+str(round(y.mod(),2))]), sep='\n')