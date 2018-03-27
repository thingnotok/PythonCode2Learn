"""
np_cffi implementaion
"""

import cffi

FFI = cffi.FFI()
FFI.cdef(open('np.h').read())


FFI.set_source('ctest._np', open('np.c').read())


if __name__ == '__main__':
    FFI.compile(verbose=False)