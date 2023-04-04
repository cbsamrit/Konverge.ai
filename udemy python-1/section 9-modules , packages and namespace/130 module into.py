def sum():

    a=10
    b=20
    print(a,b)


# import fractions
# import sys
# print(fractions)
# from fractions import Fraction
# print(globals()['fractions'].Fraction)
# print(fractions.__name__)
# print(fractions.__dict__['Fraction'])
# print(sys.modules['fractions'])
# print(dir(fractions))
# print(fractions.__dict__)
# print(fractions)

from types import ModuleType
k=ModuleType("Test","this is a test module")
k.f=lambda x : (x)
k.a=34
print(k.__dict__)
print(k.__name__)
print(k.__doc__)
print(k.f(4))
f=k.f
print(f(4))
print(globals()['k'])
print(globals()['f'])
print('f' in globals())

from collections import namedtuple

k.point=namedtuple("point",("x","y"))
print(dir(k))
print(k.__dict__['point'](2,3))
k=k.point
print(k(2,3))






