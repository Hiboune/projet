import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data.csv')

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)


data.loc[data['Sales'].isnull(),'Sales']=data['Sales'].median()

for column in data.columns.values.tolist() :
    data[column].fillna(data['Sales'].median(), inplace=True)

data['mediane']= data['Price'].median()
data['efficacite']=(data['Sales']*data['Ratings'])/data['Price']

categorie= data.groupby('Category')
print(categorie.sum())