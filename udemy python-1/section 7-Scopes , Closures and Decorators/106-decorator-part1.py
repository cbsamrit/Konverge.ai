from functools import wraps
def outer(fun):
    c=0

    # @wraps(fun)
    def inner(*a,b):

        '''mnjfv  fv rvnfvj
        fmvvkrnv  vmf vm '''

        print(f"value f c is {c}")

        return fun(a,b)
    # inner.__name__=fun.__name__
    # inner.__doc__=fun.__doc__
    # inner.__annotations__= fun.__annotations__
    return inner

def fun(a : "value a",b : "value b") -> "return a and b":

      " wrote  by chetan samrit "

      print(a)
      print(b)

@outer
def ls(s,i):

    print(s,i)    


fun=outer(fun)
help(fun)
help(ls)

