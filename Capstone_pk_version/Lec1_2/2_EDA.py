
#EDA ->Univariate AND Pandas profiling 
# Importing package, option setup, path setup
import numpy as np
import pandas as pd                     #barplot,pie-plot
import re
import matplotlib.pyplot as plt         #plot(x,y)                # module.function    
import seaborn as sns                   #histplot,boxplot,barplot(x,y)
#from sklearn.preprocessing import StandardScaler.fit_transform()
#Package/library-> sklearn is a package or library in Python
#Subpackage -> preprocessing
#Module-> StandardScaler
#Function/Method-> fit_transform()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',None)

import os
os.getcwd()
#path= r'C:\Users\Piyush\OneDrive\Desktop\Capstone\Lec1'
#dir=os.listdir(path)
#dir
#os.chdir(path)

df=pd.read_csv('gurgaon_properties_cleaned_v2.csv')
df.shape
df.info()
df.drop(columns=['Unnamed: 0','Unnamed: 0.1'],inplace=True)
df.duplicated().sum()
df.drop_duplicates(inplace=True)

df['property_type'].value_counts().plot(kind='bar')   
df['property_type'].value_counts(normalize=True)    
#Observation1: flats are 76% and house are 23%


df['society'].value_counts(normalize=True)
df['society'].value_counts(normalize=True).cumsum()
df[df['society'] != 'independent']['society'].value_counts().head(10).plot(kind='bar')     #top 10 popular society/brands
a_10_50 = df['society'].value_counts()[(df['society'].value_counts() <=50) & (df['society'].value_counts() >=10)]
#value_count jab bhut zyada ho toh usko bhi club krke modified value_count bana sakte hai in form of dictionaries
society_counts = df['society'].value_counts()       #Total 676 categories hai
society_bins_dict = {"Very High(>100)":(society_counts > 100).sum(),
                  "High (50-100)": ((society_counts >= 50) & (society_counts <= 100)).sum(),
                  "Average (10-49)": ((society_counts >= 10) & (society_counts < 50)).sum(),
                  "Low (2-9)": ((society_counts > 1) & (society_counts < 10)).sum(),
                  "Very Low (1)": (society_counts == 1).sum()
                  }
society_bins_dict
df['society'].isnull().sum()
#Observation2: 
#Total 676 categories hai iss column mein
#1.There is 1 missing value 
#2.13% of data belongs to independent society category
#3.Variability(category) in data: 676 category mein 1 category(independent) aisi hai,jo 100+ rows mein available hai, 676 category mein 2 category aisi hai jo 50-100 rows mein available hai
#676 category mein 92 category aisi hai,jo 10-49 rows mein available hai and inn saare categories ka sum 676 hoga and rows ka sum 3681 

df['sector'].value_counts().shape       #Total 114 categories 
df['sector'].value_counts().head(10).plot(kind='bar')
sector_counts=df['sector'].value_counts()
sector_bins_dict = {"Very High(>100)":(sector_counts > 100).sum(),
                  "High (50-100)": ((sector_counts >= 50) & (sector_counts <= 100)).sum(),
                  "Average (10-49)": ((sector_counts >= 10) & (sector_counts < 50)).sum(),
                  "Low (2-9)": ((sector_counts > 1) & (sector_counts < 10)).sum(),
                  "Very Low (1)": (sector_counts == 1).sum()
                  }
df['sector'].isnull().sum()
#Observation3: 
#1.Total 114 categories hai iss column mein
#2. 3 category aisa hai out of 114 categories mein jo 100+rows mein available hai, 25 category aisa hai out of 114 categories mein jo 50+rows
# mein available hai, 63 categories aisa hai out of 114 categories mein jo 10+rows mein available hai

df['price'].isnull().sum()      #17 missing
df['price'].describe()
Quantiles=df['price'].quantile([0.05,0.9,0.95,0.99])
sns.histplot(df['price'],kde=True,bins=50)
sns.boxplot(x=df['price'], color='lightgreen')
skewness=df['price'].skew()
kurtosis=df['price'].kurt()
#Observation4:
#1. 17 missing hai iss column mein
#2. 50% property 1.5cr ke niche hai
#3. 25% property 95lkh ke niche hai
#4. 75% property 2.75cr ke niche hai
#5. baaki 25% property 2.75cr ke upar hai
#6. Std. deviation is 2.98 (high variability)
#7. data skewed hai high prices ke taraf matlab 5.9cr se pehle 90%population covered hai baaki(10%) population 5.9cr+ ke baad distributed hai
#8. The box plot showcases the spread of the data and potential outliers. Properties priced above approximately 10cr might be considered outliers
# as they lie beyond the upper whisker of the box plot.
#9. Skewness is 3.27 indicating +ve skew. This means the distribution tail is skewed to the right which means most population have prices on the
#lower end (left side) and few properties have prices on high-priced (right side)
#10. Kurtosis is 14.93 > 3. Which means a distribution with heavier tails and more outliers compared to normal distribution
#11. So the 'price' column is not normally distributed. Noted here, we generally demand y-variable to be normally distributed in linear reg
#To find mode price of flats, meaning most of the flats are available at what price, as we already know that median price is 1.5cr but we want to know at granular level with interval is 50lkh or price distribution
price_bins_dict = {"0-1cr":(df['price']<=1).sum(),
                   "1-1.5cr":((df['price']>1) & (df['price']<=1.5)).sum(),
                   "1.5-2cr":((df['price']>1.5) & (df['price']<=2)).sum(),
                   "2-3cr":((df['price']>2) & (df['price']<=3)).sum(),
                   "3-5cr":((df['price']>3) & (df['price']<=5)).sum(),
                   "5+cr":(df['price']>5).sum() }
pd.Series(price_bins_dict).plot(kind='bar')                 #pd.DataFrame will not work here since Dataframe is multiple column thing, series is a one column thing so it worked
#Most flats belongs to 0-1cr(1000+)

#ecdf plot => cumulative density function (y-axis is cumulative sum of value_counts frequency, x-axis is the index value)
ecdf = df['price'].value_counts().sort_index().cumsum() / len(df['price'])
plt.plot(ecdf.index,ecdf)

#identify potential outliers using IQR method - I think data is not normally distributed thus mu plus minus sigma will not apply for outlier 
#thus identifying cutoff of outliers using IQR
Q1 = df['price'].describe()['25%']              #type(df['price'].describe()['25%'])
Q3 = df['price'].describe()['75%']
IQR = Q3 - Q1
lower_bound = Q1 -1.5*IQR
upper_bound = Q3 +1.5*IQR
range_of_outliers = [lower_bound, upper_bound]        #[-1.75,5.45] is the range , matlab ki 5.45cr ke upar property ko outlier keh rhe hai
outliers = df[(df['price'] >= upper_bound) | (df['price'] <= lower_bound)]      
outliers.shape                                        #(425, 29)
#So, many outliers so ,Studying the outliers 
outliers['price'].describe()
sns.histplot(outliers['price'],kde=True,bins=20)

#Since this is right skewed data so applying log transformation to make it normal distribution
#We have applied log10 => log(1+0.7) to avoid x-axis to go to negative
sns.histplot(df['price'],kde=True,bins=50)
sns.histplot(np.log1p(df['price']),kde=True,bins=50)    #range has been reduced from 31 to 3.5
sns.boxplot(df['price'])
sns.boxplot(np.log1p(df['price']))


df['price_per_sqft'].describe()   #The median is Rs.9000 The std.deviation is 23210, which is very very high, high variablility
sns.histplot(df['price_per_sqft'],kde=True,bins=100)        #Data is right skewed
sns.boxplot(df['price_per_sqft'])                           #Some of the outliers are abnormal
df['price_per_sqft'].isnull().sum()
#Observation4:
#There are 17 missing values
#The median is Rs.9000 The std.deviation value is 23210, which is very very high variablility
#Data is right skewed
#Some of the outliers are abnormal


df['bedRoom'].isnull().sum()                    #0 missing
df['bedRoom'].value_counts(normalize=True)
df['bedRoom'].value_counts().plot(kind='pie',autopct='%0.2f%%')  
df['bathroom'].isnull().sum()                    #0 missing
df['bathroom'].value_counts(normalize=True)
df['balcony'].isnull().sum()
df['balcony'].value_counts(normalize=True)  
#Observation5:
#3BHK(40%) is most popular followed by 2BHK(25%). 5BHK(6%) is more than 1BHK(3%)
#3+ and 3 balcony is 30% while 2 balcony is 25%, 1 balcony is 9%

#Let's see how much columns we have covered and how much left
df.iloc[3000:3005,10:]

df['floorNum'].describe()
df['floorNum'].quantile([0.95,0.98,0.99])
sns.boxplot(df['floorNum'])
df['floorNum'].value_counts()     
#Observation6:
#boxplot will give you the cutoff value below which floornum value is popular and after cutoff potential outlier exist. The cutoff is 23 floor
#15 flats is at 23 floor

df['facing'].isnull().sum()
df['facing'].value_counts()
#Observation7: East and North facing are popular, followed by west and south. South facing are very less likely 
#1048 value is missing


df['agePossession1'].value_counts(normalize=True)
#Observation8:
#Most properties(50%) belong to 1-5 yrs, followed by new property(16%) belong to 0-1 yrs. That means this might be the investors, these are not the end users.
#Under construction property is 3%. 
#It means that there is high probability(50%+16% = 66%) of flats which belong between 0-5yrs are likely to sale
#12% properties are undefined


df['super_built_up_area'].isnull().sum()/len(df['super_built_up_area'])     
df['super_built_up_area'].describe()
sns.histplot(df['super_built_up_area'],kde=True,bins=50)
sns.boxplot(df['super_built_up_area'])
#Observation9:
#50% value is missing
#Std. is 764
#Mean is 1924 and Median is 1828. This value told us about shrinkflation i.e. how low the flat size in an area
#Through boxplot and 25%-75% range (from describe command) is 1478-2215. This will again tell about shrinkflation range
#Almost normal dist.

df['built_up_area'].isnull().sum()/len(df['built_up_area'])     
df['built_up_area'].describe()
sns.boxplot(df['built_up_area'])
#Observation10:
#54% value is missing
#Std. is 17932
#Mean is 2378 and Median is 1650. Not seems like normal distributions
#25%-75% range (from describe command) is 1100-2400
#There is one value which is not outlier, a data error

df['carpet_area'].isnull().sum()/len(df['carpet_area']) 
df['carpet_area'].describe()
sns.boxplot(df['carpet_area'])
#Observation11:
#49% value is missing
#Std. is 22787
#25%-75% range (from describe command) is 845-1790
#Mean is 2528 and median is 1300
#Seems 3 data error

#which columns left to analyze
df.iloc[10:15,20:]

binary_columns = df[['study room','servant room','store room','pooja room','others']]
# Plotting pie charts for each column
for column in binary_columns:
    counts = df[column].value_counts()         # Calculate counts of 0s and 1s for the column
    # Create a pie chart
    plt.figure()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Pie chart for {column}')
    plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle
    plt.show()
#Observation12:
#36% rows has servant room
#19% rows has study room   
#17% rows has pooja room
#9% rows has store room
#11% rows has others

df['furnishing_type'].value_counts()      
# 0 -> unfurnished  => 1057
# 1 -> semifurnished => 206
# 2 -> furnished     => 2418
#Observation13:
#The number are matching but classification is different for campusx - 0=> 2411, 1=>1059, 2=>207

df['luxury_score'].isnull().sum()           #0
df['luxury_score'].value_counts().sort_index()
df['luxury_score'].describe()
sns.histplot(df['luxury_score'],kde=True,bins=50)  
sns.boxplot(df['luxury_score']) 
#Observation14:
#This is a multimodal, peak at 50 and 150
#No outliers
#25%-75% range is 31-110 luxury score.
#Std. is 53

#What we have found -> Missing values treatment and Outliers(or data error)
#2nd part of class is about pandas profiling
#Pandas profiling is a library which perform EDA report
#conda install pandas-profiling
from pandas_profiling import ProfileReport

# Load your dataset
df = pd.read_csv('gurgaon_properties_cleaned_v2.csv').drop_duplicates()

# Create the ProfileReport object
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

# Generate the report
profile.to_file("output_report.html")





  





