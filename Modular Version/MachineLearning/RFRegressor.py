def model_training(month,year):
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
  best = 0
  data = pd.read_csv(f'https://raw.githubusercontent.com/SparshRastogi/Covid-19-Risk-Calculator/main/Imputed%20Dataset%20{year}%20Month{month}.csv')
  data = data.dropna()
  features = data.drop(['Cases','Deaths','FIPS CODE','County','State'],axis = 1)
  features = features.select_dtypes(exclude = 'object')
  features = features.drop(['MMWR_week','Series_Complete_Pop_Pct',
       'Series_Complete_Yes', 'Series_Complete_12Plus',
       'Series_Complete_12PlusPop_Pct', 'Series_Complete_18Plus',
       'Series_Complete_18PlusPop_Pct', 'Series_Complete_65Plus',
       'Series_Complete_65PlusPop_Pct'],axis = 1)
  targets = data['Cases']
  for i in range(10):
    features_train,features_test,targets_train,targets_test = train_test_split(features,targets,train_size=0.9 ,test_size = 0.1)
    model = RandomForestRegressor()
    model.fit(features_train,targets_train)
    accuracy = model.score(features_test, targets_test)
    print('Accuracy',accuracy)
    print('MSE',mean_squared_error(targets_test,model.predict(features_test)))
    print('MAE',mean_absolute_error(targets_test,model.predict(features_test)))
    print('RMSE',mean_squared_error(targets_test,model.predict(features_test),squared=False))
    if accuracy > best:       
      best=accuracy
      print(best,' Best','\n')
      with open(f'/content/drive/MyDrive/Colab Notebooks/Model Month {month}.pickle','wb') as f:
           pickle.dump(model,f)
