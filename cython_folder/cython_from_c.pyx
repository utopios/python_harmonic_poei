cdef extern void hello_word(const char *name)

def print_hello(name: bytes):
    hello_word(name)