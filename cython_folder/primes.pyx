from math import floor, sqrt

def get_primes(limit):
    primes = []
    i = 3
    while i < limit:
        if prime_python(i):
            primes.append(i)
        i += 1

    return primes

cdef int* get_primes_cython(const int limit):
    cdef:
        int i = 3
        int primes[limit]
        int index = 0
    while i < limit:
        if prime_cython(i):
            print(i)
            primes[index] = i
            index += 1
        i += 1
    return primes

def run_get_primes_cython(limit):
    ###Cette fonction récupère le tableau de get_primes_cython et le va le convertir en list python,
    ### la conversion n'est pas implicite entre un array en c et une liste en python
    primes_list = []
    result = get_primes_cython(limit)

    index = 0
    while index < limit:
        print(result[index])
        primes_list.append(result[index])
        index += 1
    return primes_list

def prime_python(n):
    if n == 1:
        return False
    limit = floor(sqrt(n))
    i = 1
    while i < limit + 1:
        i += 1
        if n % i == 0:
            return False
    return True


cdef bint prime_cython(long int n):
    cdef long int i
    cdef long int limit
    if n == 1:
        return False
    limit = floor(sqrt(n))

    i = 1
    while i < limit + 1:
        i += 1
        if n % i == 0:
            return False
    return True

def run_cython_prime(n):
    return prime_cython(n)