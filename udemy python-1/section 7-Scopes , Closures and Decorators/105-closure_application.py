def outer(fn,x=0):
    def inner(a,b):
        nonlocal x
        x+=1
        print(f"{fn.__name__} call {x} times ")
        return fn(a,b)
    return inner


def add(l,m):
    return l+m

def mul(x,y):
    return x*y
    
k1=outer(add)

print(k1(2,3))
print(k1(4,5))
print(k1(6,7))

