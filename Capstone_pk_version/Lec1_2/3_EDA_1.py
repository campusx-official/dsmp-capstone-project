#Bivariate AND Multivariate
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)
df=pd.read_csv('gurgaon_properties_cleaned_v2.csv')
df.shape
df.drop_duplicates(inplace=True)

#property_type vs price
sns.barplot(x=df['property_type'],y=df['price'],estimator=np.median)
df[df['property_type']=='flat']['price'].value_counts().sort_index()
df[df['property_type']=='flat']['price'].describe()
df[df['property_type']=='house']['price'].describe()
sns.boxplot(df['property_type'],df['price'])
#The median price of house is much higher (4.25cr) than flats(1.38cr)
#Through boxplot it can be seen that range of price of flat(0-5cr) and house(0-15cr)

#property_type vs area
sns.barplot(df['property_type'],df['built_up_area'],estimator=np.median)
sns.boxplot(df['property_type'],df['built_up_area'])
df=df[df['built_up_area'] !=737147]
#Range of built_up_area of flats is (0-3500) and of house is (0-7200) 

#property_type vs price_per_sqft
sns.barplot(df['property_type'],df['price_per_sqft'],estimator=np.median)
#flats sqft price is lower than house

#property_type vs BedRoom
cross_tab = pd.crosstab(df['property_type'],df['bedRoom'],margins=True)
cross_tab.div(cross_tab['All'],axis=0)*100
sns.heatmap(pd.crosstab(df['property_type'],df['bedRoom']))
#flats has 2,3,4 Bedroom while houses has 3,4,5,6 Bedroom

#property_type vs floornum
sns.barplot(df['property_type'],df['floorNum'],estimator=np.median)
#houses are in general having less number of floors
#1:23:00