
import main
import fib
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("Python function")
    # main.function_python()
    # print("Cython Fucntion")
    # main.function_cython()

    print("Fib ave python")
    print(fib.fib_python(50))

    print("Fib ave cython")
    print(fib.run_cython_fib(50))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
