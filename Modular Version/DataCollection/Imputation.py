def impute_dataset(month,year):
  data = pd.read_csv(f'https://raw.githubusercontent.com/SparshRastogi/Covid-19-Risk-Calculator/main/Dataset%20{year}%20Month{month}.csv')
  data = data[data['FIPS CODE'] < 57000]
  data = data.drop(['Unnamed: 0', 'Unnamed: 0_x',
       'Unnamed: 0_y', 'date_x', 'Unnamed: 0.1', 'metro_area',
       'iso_3166_2_code', 'place_id', 'date_y'],axis = 1)
  for i in data.columns:    
    if data[i].isna().sum() != 0 and data[i].dtype == 'float':
      imputer = KNNImputer()
      data[i] = imputer.fit_transform(np.array(data[i]).reshape(-1,1))
  print(data.info())
  name = '/content/drive/MyDrive/Colab Notebooks/Imputed Dataset {year} Month{month}.csv' 
  data.to_csv(name)
