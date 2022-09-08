import pandas as pd

###Read from csv

df = pd.read_csv("Salaries.csv", sep=',')
# print(df[['rank','service']])
# print(df.tail(10))
# print(df[15:30:3])
# print(df.iloc[[2,3]])

# print(df.sort_values(by=['salary'], ascending=False))
# print(df[["salary"]].describe())

# groupby
print(df[['rank','salary']].groupby(['rank']).mean(['salary']).rename(columns={'salary':'mean'}))
print(df[['sex','salary']].groupby(['sex']).mean(['salary']))