import re

with open('salaries.txt', 'r') as reader:
    with open('result.txt', 'w') as writer:
        for line in reader:
            id = re.match(r'\d', line)
            salaire = re.search(r'\d{4,}\.\d{2}', line)
            print(id.group(), salaire.group())
            writer.write(id.group()+"\t")
            writer.write(salaire.group()+"\n")