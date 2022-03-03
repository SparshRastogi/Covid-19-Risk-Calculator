import requests
import pandas as pd

url = 'https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv'
df = pd.read_csv(url)

df.info()

usdata = df.loc[df['country_region'] == 'United States']
usdata['date'] = pd.to_datetime(usdata['date'])
usdata['year'] = usdata['date'].dt.year
usdata['month'] = usdata['date'].dt.month

mobility2021 = pd.DataFrame(usdata.loc[usdata['year'] == 2021])

mobility2021

county = list(usdata['census_fips_code'].unique())

dfco = pd.DataFrame(columns = columns)

for j in range(1,10):
  dfco = pd.DataFrame(columns = columns)
  for i in county:    
     data = pd.DataFrame(mobility2021.loc[(mobility2021['census_fips_code'] == i) & (mobility2021['month'] == j)])
     mobility = ['date','month','year','retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']
     mobility1 = ['census_fips_code','month','retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']
     d = pd.DataFrame(mobility2021.loc[(mobility2021['census_fips_code'] == i) & (mobility2021['month'] == j)])
     d = d.drop((mobility),axis=1)
     d = d.drop_duplicates(subset = 'census_fips_code')
     da =pd.DataFrame(data[mobility1].mean())
     da = da.transpose()
     fd = pd.merge(d,da,on = 'census_fips_code')
     objs = [dfco,fd]
     dfco = pd.concat(objs,axis = 0)
     print(dfco)
  name = '/content/drive/MyDrive/Colab Notebooks/Mobility 2021 Month' + str(j) +'.xlsx'
  dfco.to_excel(name)
