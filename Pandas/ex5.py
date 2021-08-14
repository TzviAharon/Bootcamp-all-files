import pandas as pd 
filename = 'NewMat.csv'
data     = pd.read_csv(filename)
dtype    = data.Q1.dtype 
print(data.loc[pd.notnull(data.Q2)])
