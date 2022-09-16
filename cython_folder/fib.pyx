def fib_python(n):
    i = 0
    a, b = 0, 1
    while i < n:
        a,b = b, b + a
        i += 1
    return a

cdef int fib_cython(unsigned int n):
    cdef unsigned int i = 0
    cdef unsigned int a, b
    a, b = 0, 1
    while i < n:
        a, b = b, b + a
        i += 1
    return a

def run_cython_fib(n):
    return fib_cython(n)