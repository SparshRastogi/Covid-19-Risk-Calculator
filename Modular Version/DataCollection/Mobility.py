import requests
import pandas as pd

def mobility_dataset(month,year):
  url = 'https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv'
  df = pd.read_csv(url)
  columns = df.columns
  usdata = df.loc[df['country_region'] == 'United States']
  usdata['date'] = pd.to_datetime(usdata['date'])
  usdata['year'] = usdata['date'].dt.year
  usdata['month'] = usdata['date'].dt.month
  mobility = pd.DataFrame(usdata.loc[usdata['year'] == year])
  county = list(usdata['census_fips_code'].unique())
  dfco = pd.DataFrame(columns = columns)
  for i in county:    
     data = pd.DataFrame(mobility.loc[(mobility['census_fips_code'] == i) & (mobility['month'] == month)])
     mobility1 = ['date','month','year','retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']
     mobility2 = ['census_fips_code','month','retail_and_recreation_percent_change_from_baseline','grocery_and_pharmacy_percent_change_from_baseline','parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline','workplaces_percent_change_from_baseline','residential_percent_change_from_baseline']
     d = pd.DataFrame(mobility.loc[(mobility['census_fips_code'] == i) & (mobility['month'] == month)])
     d = d.drop((mobility1),axis=1)
     d = d.drop_duplicates(subset = 'census_fips_code')
     da =pd.DataFrame(data[mobility2].mean())
     da = da.transpose()
     fd = pd.merge(d,da,on = 'census_fips_code')
     objs = [dfco,fd]
     dfco = pd.concat(objs,axis = 0)
     dfco.reset_index(drop = True,inplace = True)
     print(dfco)
     name = f'/content/drive/MyDrive/Colab Notebooks/Mobility {year} Month{month}.csv'
     dfco.to_csv(name,index=False)
