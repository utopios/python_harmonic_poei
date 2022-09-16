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
            primes[index] = i
            index += 1
        i += 1
    return primes

cpdef get_primes_second(const int taille):
    cdef int n, i, len
    cdef int p[taille]
    print(taille)
    len = 0
    n = 2
    while len < taille:
        for i in p[:len]:
            if n % i == 0:
                break
        else:
            p[len] = n
            len += 1
        n += 1

    result_as_list  = [prime for prime in p[:len]]
    return result_as_list

cpdef run_get_primes_cython(const int limit):
    ###Cette fonction récupère le tableau de get_primes_cython et le va le convertir en list python,
    ### la conversion n'est pas implicite entre un array en c et une liste en python
    # primes_list = []
    # cdef int* result = get_primes_cython(limit)
    #
    #
    # cdef int index = 0
    # while index < limit:
    #     primes_list.append(result[index])
    #     index += 1
    # return primes_list
    return get_primes_second(10)

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