cdef extern void getDirectory(const char* folder)

def display_file(folder):
    getDirectory(folder)