class ComplexNo:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("ComplexNumber object destroyed")

    def __add__(self,other):
        return ComplexNo(self.real + other.real,self.imag + other.imag)

    def __sub__(self,other):
        return ComplexNo(self.real - other.real,self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNo(4,5)
c2 = ComplexNo(2,3)

print("Addition:",c1 + c2)
print("Subtraction:",c1 - c2)
