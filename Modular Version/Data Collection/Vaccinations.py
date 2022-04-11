import requests
import pandas as pd
vaccines = ['Series_Complete_Pop_Pct', 'Series_Complete_Yes',
       'Series_Complete_12Plus', 'Series_Complete_12PlusPop_Pct',
       'Series_Complete_18Plus', 'Series_Complete_18PlusPop_Pct',
       'Series_Complete_65Plus', 'Series_Complete_65PlusPop_Pct',
       'Completeness_pct', 'Administered_Dose1_Recip',
       'Administered_Dose1_Pop_Pct', 'Administered_Dose1_Recip_12Plus',
       'Administered_Dose1_Recip_12PlusPop_Pct',
       'Administered_Dose1_Recip_18Plus',
       'Administered_Dose1_Recip_18PlusPop_Pct',
       'Administered_Dose1_Recip_65Plus',
       'Administered_Dose1_Recip_65PlusPop_Pct',
       'Series_Complete_Pop_Pct_SVI', 'Series_Complete_12PlusPop_Pct_SVI',
       'Series_Complete_18PlusPop_Pct_SVI',
       'Series_Complete_65PlusPop_Pct_SVI',
       'Series_Complete_Pop_Pct_UR_Equity',
       'Series_Complete_12PlusPop_Pct_UR_Equity',
       'Series_Complete_18PlusPop_Pct_UR_Equity',
       'Series_Complete_65PlusPop_Pct_UR_Equity']
def vaccinations_dataset(month,year):
   url = 'https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?'
   df = pd.read_csv(url)
   columns = df.columns
   df['Date'] = pd.to_datetime(df['Date'])
   df['year'] = df['Date'].dt.year
   df['month'] = df['Date'].dt.month
   df.dropna(subset = ['FIPS'],inplace = True)
   df['FIPS'] = df['FIPS'] 
   vaccinations = pd.DataFrame(df.loc[df['year'] == year])
   vaccinations = vaccinations.drop(['Date'],axis=1)
   county = list(vaccinations['FIPS'].unique())
   columns = columns[1:]
   dfco = pd.DataFrame(columns = columns)
   for i in county:    
     data = pd.DataFrame(vaccinations.loc[(vaccinations2021['FIPS'] == i) & (vaccinations['month'] == month)])
     d = pd.DataFrame(vaccinations.loc[(vaccinations2021['FIPS'] == i) & (vaccinations['month'] == month)])
     d = d.drop((vaccines),axis=1)
     d = d.drop_duplicates(subset = 'FIPS')
     da =pd.DataFrame(data[vaccines].mean())
     da = da.transpose()
     da['FIPS'] = str(i)
     fd = pd.merge(d,da,on = 'FIPS')
     objs = [dfco,fd]
     dfco = pd.concat(objs,axis = 0)
     dfco.reset_index(drop = True,inplace = True)
     print(dfco)
   name = f'/content/drive/MyDrive/Colab Notebooks/Vaccinations 2021 Month{month}.csv'
   dfco.to_csv(name,index = False)
