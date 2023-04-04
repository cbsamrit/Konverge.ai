# timimg.py
from collections import namedtuple
from time import perf_counter
print("laoding timimg module")


Timing = namedtuple('Timing', ("repeasts", "elapsed", "avg"))

# if __name__ == '__main__' :

def timeit(code, repeats=10):

    code = compile(code, filename='<strings>', mode='exec')
    s = perf_counter()
    for _ in range(repeats):
        exec(code)
    e = perf_counter()
    elapsed = e = s
    print(elapsed)
    avg = elapsed / repeats
    return Timing(repeats, elapsed, avg)
