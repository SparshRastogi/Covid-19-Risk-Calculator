for k in range(9,10):
  a = []
  j = k + 1
  data = pd.read_csv('https://raw.githubusercontent.com/SparshRastogi/Covid-19-Risk-Calculator/main/Imputed%20Dataset%202021%20Month' + str(k) + '.csv')
  data = data.dropna(subset=['Cases '])
  f =open('/content/drive/MyDrive/Colab Notebooks/Model Month' + str(k) + '.pickle','rb')
  model = pickle.load(f)
 # data = data.dropna(subset = ['Cases'])
  target = data['Cases ']
#  target = target.dropna()
  #print(target)
  features1 = data[features]
  predictions = model.predict(features1)
 # for x in range(3143):
   # diff = predictions[x] - target[x]
   # if diff > 100 or diff < -100:
     # a.append(diff)
 # print(len(a))
  #score = model.score(model.predict(data[features]),targets)
  ma = mean_absolute_error(target, model.predict(features1))
  ms = mean_squared_error(target,model.predict(features1))
  rmse = mean_squared_error(target,model.predict(features1),squared = False)
  #print(score)
  print(ma)
  print(ms)
  print(rmse)
  results = permutation_importance(model, features1, targets, scoring='neg_mean_squared_error')
# get importance
  importance = results.importances_mean
  cumulative = abs(importance).sum()
  print(cumulative)
# summarize feature importance
  for i,v in enumerate(importance):
    print(features[i],'Feature: %0d, Score: %.5f' % (i,v/cumulative))
# plot feature importance
  plt.bar([x for x in range(len(importance))], importance/cumulative)
  plt.show()
  risk = pd.DataFrame()
 # risk['risk'] = 0
  for i,v in enumerate(importance):   
    impo = (v/cumulative)*100
    print(impo)
    column = features[i] 
    df = pd.DataFrame() 
    df[column] = data[column]
    df['maximum'] = abs(df[column]).max()
   # print(maximum)
    if column not in vc:
      df['risk'] = (df[column]/df['maximum'])*impo
    else:
      df['risk'] = ((100-df[column])/df['maximum'])*impo
    vu = column + 'risk'
    risk[vu] = df['risk']
    #for i in df:
  risk['risk'] =risk[risk.columns].sum(axis=1) 
  risk = risk['risk']
  risk = pd.concat([data,risk],axis = 1)
  print(risk)
  risk.to_csv('/content/drive/MyDrive/Colab Notebooks/2021 Month' + str(k) + ' Risk.csv')
  #print(features[i],'Feature: %0d, Score: %.5f' % (i,v/cumulative))
