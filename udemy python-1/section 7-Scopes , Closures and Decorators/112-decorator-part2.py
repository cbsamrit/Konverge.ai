from functools import wraps


def outer(reps):

    def timed(fun):

        from time import perf_counter

        @wraps(fun)
        def inner(*arg, **args):
            start = perf_counter()
            result = fun(*arg, **args)
            end = perf_counter()
            e = end-start
            print(f"Run times {e} {reps}")
            return result
        return inner

    return timed


timed=outer("chetan")


# @outer("chetan")
def fun(l, m):
    return l+m
# print(fun(3, 4))

fun=timed(fun)
print(fun(3,4))

# fun=timed(fun,"chetan")
# print(fun(2, 3))
