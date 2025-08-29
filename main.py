import pandas as pd

#Load CSV
df = pd.read_csv('us-shein-appliances-3987.csv')

#Renaming columns
df = df.rename(columns={
    'goods-title-link--jump' : 'Title',
    'goods-title-link--jump href' : 'Ref-link',
    'rank-title' : 'Ranking',
    'rank-sub' : 'Category',
    'price' : 'Price',
    'discount' : 'Discount',
    'selling_proposition' : 'Pitch',
    'goods-title-link' : 'Type'

})

#Cleaning non-null values
df['Title'] = df['Title'].fillna('No link')
df['Ref-link'] = df['Ref-link'].fillna('No link')
df['Ranking'] = df['Ranking'].fillna('Unranked')
df['Category'] = df['Category'].fillna('No Category')
df['Price'] = df['Price'].fillna('No price')
df['Discount'] = df['Discount'].fillna('No Discount')
df['Pitch'] = df['Pitch'].fillna('No sales recently')
df['Type'] = df['Type'].fillna('No Type')

df = df.to_csv('US Shein Appliances.csv', index=False)