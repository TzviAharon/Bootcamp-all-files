import pandas as pd
filePath = 'NewMat.csv'
data                    = pd.read_csv(filePath)
Mean                    = data.Q3.mean()
UniCitys                = data.City.unique()
reviews_per_city        = data.City.value_counts()
centered_price          = data.Q3 - Mean
ratio                   = data.Q3/data.Q1
bargain                 = data.loc[(ratio == min(ratio))].iloc[:,0]

barcaCountMap           = data.City.map(lambda row: 'Barca' == row).sum()
romeCountMap            = data.City.map(lambda row: 'Rome' == row).sum()
cityCounts              = pd.Series([barcaCountMap,romeCountMap], index = ['Barca' , 'Rome'])

def DecToStars(row):
    if row.City == 'TLV':
        return '3 Stars'
    
    if row.Q1 < 0.15:
        return '1 Stars'
    
    if row.Q1 < 0.3:
        return '2 Stars'
    
    else:
        return '3 Stars'
    
    
starsData = data.apply(DecToStars, axis = 'columns')
    