
import main
import fib
import primes
# import demo_diseable_gil
import cython_from_c
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("Python function")
    # main.function_python()
    # print("Cython Fucntion")
    # main.function_cython()

    # print("Fib ave python")
    # print(fib.fib_python(50))
    #
    # print("Fib ave cython")
    # print(fib.run_cython_fib(50))

    ##Get Primes
    # print("Get primes with python")
    # print(primes.get_primes(10))
    # print("Get primes with cython")
    # print(primes.run_get_primes_cython(10))

    # noGIL
    # demo_diseable_gil.demo_diseable_gil()

    #C in Cython
    cython_from_c.print_hello(b"ihab")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
