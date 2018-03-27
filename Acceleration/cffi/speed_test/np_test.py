from ctest._np import ffi, lib
import numpy as np
import time


w, h = 1024, 768
img_src = np.ones(w*h, dtype=np.float32).reshape(h, w)
img_dst = np.zeros_like(img_src)
p_src = ffi.cast('float *', img_src.ctypes.data)
p_dst = ffi.cast('float *', img_dst.ctypes.data)


def timer(stuff, times):
    tSt = time.time()
    for i in range(times):
        exec(stuff)
    tEn = time.time()
    print('Runnung ', stuff, ' ' ,str(times), 'times takes : ', tEn-tSt, ' sec')

def correctness():
    Ref = img_src+img_src
    lib.add(p_src, p_src, p_dst, w, h)
    print('Correctness Check : ', np.array_equal(Ref, img_dst))

print('Numpy 2D Array addition test : ')
correctness()
timer('Ref = img_src+img_src', 1000)
timer('lib.add(p_src, p_src, p_dst, w, h)', 1000)
print(lib.cnt)