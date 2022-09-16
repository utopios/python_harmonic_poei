def fib_python(n):
    i = 0
    a, b = 0, 1
    while i < n:
        a,b = b, b + a
        i += 1
    return a

cdef long long int fib_cython(int n):
    cdef:
        long long int i = 0
        long long int a, b
    a, b = 0, 1
    while i < n:
        a, b = b, b + a
        i += 1
    return a

def run_cython_fib(n):
    return fib_cython(n)