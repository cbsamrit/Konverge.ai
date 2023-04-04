def timed(fun):

    from time import perf_counter
    from functools import wraps

    @wraps(fun)
    def inner(*a: "value enter a ", **b: "value enter b"):
        "take reference by another function "
        s = perf_counter()
        result = fun(*a, **b)
        e = perf_counter()
        print(f"time requird to run {fun.__name__} is {e-s}")

        return result

    return inner

# @timed
def fibo(a: "value is a") -> "return fibono":
    "this code written by chetan"
   
    # print("jsnvr")
    if a <= 2:
        return 1
    else:
     return fibo(a-1) + fibo(a-2)
    
# do not direct decorate recursive fuction
# print(fibo(55))


@timed
def fibo_return(a):
    return fibo(a)


print(fibo_return(55))


# @timed
# def fibo_f(a):
#     l=1
#     m=1
#     for i in range(1,a):

#         l,m=m,l+m

#     return l

# print(fibo_f(34))

# def fibo_r(n):


