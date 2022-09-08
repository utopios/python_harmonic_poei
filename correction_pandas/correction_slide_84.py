import pandas as pd

###Read from csv

df = pd.read_csv("Salaries.csv", sep=',')

#Q1
# print(df.head(20))
#
# #Q2
# print(df.tail(10))
#
# #Q3
# print(df.size)

#Q4
#print(df.columns)

#Q5
# print(df.dtypes)

#Q6
print(df[['phd','service','salary']].std())
print(df.select_dtypes(include='int64').std())

#Q7
#print(df[['phd','service','salary']].head(50).mean())
