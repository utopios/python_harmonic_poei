#1
from re import findall, split, sub, subn

chaine = "test   : testetsestets"

if(len(findall(":", chaine)) == 1):
    print(split(":", chaine)[1])
else:
    print("la chaine n'a pas 1 seul ':'")

#2
chaines = [
    "par ici",
    "test spare",
    "un park",
    "sparkextragarden"
]
dict_replace = {
    "par": "spar",
    "spare": "extra",
    "park": "garden"
}

for i in range(len(chaines)):
    for val, repl in dict_replace.items():
        chaines[i] = sub(r"\b" + val + r"\b", repl, chaines[i])
print(chaines)

#3
str = "(1) test (333) ((element))"
##Patern 'Guillaume' \(([^()]*)\)
liste = findall(r"\((.*)\)", str)
print(liste)

#4
def using_subn(pattern):
    liste = ['element1', 'toto', 'tata', 'titi', 'minet']
    return [subn(f'r{pattern}', pattern, w) for w in liste]

print(using_subn('t'))