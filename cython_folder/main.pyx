import time

def function_python():
    t1 = time.time()
    calcul = 0
    for i in range(100000000):
        calcul = calcul + i

    t2 = time.time()

    t = t2 - t1
    print(str(calcul))
    print("%.20f" % t)


def function_cython():
    cdef long long int calcul
    cdef int i
    cdef float t1, t2, t
    t1 = time.time()
    for i in range(100000000):
        calcul = calcul + i

    t2 = time.time()
    print(str(calcul))
    t = t2 - t1

    print("%.100f" % t)

def run_python_pointeur(chaine):
    demo_pointeur(chaine)

cdef void demo_pointeur(char* msg):
    print(msg)
