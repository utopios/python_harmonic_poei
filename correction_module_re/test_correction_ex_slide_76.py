#1
from re import findall, split, sub, subn, finditer

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
def using_subn(pattern, replace):
    liste = ['element1', 'toto', 'tata', 'titi', 'minet']
    return [subn(f'r{pattern}', replace, w) for w in liste]

print(using_subn('t', 't'))

#5
def question_5():
    str = "TWXA42:JWPA:NTED01:"
    #pattern = r"([A-Z]{4}\d{2})|([A-Z]{4})"
    #pattern= r"([A-Z]{4})([0-9][0-9])?"
    #Remarque hamdi
    pattern = r"(.{4})(..)?:"
    for m in finditer(pattern, str):
        print(m.groups(default='NA'))
if __name__ == "__main__":
    question_5()