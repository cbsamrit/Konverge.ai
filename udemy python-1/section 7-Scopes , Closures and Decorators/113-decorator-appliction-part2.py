class myclass:
    def __init__(self,a,b) :
        self.a=a
        self.b=b

    def outer(self,fun):
        print(f"value of a and b is {self.a} and {self.b}")
        print("call outer fun")
        def inner(a,b):
          print("call inner fun")
          return fun(a,b)
        return inner
def fun(a,b):
    return a*b

temp=myclass(2,3)

k=temp.outer(fun)

print(k(4,5))



