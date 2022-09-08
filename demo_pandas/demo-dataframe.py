import pandas as pd

##Création d'une dataframe

df1 = pd.DataFrame()
#print(df1)

df2 = pd.DataFrame([pd.Series([1,3,5,7,10]), pd.Series([10,20,40,60])])
#print(df2)

data = [["toto", 20], ["tata", 30], ["titi", 35]]
df3 = pd.DataFrame(data, columns=['Prénom', 'Age'])

#print(df3)
data = {'Prénom': ["toto","tata", "titi"], 'Age':[20,30,35]}
df4 = pd.DataFrame(data, index=['r1', 'r2', 'r3'])
print(df4)
