import pandas as pd 

# do not name file as csv
data=pd.read_csv('data.csv')

print(data)

new_csv=pd.read_csv('data.csv',names=['alphabet','price','quantity'],header=0,usecols=[1,2,3])
new_csv.to_csv('data_written.csv')