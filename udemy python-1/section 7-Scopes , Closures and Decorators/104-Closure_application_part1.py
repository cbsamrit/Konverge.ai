class avg:

    def __init__(self):

        self.list_of_n = []

    def add(self, c):
        self.list_of_n.append(c)
        total = sum(self.list_of_n)
        n = len(self.list_of_n)
        return total/n


k = avg()

k.add(2)

k.add(3)

l = avg()

l.add(2)

l.add(3)


def fun():

    l = []

    def add(k):
        l.append(k)
        total = sum(l)
        n = len(l)

        return total/n

    return add


c1 = fun()
print(c1(2))
print(c1(3))
print(c1(5))
print(c1(5))

c2 = fun()
print(c2(2))
