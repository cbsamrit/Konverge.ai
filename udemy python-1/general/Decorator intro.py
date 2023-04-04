from functools import wraps
def counter(fun):

    count=0
    
    @wraps(fun)
    def inner(*a:"value is a",**b:"value is b"):

        "this code written by chetan"
        nonlocal count
        count+=1
        print(f"name of function is {fun.__name__} and call {count} times")
        return fun(*a,**b)

    return inner


@counter
def fun(l:"chetan",m:"c=bhaurao"):

    "this code written by rahul"
    return l+m


print(fun(2,3))
print(help(fun))
print(fun.__name__) #if we not add wraps then show propery of inner bcx here fun=counter(fun) that return address 
                    # of inner




k=counter(fun)
print(k(2,3))
print(k.__name__)
print(help(k))  #if we not add wraps then show propery of inner bcx here fun=counter(fun) that return address 
                    # of inner





