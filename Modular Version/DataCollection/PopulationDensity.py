import requests
import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/County Wise Population Density.xlsx')
df = df.drop(['Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11'],axis = 1)
df.info()
counties = list(df['FIPS CODE'].unique())
