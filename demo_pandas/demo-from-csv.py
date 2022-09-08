import pandas as pd

###Read from csv

df = pd.read_csv("Salaries.csv", sep=',')
print(df[['rank','service']])
print(df.tail(10))