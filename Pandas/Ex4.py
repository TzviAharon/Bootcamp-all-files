import pandas as pd 
filePath        = 'NewMat.csv'
data            = pd.read_csv(filePath)
cittMin         = data.groupby('City').Q1.max()
QoneFirst       = data.groupby('City').apply(lambda df: df.Q1.iloc[0]) 
CuntriesIndexed = data.groupby('State').State.count()
priceIndexed    = data.groupby('Price').Q4.max()
priceByCity     = data.groupby('City').Price.agg([min , max])
sortedCitys     = priceByCity.sort_values(by = ['min' , 'max'])
sortedStates    = data.groupby('State').Price.mean()
FrequentComb    = data.groupby(['State' , 'City']).State.count().sort_values(ascending = False)