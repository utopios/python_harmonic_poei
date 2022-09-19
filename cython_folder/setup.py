import os
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

ext_modules = [
    # Extension("main", ["main.pyx"]),
    # Extension("fib", ["fib.pyx"]),
    # Extension("primes", ["primes.pyx"]),
    # Extension("cython_from_c", ["cython_from_c.pyx", "demo.c"])
    # Extension("slide_21", ["slide_21.pyx", "slide_21_functions.c"]),
    Extension("correction_slide_18", ["correction_slide_18.pyx"])
]

setup(
    name="demo_cython",
    cmdclass = {'build_ext': build_ext},
    ext_modules=ext_modules
)
