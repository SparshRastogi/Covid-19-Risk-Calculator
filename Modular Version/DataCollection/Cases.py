import requests
import pandas as pd
def cases_dataset(month,year):
  df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')
  columns = df.columns
  df['date'] = pd.to_datetime(df['date'])
  df['year'] = df['date'].dt.year
  df['month'] = df['date'].dt.month
  cases2021 = df.loc[df['year'] == year]
  counties = list(cases2021['fips'].unique())
  cases2021.rename(columns = {'fips':'FIPS CODE'}, inplace = True)
  dfco = pd.DataFrame(columns = columns)
  dfco = dfco.drop(['fips'],axis = 1)
  for i in counties:    
     data = pd.DataFrame(cases2021.loc[(cases2021['FIPS CODE'] == i) & (cases2021['month'] == month)])
     cases = ['cases','deaths']     
     cases1 = ['FIPS CODE','cases','deaths']
     d = pd.DataFrame(cases2021.loc[(cases2021['FIPS CODE'] == i) & (cases2021['month'] == month)])
     d = d.drop((cases),axis=1)
     d = d.drop_duplicates(subset = 'FIPS CODE')
     da =pd.DataFrame(data[cases1].mean())
     da = da.transpose()
     fd = pd.merge(d,da,on = 'FIPS CODE')
     objs = [dfco,fd]
     dfco = pd.concat(objs,axis = 0)
     dfco.reset_index(drop = True,inplace = True)
     print(dfco)
  name = f'/content/drive/MyDrive/Colab Notebooks/Cases 2021 Month{month}.csv'
  dfco.to_csv(name,index = False)
