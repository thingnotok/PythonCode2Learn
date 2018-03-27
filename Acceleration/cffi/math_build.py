import cffi

ffibuilder = cffi.FFI()
ffibuilder.set_source('ctest._math',r"""
int add(int a, int b){
    return a + b;
}
int mul(int a, int b){
    return a * b;
}
int ipow(int base, int exp)
{
    int result = 1;
    while (exp != 0)
    {
        if ((exp & 1) == 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}
""")

ffibuilder.cdef("""
int add(int, int);
int mul(int, int);
int ipow(int, int);
""")

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)