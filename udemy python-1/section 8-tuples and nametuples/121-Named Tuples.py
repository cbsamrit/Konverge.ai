# import inspect
# from math import *
# t = (10, 20)
# print(round(sqrt(t[0]**2+t[1]**2), 3))


# t=(1,2,3)
# s=(1,2,3)
# print(id(t),id(s))
# print(t==s)


# l=sum( e[0] + e[1] for e in zip(t,s))
# print(l)


# class pt3d:
#     def __init__(self, a, b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __eq__(self, object):
#         if isinstance(object, pt3d):
#             return self.a == object.a and self.b == object.b and self.c==object.c
#         else:
#             return False

#     def __repr__(self):
        

#         return (f"value of a and b and c is {self.a} , {self.b} and {self.c}")    

# p1=pt3d(2,3,4)
# p2=pt3d(2,3,4)

# print(p1)
# print(p1 == p2)
# print(max(p1))  #show an eror


# def dotproduct(s,o):

#     return s.a+o.a+s.b+o.b+s.c+o.c

# print((dotproduct(p1,p2)))



# from collections import namedtuple
# point2d = namedtuple("Point2d",("x","y"))
# pt=point2d(2,3)
# st=point2d(2,3)
# print(st,pt)
# print(pt == st)
# print(max(pt))
# print(point2d._source)
# print(point2d._fields)
# print(pt._asdict())
# from collections import namedtuple

# circle=namedtuple("circle",["center_x", "Center_y" , "redius"])
# c=circle(2,3,4)
# print(c.redius)

from collections import namedtuple
stock=namedtuple("stock",("a","b","_c"),rename=True)
s=stock(2,3,4)
print(stock._fields)
print(stock._source)
# print(s.a," ",s.b," ",s.c)
# for item in s:
#     print(item)
# print(s.a)    

# l,m,n=s
# print(l,m,n)


