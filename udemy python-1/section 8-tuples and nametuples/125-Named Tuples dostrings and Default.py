from collections import namedtuple

stock=namedtuple("stock",("open","close","high","low",))

# chetan=stock(2.34,3.45,0.23,7.90)
# print(chetan)
# print(stock.__doc__)

stock.__new__.__defaults__=(0,0,0,0)

chetan=stock(2.34,4.45)
print(chetan)



 