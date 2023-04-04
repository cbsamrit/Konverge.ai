from collections import namedtuple
d = dict(key1=1, key2=2, key3=3)
print(d)
data = namedtuple("data", list(d.keys()))
k = data(**(d))
print(k)
print(k[0])
print(k.key1)
print(data._fields)
data = namedtuple("data", data._fields+("key4",))


d = [{"key1": 1, "key2": 2}, {"key1": 3}, {"key3": 4}]
s = set()
for i in d:
    for item in i:
        s.add(item)


temp = namedtuple("temp", s)

temp.__new__.__defaults__ = (None,)*len(s)

ts = []
for i in d:
    ts.append(temp(**i))

print(ts)
