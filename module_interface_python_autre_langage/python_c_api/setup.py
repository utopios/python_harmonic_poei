from distutils.core import setup, Extension

def main():
    setup(
        name="fputs",
        version="1.0.0",
        ext_modules=[Extension("fputs", ["fputsmodule.c"])]
    )

if __name__ == "__main__":
    main()