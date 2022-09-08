import pandas as pd

#Création d'une serie
s1 = pd.Series(3)
print(s1)
s1 = pd.Series(['a', 'c', 'd'], index=[30,40,50])
print(s1[[30]])
print(s1[[30,40]])
s1 = pd.Series({'a': 'toto', 'b': 'tata', 'c':'titit'}, index=[1,20,30,40])
print(s1)

###Utilisation des propriétés d'une serie
print(s1.size)
print(s1.count())

s2 = pd.Series([10,30,40,60,10])

print(s2.unique())