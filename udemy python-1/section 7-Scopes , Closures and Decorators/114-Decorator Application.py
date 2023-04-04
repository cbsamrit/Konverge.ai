from fractions import Fraction
f=Fraction(2,3)
Fraction.speak = lambda self : "This is late parrot"
Fraction.is_integral= lambda self : f"{self} and {self.denominator==1}"

print(f.is_integral())
print(f.speak)



 

