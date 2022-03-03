import requests
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

df.info()

columns = df.columns

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

cases2021 = df.loc[df['year'] == 2021]

cases2021

counties = list(cases2021['fips'].unique())

counties

cases2021.rename(columns = {'fips':'FIPS CODE'}, inplace = True)

for j in range(1,10):
  dfco = pd.DataFrame(columns = columns)
  dfco = dfco.drop(['fips'],axis = 1)
  for i in counties:    
     data = pd.DataFrame(cases2021.loc[(cases2021['FIPS CODE'] == i) & (cases2021['month'] == j)])
     cases = ['cases','deaths']     
     cases1 = ['FIPS CODE','cases','deaths']
     d = pd.DataFrame(cases2021.loc[(cases2021['FIPS CODE'] == i) & (cases2021['month'] == j)])
     #print(d)
     d = d.drop((cases),axis=1)
     d = d.drop_duplicates(subset = 'FIPS CODE')
     da =pd.DataFrame(data[cases1].mean())
     da = da.transpose()
     #print(da)
     #o = [d,da]
     fd = pd.merge(d,da,on = 'FIPS CODE')
     #print(fd)
     objs = [dfco,fd]
     dfco = pd.concat(objs,axis = 0)
     dfco.reset_index(drop = True,inplace = True)
     print(dfco)
  name = '/content/drive/MyDrive/Colab Notebooks/Cases 2021 Month' + str(j) +'.csv'
  dfco.to_csv(name)
