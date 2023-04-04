from random import randint
from collections import namedtuple

color=namedtuple("color",("red","blue","green"))

def random_color():

    red=randint(0,255)
    blue=randint(0,255)
    green=randint(0,255)

    return color(red,blue,green)

if __name__=="__main__" :
 print("ncbdhc")

import time


