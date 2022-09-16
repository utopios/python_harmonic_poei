def main():
    #variable python
    s1 = b"hello from first string"
    s2 = b"hello from second string"
    #cdef char *all = s1 + s1 => ce code ne peut fonctionner car les objets  s1 et s2 risque d'être détruit par le GC
    # il faut générer une variable tmp avant de l'envoyer dans notre pointeur de char
    cdef bytes tmp = s1 + s2
    cdef char *all = tmp
    print(all)