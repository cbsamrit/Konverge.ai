from collections import namedtuple

stock=namedtuple("stock",("open","close","high","low",))

chetan=stock(2.34,3.45,0.23,7.90)
print(chetan)
chetan._replace(close=9.40,low=4.50)
print(chetan)
extended_stock=namedtuple("extended_stock",stock._fields+("prev_close",))
rohit=extended_stock(2.34,3.45,0.23,7.90,4.50)
print(rohit)
# print(stock._source)


 

