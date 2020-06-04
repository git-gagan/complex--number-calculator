# --------------
import math

class complex_numbers:
    def __init__(self,r,i):
        self.real=r
        self.imag=i

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        a_r=self.real+other.real
        a_i=self.imag+other.imag
        return complex_numbers(a_r,a_i)
    
    def __sub__(self,other):
        s_r=self.real-other.real
        s_i=self.imag-other.imag
        return complex_numbers(s_r,s_i)

    def __mul__(self,other):
        m_r=self.real*other.real - self.imag*other.imag
        m_i=self.imag*other.real + self.real*other.imag
        return complex_numbers(m_r,m_i)
    
    def __truediv__(self,other):
        d_r=(self.real*other.real + self.imag*other.imag)/(other.real**2+other.imag**2)
        d_i=(self.imag*other.real - self.real*other.imag)/(other.real**2+other.imag**2)
        return complex_numbers(d_r,d_i)

    def absolute(self):
        c=math.sqrt(self.real*self.real+self.imag*self.imag)
        return c
    
    def argument(self):
        a=round(math.degrees(math.atan(self.imag/self.real)),2)
        return a
    
    def conjugate(self):
        real=self.real
        imag=-(self.imag)
        return complex_numbers(real,imag)

comp_1 = complex_numbers(3,5)
comp_1.__repr__()
comp_2 = complex_numbers(4,4)
comp_sum = comp_1 + comp_2
comp_diff = comp_1 - comp_2
comp_prod = comp_1 * comp_2
comp_quot = comp_1 / comp_2
comp_abs = comp_1.absolute()
comp_conj = comp_1.conjugate()
comp_arg = comp_1.argument()
print(comp_arg)








