###Q1 Écrivez un programme Python pour afficher les 5 premières lignes de l'ensemble de données COVID-19.
# Imprimez également les informations du jeu de données et vérifiez les valeurs manquantes.
import pandas as pd
covid_data= pd.read_csv('covid_19.csv')
print(covid_data)
print(covid_data.head(5))
print("\nDataset information:")
print(covid_data.info())
print("\nMissing data information:")
print(covid_data.isna().sum())

###Q2 Écrivez un programme Python pour obtenir le dernier nombre de cas confirmés,
# de décès, récupérés et actifs de nouveau coronavirus (COVID-19) par pays.
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(result)

###Q3 Écrivez un programme Python pour obtenir le dernier nombre de décès confirmés et de personnes récupérées
# de cas de nouveau coronavirus (COVID-19) par pays/région - province/État.
data = covid_data.groupby(['Country/Region', 'Province/State'])['Confirmed', 'Deaths', 'Recovered'].max()
pd.set_option('display.max_rows', None)
print(data)

###Q4 Écrivez un programme Python pour obtenir la province chinoise des cas confirmés,
#  des décès et des cas récupérés de nouveau coronavirus (COVID-19).
c_data = covid_data[covid_data['Country/Region']=='China']
c_data = c_data[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
result = c_data.sort_values(by='Confirmed', ascending=False)
result = result.reset_index(drop=True)
print(result)


###Q5 Écrivez un programme Python pour obtenir les derniers cas de décès par pays du nouveau coronavirus (COVID-19).
data = covid_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
result = data[data['Deaths']>0][['Country/Region', 'Deaths']]
print(result)

###Q6 Écrivez un programme Python pour répertorier les pays où aucun cas de nouveau coronavirus (COVID-19) n'a été récupéré.
data = covid_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
result = data[data['Recovered']==0][['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
print(result)

###Q7 Écrivez un programme Python pour répertorier les pays dans lesquels tous les cas de nouveau coronavirus (COVID-19) sont décédés.
data = covid_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
result = data[data['Confirmed']==data['Deaths']]
result = result[['Country/Region', 'Confirmed', 'Deaths']]
result = result.sort_values('Confirmed', ascending=False)
result = result[result['Confirmed']>0]
result = result.reset_index(drop=True)
print(result)

###Q8 Écrivez un programme Python pour répertorier les pays dans lesquels tous les cas de nouveau coronavirus (COVID-19) ont été récupérés.
data = covid_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
result = data[data['Confirmed']==data['Recovered']]
result = result[['Country/Region', 'Confirmed', 'Recovered']]
result = result.sort_values('Confirmed', ascending=False)
result = result[result['Confirmed']>0]
result = result.reset_index(drop=True)
print(result)

###Q9 Écrivez un programme Python pour obtenir les données des 10 principaux pays
# (dernière mise à jour, pays/région, confirmés, décès, récupérés) du nouveau coronavirus (COVID-19).
result = covid_data.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].max().sort_values(by='Confirmed', ascending=False)[:10]
pd.set_option('display.max_column', None)
print(result)
