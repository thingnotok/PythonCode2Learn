from ctest._math import lib

import time


c_ipow = lib.ipow

def timer(stuff, times):
    tSt = time.time()
    for i in range(times):
        exec(stuff)
    tEn = time.time()
    print('Runnung ', stuff, ' ' ,str(times), 'times takes : ', tEn-tSt, ' sec')

def correctness(stuff1, stuff2):
    res1 = eval(stuff1)
    res2 = eval(stuff2)
    print('Correctness Check : ', res1 == res2)


def py_pow(a, b):
    return a**b

print('Integer pow test : ')
correctness('c_ipow(3, 17)', 'py_pow(3, 17)')
timer('c_ipow(3, 128)', 100000)
timer('py_pow(3, 128)', 100000)
