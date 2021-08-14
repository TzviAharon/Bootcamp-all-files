import pandas as pd
filepath = 'NewMat.csv'
data = pd.read_csv (filepath)

desc               =  data.loc[:,'Q1']
first_description  =  desc[0]
first_row          =  data.iloc[0,: ]
first_descriptions =  data.loc[:4,'Q2']
sample_reviews     =  data.iloc[[1,2,4]]
df                 =  data.loc[:5,['Q1','Q3']]
barcaStats         =  data.loc[(data['City'] == "Barca") & (data['Q3'] > 0.16)]