# Importing package, option setup, path setup
import numpy as np
import pandas as pd
import re
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',None)

import os
os.getcwd()
#path= r'C:\Users\Piyush\OneDrive\Desktop\Capstone\Lec1'
#dir=os.listdir(path)
#dir
#os.chdir(path)


# reading data
df=pd.read_excel('flats.xlsx')
df.shape
df.info()    #to check missing value and datatype of each columns
df.duplicated().sum()
df['property_id'].duplicated().sum()      #duplicate account_id
dupout=df[df['property_id'].duplicated()]
df = df.rename(columns={'area':'price_per_sqft'})
#df.rename(str.lower,axis=1,inplace=True)
df['society'].value_counts()
df['society'].value_counts().shape

#society variable -> Wanted to eliminate decimal number(3.8),?space?, symbol like star at the end of sentence and also make it lower for uniformity
import re
df['society'] = df['society'].apply(lambda x: re.sub(r'\d+(\.\d+)?\s?★', '', str(x)).strip()).str.lower()
df['society'].apply(lambda x:str(x).split(' '))[0]      #Series[0]
df['society'].apply(lambda x:str(x).split(' ')[0])      #Series each element str[0]

#price variable converted string Lac to Crore to list and applied a function as a object
df['price'].value_counts()     #There are lacs, crore, Price on request variable
df['price']
df = df[df['price'] != 'Price on Request']
def treat_price(x):
    if type(x) == float: return x
    else:
        if x[1] == 'Lac': return round(float(x[0])/100,2)       #Here x is a string
        else: return round(float(x[0]),2)
df['price']=df['price'].str.split(' ').apply(treat_price)

#price_per_sqft variable
df['price_per_sqft'].value_counts()
df['price_per_sqft']=df['price_per_sqft'].str.split('/').str.get(0).str.replace('₹','').str.replace(',','').str.strip().astype('float')
#Note: It is converted into float and not int,bcoz int requires no missing value but here are missing values so it will throw error

#bedroom, bathroom, balcony, additionalRoom, floorNum
df['bedRoom'].value_counts()
df['bedRoom'].isnull()
df=df[~df['bedRoom'].isnull()]
df.shape
df['bedRoom']=df['bedRoom'].str.split(' ').str.get(0).astype('int')

df['bathroom'].value_counts()
df['bathroom'].isnull()
df['bathroom']=df['bathroom'].str.split(' ').str.get(0).astype('int')

df['balcony'].value_counts()
df['balcony'] = df['balcony'].str.split(' ').str.get(0).str.replace('No','0')

df['additionalRoom'].value_counts() 
df['additionalRoom'].isnull().sum()
df['additionalRoom'] = df['additionalRoom'].fillna('not available')
df['additionalRoom'].value_counts().shape 
df['additionalRoom'] = df['additionalRoom'].str.lower()

df['floorNum'].value_counts()
df['floorNum'] = df['floorNum'].str.split(' ').str.get(0).str.replace('Ground','0').str.replace('Lower','0').str.replace('Basement','-1').str.extract(r'(\d+)')

df['facing'].value_counts()
df['facing'].isnull().sum()
df['facing'] = df['facing'].fillna('NA')

# Created a new column(not at the end, but in between)
df.insert(loc=4,column='area',value=round((df['price']*10000000)/df['price_per_sqft']))
df.insert(loc=1,column='property_type',value='flat')
df.to_csv('flats_cleaned.csv')

#merging two datasets-> flats_cleaned and house_cleaned
houses = pd.read_csv('house_cleaned.csv')
flats = pd.read_csv('flats_cleaned.csv')
df = pd.concat([flats,houses],ignore_index=True)
df = df.drop(columns=['link', 'property_id'])

df.insert(loc=3,column='sector',value=df['property_name'].str.split('in').str.get(1).str.replace('Gurgaon','').str.strip().str.lower())
df['sector'].value_counts()

df['sector'] = df['sector'].str.replace('dharam colony','sector 12')
df['sector'] = df['sector'].str.replace('krishna colony','sector 7')
df['sector'] = df['sector'].str.replace('suncity','sector 54')
df['sector'] = df['sector'].str.replace('prem nagar','sector 13')
df['sector'] = df['sector'].str.replace('mg road','sector 28')
df['sector'] = df['sector'].str.replace('gandhi nagar','sector 28')
df['sector'] = df['sector'].str.replace('laxmi garden','sector 11')
df['sector'] = df['sector'].str.replace('shakti nagar','sector 11')

df['sector'] = df['sector'].str.replace('baldev nagar','sector 7')
df['sector'] = df['sector'].str.replace('shivpuri','sector 7')
df['sector'] = df['sector'].str.replace('garhi harsaru','sector 17')
df['sector'] = df['sector'].str.replace('imt manesar','manesar')
df['sector'] = df['sector'].str.replace('adarsh nagar','sector 12')
df['sector'] = df['sector'].str.replace('shivaji nagar','sector 11')
df['sector'] = df['sector'].str.replace('bhim nagar','sector 6')
df['sector'] = df['sector'].str.replace('madanpuri','sector 7')

df['sector'] = df['sector'].str.replace('saraswati vihar','sector 28')
df['sector'] = df['sector'].str.replace('arjun nagar','sector 8')
df['sector'] = df['sector'].str.replace('ravi nagar','sector 9')
df['sector'] = df['sector'].str.replace('vishnu garden','sector 105')
df['sector'] = df['sector'].str.replace('bhondsi','sector 11')
df['sector'] = df['sector'].str.replace('surya vihar','sector 21')
df['sector'] = df['sector'].str.replace('devilal colony','sector 9')
df['sector'] = df['sector'].str.replace('valley view estate','gwal pahari')

df['sector'] = df['sector'].str.replace('mehrauli  road','sector 14')
df['sector'] = df['sector'].str.replace('jyoti park','sector 7')
df['sector'] = df['sector'].str.replace('ansal plaza','sector 23')
df['sector'] = df['sector'].str.replace('dayanand colony','sector 6')
df['sector'] = df['sector'].str.replace('sushant lok phase 2','sector 55')
df['sector'] = df['sector'].str.replace('chakkarpur','sector 28')
df['sector'] = df['sector'].str.replace('greenwood city','sector 45')
df['sector'] = df['sector'].str.replace('subhash nagar','sector 12')

df['sector'] = df['sector'].str.replace('sohna road road','sohna road')
df['sector'] = df['sector'].str.replace('malibu town','sector 47')
df['sector'] = df['sector'].str.replace('surat nagar 1','sector 104')
df['sector'] = df['sector'].str.replace('new colony','sector 7')
df['sector'] = df['sector'].str.replace('mianwali colony','sector 12')
df['sector'] = df['sector'].str.replace('jacobpura','sector 12')
df['sector'] = df['sector'].str.replace('rajiv nagar','sector 13')
df['sector'] = df['sector'].str.replace('ashok vihar','sector 3')

df['sector'] = df['sector'].str.replace('dlf phase 1','sector 26')
df['sector'] = df['sector'].str.replace('nirvana country','sector 50')
df['sector'] = df['sector'].str.replace('palam vihar','sector 2')
df['sector'] = df['sector'].str.replace('dlf phase 2','sector 25')
df['sector'] = df['sector'].str.replace('sushant lok phase 1','sector 43')
df['sector'] = df['sector'].str.replace('laxman vihar','sector 4')
df['sector'] = df['sector'].str.replace('dlf phase 4','sector 28')
df['sector'] = df['sector'].str.replace('dlf phase 3','sector 24')

df['sector'] = df['sector'].str.replace('sushant lok phase 3','sector 57')
df['sector'] = df['sector'].str.replace('dlf phase 5','sector 43')
df['sector'] = df['sector'].str.replace('rajendra park','sector 105')
df['sector'] = df['sector'].str.replace('uppals southend','sector 49')
df['sector'] = df['sector'].str.replace('sohna','sohna road')
df['sector'] = df['sector'].str.replace('ashok vihar phase 3 extension','sector 5')
df['sector'] = df['sector'].str.replace('south city 1','sector 41')
df['sector'] = df['sector'].str.replace('ashok vihar phase 2','sector 5')

df['sector'].value_counts().count()
a = df['sector'].value_counts()[df['sector'].value_counts() >=3]
df = df[df['sector'].isin(a.index)] 

df['sector'] = df['sector'].str.replace('sector 95a','sector 95')
df['sector'] = df['sector'].str.replace('sector 23a','sector 23')
df['sector'] = df['sector'].str.replace('sector 12a','sector 12')
df['sector'] = df['sector'].str.replace('sector 3a','sector 3')
df['sector'] = df['sector'].str.replace('sector 110 a','sector 110')
df['sector'] = df['sector'].str.replace('patel nagar','sector 15')
df['sector'] = df['sector'].str.replace('a block sector 43','sector 43')
df['sector'] = df['sector'].str.replace('maruti kunj','sector 12')
df['sector'] = df['sector'].str.replace('b block sector 43','sector 43')

df['sector'] = df['sector'].str.replace('sector-33 sohna road','sector 33')
df['sector'] = df['sector'].str.replace('sector 1 manesar','manesar')
df['sector'] = df['sector'].str.replace('sector 4 phase 2','sector 4')
df['sector'] = df['sector'].str.replace('sector 1a manesar','manesar')
df['sector'] = df['sector'].str.replace('c block sector 43','sector 43')
df['sector'] = df['sector'].str.replace('sector 89 a','sector 89')
df['sector'] = df['sector'].str.replace('sector 2 extension','sector 2')
df['sector'] = df['sector'].str.replace('sector 36 sohna road','sector 36')

df = df.drop(columns=['property_name','address','description','rating'])
df.to_csv('gurgaon_properties_cleaned_v1.csv',index=False)







########################################Feature engineering##################################################################

#Our focus is feature eng. of 1.areaWithType, 2.additionalRoom, 3.agePossession, 4.furnishDetails, 5.features
df = pd.read_csv('gurgaon_properties_cleaned_v1.csv')




##   1.areaWithType    ##
# This function extracts the Super Built up area
def get_super_built_up_area(text):
    match = re.search(r'Super Built up area (\d+\.?\d*)',text)
    if match:
        return match.group(1)
    else: return None

# This function checks if the area is provided in sq.m. and converts it to sqft if needed
def convert_to_sqft(text, area_value):
    if area_value is None:
        return None
    match = re.search(r'{} \((\d+\.?\d*) sq.m.\)'.format(area_value), text)
    if match:
        sq_m_value = float(match.group(1))
        return sq_m_value * 10.7639  # conversion factor from sq.m. to sqft
    return area_value

df['super_built_up_area'] = df['areaWithType'].apply(get_super_built_up_area)
df['super_built_up_area'].isnull().sum()
df['super_built_up_area'] = df.apply(lambda x: convert_to_sqft(x['areaWithType'], x['super_built_up_area']), axis=1)
df['super_built_up_area'].isnull().sum()

# This function extracts the Built Up area or Carpet area
def get_area(text, area_type):
    match = re.search(area_type + r'\s*:\s*(\d+\.?\d*)', text)
    if match:
        return float(match.group(1))
    return None 

df['built_up_area'] = df['areaWithType'].apply(lambda x: get_area(x,'Built Up area'))
df['built_up_area'] = df.apply(lambda x: convert_to_sqft(x['areaWithType'], x['built_up_area']), axis=1)

df['carpet_area'] = df['areaWithType'].apply(lambda x: get_area(x,'Carpet area'))
df['carpet_area'] = df.apply(lambda x: convert_to_sqft(x['areaWithType'], x['carpet_area']), axis=1)

#To get an idea in how much columns have all three values
df[['property_type','areaWithType','super_built_up_area','built_up_area','carpet_area']].sample(5)
df[~((df['super_built_up_area'].isnull()) | (df['built_up_area'].isnull()) | (df['carpet_area'].isnull()))].shape

all_nan_df = df[((df['super_built_up_area'].isnull()) & (df['built_up_area'].isnull()) & (df['carpet_area'].isnull()))]
all_nan_index = df[((df['super_built_up_area'].isnull()) & (df['built_up_area'].isnull()) & (df['carpet_area'].isnull()))].index

#Data knowledge -> 
#Carpet area
#Built up area -> Carpet area + Wall + balcony
#Super Built up area -> Built up area + staircase + lift area
#Plot area will come under Built area, Also Plot area is measured in yard in data
#Thus, we need to plot area information in Built up area
df[(df['areaWithType'].str.contains('Plot')) & (df['built_up_area'].isnull())].sample(5)
def extract_plot_area(area_with_type):
    match = re.search(r'Plot area (\d+\.?\d*)',area_with_type)
    if match:
        return float(match.group(1))
    else: None
all_nan_df['built_up_area'] = all_nan_df['areaWithType'].apply(extract_plot_area)   

all_nan_df['built_up_area'].isnull().sum()
def convert_scale(row):
    if np.isnan(row['area']) or np.isnan(row['built_up_area']):
        return row['built_up_area']
    else:
        if round(row['area']/row['built_up_area']) == 9.0:
            return row['built_up_area'] * 9
        elif round(row['area']/row['built_up_area']) == 11.0:
            return row['built_up_area'] * 10.7
        else: return row['built_up_area']
all_nan_df['built_up_area'] = all_nan_df.apply(convert_scale,axis=1)    

# update the original dataframe
df.isnull().sum()
df.update(all_nan_df)
df.isnull().sum()




##   2.additionalRoom    ##
df['additionalRoom'].value_counts()
#List of new columns to be created
new_cols = ['study room','servant room','store room','pooja room','others']
for col in new_cols:
    df[col] = df['additionalRoom'].str.contains(col).astype(int)





##   3.agePossession    ## - Every variable need to paas through this two command for the first overview
df['agePossession'].value_counts()
df['agePossession'].isnull().sum()
d=df['agePossession'].value_counts()[df['agePossession'].value_counts()>=0]
#d.to_csv('value_counts.csv')    #to take value_counts output in excel
#v=int('2024-12-01 00:00:00'.split(" ")[-1])
def categorize_age_possession(value):
    if pd.isna(value):
        return "Undefined"
    if "0 to 1 Year Old" in value or "Within 6 months" in value or "Within 3 months" in value:
        return "New Property"
    if "1 to 5 Year Old" in value:
        return "Relatively New"
    if "5 to 10 Year Old" in value:
        return "Moderately Old"
    if "10+ Year Old" in value:
        return "Old Property"
    if "Under Construction" in value or "By" in value:
        return "Under Construction"
    try:
        # For entries like 'May 2024'
        int(value.split(" ")[-1])
        return "Under Construction"
    except:
        return "Undefined"
df['agePossession1'] = df['agePossession'].apply(categorize_age_possession)
df['agePossession1'].value_counts()   






##   4.furnishDetails    ##
df['furnishDetails'].str.replace('[','').str.replace(']','').str.replace("'",'').str.split(', ')
type(df['furnishDetails'][1].replace('[','').replace(']','').replace("'",'').split(', '))         #Output -> list
df['furnishDetails'][1].replace('[','').replace(']','').replace("'",'').split(', ')[3]            #Output -> 1 Geyser

# Extract all unique furnishings from the furnishDetails column
#DataFrame column -> string -> list -> list.extend() -> set ->List COmprehension
all_furnishing=[]
for detail in df['furnishDetails'].dropna():
    furnishings = detail.replace('[','').replace(']','').replace("'",'').split(', ')
    all_furnishing.extend(furnishings)
unique_furnishings = list(set(all_furnishing))
# Simplify the furnishings list by removing "No" prefix and numbers by using List comprehension F=[Output loop condition]
columns_to_include = [re.sub(r'No |\d+','', furnishings).strip() for furnishings in unique_furnishings]
columns_to_include = list(set(columns_to_include))   # Get unique furnishings
columns_to_include = [furnishings for furnishings in columns_to_include if furnishings]

# Define a function to extract the count of a furnishing from the furnishDetails
def get_furnishing_count(details,furnishing):
    if isinstance(details,str):                      #if detail datatype is string 
        if f"No {furnishing}" in details:
            return 0
        pattern=re.compile(f"(\d+) {furnishing}")
        match=pattern.search(details)
        if match:
            return int(match.group(1))
        elif furnishing in details:
            return 1
    return 0   

for furnishing in columns_to_include:
    df[furnishing]=df['furnishDetails'].apply(lambda x: get_furnishing_count(x,furnishing))

# Create the new dataframe with the required columns
furnishings_df = df[['furnishDetails'] + columns_to_include]     #since columns_to_include is a list thus it works to sum the list
furnishings_df.shape    
furnishings_df.drop(columns=['furnishDetails'],inplace=True)
#This furnishings_df data is used in k-means clustering to get an idea a row will assign to which cluster
#Firstly, on the basis of k-means clustering we will figure out how many optimal cluster is required to group the data
#To find an optimal cluster we require to find the speed of slope of the graph is steadily decrease

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(furnishings_df)


wcss_reduced = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(scaled_data)
    wcss_reduced.append(kmeans.inertia_)

# Plot the results
plt.figure(figsize=(12, 8))
plt.plot(range(1,11), wcss_reduced, marker='o', linestyle='--')
plt.title('Elbow Method For Optimal Number of Clusters (Reduced Range)')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

n_clusters = 3       #on looking at the graph it is decided to take 3 as optimal class, and also by intution it is giving furnished, semi-furnished, Unfurnished

# Fit the KMeans model n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(scaled_data)

# Predict the cluster assignments for each row
cluster_assignments = kmeans.predict(scaled_data)
counts = np.unique(cluster_assignments, return_counts=True)

df = df.iloc[:,:-18]
df['furnishing_type'] = cluster_assignments
df.loc[[3344,3054,3400,3179,3397],['furnishDetails','furnishing_type']]
# 0 -> unfurnished
# 1 -> semifurnished
# 2 -> furnished




##   5.features   ##
df[['society','features']].sample(5)
df['features'].value_counts()
df['features'].isnull().sum()
type(df['features'][1])

#We can fetch missing data of features from apartment data
#sabse pehle fist data ko filter kiya on the basis of column jis mein null values hai
#uske baad dono data ko merge kiya on the basis of column name, aur uss merge dataset ko maine dataframe ke form mein nhi liya usko series form mein le liya
#phir maine loc use krke main dataset ke column mein row-wise data fill kar diya 

app_df = pd.read_csv('appartments.csv')
app_df.info()
app_df['PropertyName']=app_df['PropertyName'].str.lower()

temp_df = df[df['features'].isnull()]                   #635

x = temp_df.merge(app_df,left_on='society',right_on='PropertyName',how='left')['TopFacilities']          #481 null value and only series of TopFacilities is there

df['features'].isnull().sum()                    #635
df.loc[temp_df.index,'features'] = x.values      
df['features'].isnull().sum()                    #481

# Convert the string representation of lists in the 'features' column to actual lists
from sklearn.preprocessing import MultiLabelBinarizer
import ast
# Convert the string representation of lists in the 'features' column to actual lists
df['features_list'] = df['features'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) and x.startswith('[') else [])
type(df['features_list'][4])                #it has converted string into list

# Use MultiLabelBinarizer to convert the features list into a binary matrix
mlb = MultiLabelBinarizer()
features_binary_matrix = mlb.fit_transform(df['features_list'])

# Convert the binary matrix into a DataFrame
features_binary_df = pd.DataFrame(features_binary_matrix, columns=mlb.classes_)
features_binary_df.shape
features_binary_df.to_csv('features_binary_df.csv')

#First Approach: k means Clustering
wcss_reduced = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(features_binary_df)
    wcss_reduced.append(kmeans.inertia_)
# Plot the results
plt.figure(figsize=(12, 8))
plt.plot(range(1,11), wcss_reduced, marker='o', linestyle='--')
plt.title('Elbow Method For Optimal Number of Clusters (Reduced Range)')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()    
#2 cluster is enough by looking at the graph - we were planning for 3 clusters - Luxurious, semi-luxurious, budget society. Also if we are assigning 
#2 cluster to data then 1 cluster is taking the Nan values and other cluster is filled values.

#So, we have decided to give a luxury score to each society
# Define the weights for each feature as provided
# Assigning weights based on perceived luxury contribution
weights = {
    '24/7 Power Backup': 8,
    '24/7 Water Supply': 4,
    '24x7 Security': 7,
    'ATM': 4,
    'Aerobics Centre': 6,
    'Airy Rooms': 8,
    'Amphitheatre': 7,
    'Badminton Court': 7,
    'Banquet Hall': 8,
    'Bar/Chill-Out Lounge': 9,
    'Barbecue': 7,
    'Basketball Court': 7,
    'Billiards': 7,
    'Bowling Alley': 8,
    'Business Lounge': 9,
    'CCTV Camera Security': 8,
    'Cafeteria': 6,
    'Car Parking': 6,
    'Card Room': 6,
    'Centrally Air Conditioned': 9,
    'Changing Area': 6,
    "Children's Play Area": 7,
    'Cigar Lounge': 9,
    'Clinic': 5,
    'Club House': 9,
    'Concierge Service': 9,
    'Conference room': 8,
    'Creche/Day care': 7,
    'Cricket Pitch': 7,
    'Doctor on Call': 6,
    'Earthquake Resistant': 5,
    'Entrance Lobby': 7,
    'False Ceiling Lighting': 6,
    'Feng Shui / Vaastu Compliant': 5,
    'Fire Fighting Systems': 8,
    'Fitness Centre / GYM': 8,
    'Flower Garden': 7,
    'Food Court': 6,
    'Foosball': 5,
    'Football': 7,
    'Fountain': 7,
    'Gated Community': 7,
    'Golf Course': 10,
    'Grocery Shop': 6,
    'Gymnasium': 8,
    'High Ceiling Height': 8,
    'High Speed Elevators': 8,
    'Infinity Pool': 9,
    'Intercom Facility': 7,
    'Internal Street Lights': 6,
    'Internet/wi-fi connectivity': 7,
    'Jacuzzi': 9,
    'Jogging Track': 7,
    'Landscape Garden': 8,
    'Laundry': 6,
    'Lawn Tennis Court': 8,
    'Library': 8,
    'Lounge': 8,
    'Low Density Society': 7,
    'Maintenance Staff': 6,
    'Manicured Garden': 7,
    'Medical Centre': 5,
    'Milk Booth': 4,
    'Mini Theatre': 9,
    'Multipurpose Court': 7,
    'Multipurpose Hall': 7,
    'Natural Light': 8,
    'Natural Pond': 7,
    'Park': 8,
    'Party Lawn': 8,
    'Piped Gas': 7,
    'Pool Table': 7,
    'Power Back up Lift': 8,
    'Private Garden / Terrace': 9,
    'Property Staff': 7,
    'RO System': 7,
    'Rain Water Harvesting': 7,
    'Reading Lounge': 8,
    'Restaurant': 8,
    'Salon': 8,
    'Sauna': 9,
    'Security / Fire Alarm': 9,
    'Security Personnel': 9,
    'Separate entry for servant room': 8,
    'Sewage Treatment Plant': 6,
    'Shopping Centre': 7,
    'Skating Rink': 7,
    'Solar Lighting': 6,
    'Solar Water Heating': 7,
    'Spa': 9,
    'Spacious Interiors': 9,
    'Squash Court': 8,
    'Steam Room': 9,
    'Sun Deck': 8,
    'Swimming Pool': 8,
    'Temple': 5,
    'Theatre': 9,
    'Toddler Pool': 7,
    'Valet Parking': 9,
    'Video Door Security': 9,
    'Visitor Parking': 7,
    'Water Softener Plant': 7,
    'Water Storage': 7,
    'Water purifier': 7,
    'Yoga/Meditation Area': 7
}
weights.keys()
weights.values()
# Calculate luxury score for each row of features_binary_df
luxury_score = features_binary_df[list(weights.keys())].multiply(list(weights.values())).sum(axis=1)
type(luxury_score)
df['luxury_score'] = luxury_score
df.shape
df.info()
df.to_csv('gurgaon_properties_cleaned_v2.csv')
