def risk_calculator(month,year):
  import pandas as pd
  import numpy as np
  import sklearn
  from sklearn import linear_model
  from sklearn.utils import shuffle 
  from sklearn.impute import KNNImputer
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import RandomForestRegressor
  import matplotlib
  from matplotlib import pyplot as plt
  from matplotlib import style
  import pickle
  from sklearn.inspection import permutation_importance 
  from sklearn.metrics import mean_squared_error, mean_absolute_error
  features =  ['Population Density',
       'retail_and_recreation_percent_change_from_baseline',
       'grocery_and_pharmacy_percent_change_from_baseline',
       'parks_percent_change_from_baseline',
       'transit_stations_percent_change_from_baseline',
       'workplaces_percent_change_from_baseline',
       'residential_percent_change_from_baseline', 'Completeness_pct',
       'Administered_Dose1_Recip', 'Administered_Dose1_Pop_Pct',
       'Administered_Dose1_Recip_12Plus',
       'Administered_Dose1_Recip_12PlusPop_Pct',
       'Administered_Dose1_Recip_18Plus',
       'Administered_Dose1_Recip_18PlusPop_Pct',
       'Administered_Dose1_Recip_65Plus',
       'Administered_Dose1_Recip_65PlusPop_Pct', 'Series_Complete_Pop_Pct_SVI',
       'Series_Complete_12PlusPop_Pct_SVI',
       'Series_Complete_18PlusPop_Pct_SVI',
       'Series_Complete_65PlusPop_Pct_SVI',
       'Series_Complete_Pop_Pct_UR_Equity',
       'Series_Complete_12PlusPop_Pct_UR_Equity',
       'Series_Complete_18PlusPop_Pct_UR_Equity',
       'Series_Complete_65PlusPop_Pct_UR_Equity']
  vc =  ['Completeness_pct',
       'Administered_Dose1_Recip', 'Administered_Dose1_Pop_Pct',
       'Administered_Dose1_Recip_12Plus',
       'Administered_Dose1_Recip_12PlusPop_Pct',
       'Administered_Dose1_Recip_18Plus',
       'Administered_Dose1_Recip_18PlusPop_Pct',
       'Administered_Dose1_Recip_65Plus',
       'Administered_Dose1_Recip_65PlusPop_Pct', 'Series_Complete_Pop_Pct_SVI',
       'Series_Complete_12PlusPop_Pct_SVI',
       'Series_Complete_18PlusPop_Pct_SVI',
       'Series_Complete_65PlusPop_Pct_SVI',
       'Series_Complete_Pop_Pct_UR_Equity',
       'Series_Complete_12PlusPop_Pct_UR_Equity',
       'Series_Complete_18PlusPop_Pct_UR_Equity',
       'Series_Complete_65PlusPop_Pct_UR_Equity']
  data = pd.read_csv(f'https://raw.githubusercontent.com/SparshRastogi/Covid-19-Risk-Calculator/main/Imputed%20Dataset%20{year}%20Month{month}.csv')
  data = data.dropna(subset=['Cases'])
  f =open(f'/content/drive/MyDrive/Colab Notebooks/Model Month{month}.pickle','rb')
  model = pickle.load(f)
  target = data['Cases']
  features1 = data[features]
  predictions = model.predict(features1)
  ma = mean_absolute_error(target, model.predict(features1))
  ms = mean_squared_error(target,model.predict(features1))
  rmse = mean_squared_error(target,model.predict(features1),squared = False)
  print(ma)
  print(ms)
  print(rmse)
  results = permutation_importance(model, features1, target, scoring='neg_mean_squared_error')
  importance = results.importances_mean
  cumulative = abs(importance).sum()
  print(cumulative)
  for i,v in enumerate(importance):
    print(features[i],'Feature: %0d, Score: %.5f' % (i,v/cumulative))
  plt.bar([x for x in range(len(importance))], importance/cumulative)
  plt.show()
  risk = pd.DataFrame()
  for i,v in enumerate(importance):   
    impo = (v/cumulative)*100
    print(impo)
    column = features[i] 
    df = pd.DataFrame() 
    df[column] = data[column]
    df['maximum'] = abs(df[column]).max()
    if column not in vc:
      df['risk'] = (df[column]/df['maximum'])*impo
    else:
      df['risk'] = ((100-df[column])/df['maximum'])*impo
    vu = column + 'risk'
    risk[vu] = df['risk']
  risk['risk'] =risk[risk.columns].sum(axis=1) 
  risk = risk['risk']
  risk = pd.concat([data,risk],axis = 1)
  print(risk)
  risk.to_csv('/content/drive/MyDrive/Colab Notebooks/2021 Month {month} Risk.csv')
  #print(features[i],'Feature: %0d, Score: %.5f' % (i,v/cumulative) 
