import numpy as np
import pandas as pd
#CONTENT - PRINT
#Print command read the string, number, list as it is. And output the word as a list, string and number
#Print command output ko kisi khaas format mein sentence likhta hai {} {}.format. Jo output string jaisa dikhta hai
print('Stock is {} and it belongs to {} sector'.format(Stock,Sector))
#Python mein har ek datatype ke element/value ke beech mein comma ka zaroorat padta hai. 'Print', 'List', 'Tuple','Sets',dictionary
print([1,34,4]+[94.98,3,9])
#String converted to list by split function and uses 'apply' command taking input function as a object
df['price']=df['price'].str.split(' ').apply(treat_price)
np.NaN or None #Both represent missing, however np.NaN is used as a missing for numerical operation while None is more general and commonly used to represent absence or missing values in Python objects
a=input("kuch input do bhai: ")
print("output: ", a)

#If s is string, then what this both refers s.python_command() and python_command(s)?
#s.python_command(): -> python_command behaving as an inbuilt function under class s. s may be string, List, dictionary
#This expression assumes that "s" is an instance\object of a class that has a method called "python_command." The dot notation (s.python_command()) is used to access a method or attribute of an object. In this case, it is invoking the "python_command" method on the object represented by "s." The method could be defined within the class of "s" or be inherited from a parent class. The exact behavior of the method depends on its implementation.
#python_command(s): -> python_command behaving as an external command
#This expression assumes that "python_command" is a standalone function that takes a string argument. The expression "python_command(s)" is calling or invoking the function "python_command" and passing the string variable "s" as an argument. The function "python_command" can then perform operations or computations using the provided string argument.
#In summary, "s.python_command()" suggests that "python_command" is a method associated with the object "s," while "python_command(s)" implies that "python_command" is a standalone function that takes a string argument.

#Python mein kahan atakte hai -
#sabse pehle pata hona chahiye ki 's' ka datatype kya hai
#uske baad kaun kaun se method/function/command uss s mein built-in hai
#uske baad uss command ke bracket ke andar koi value ki zaroorat hai
#Example -
print(['hello', 'Delhi'].join("--"))   -> This will give error-> 'list' object has no attribute 'join'
print("---".join(['hello', 'Delhi']))  -> While this will not give error -> bcoz "---" this is a string which has inbuilt method join which takes
                                          #list as an argument
#Thus, we can say print() is an external command

#UNDERSTANDING THE DESIGN of attribute,method of class 'pandas'
#data.unique -> unique is a method we are not calling it we are referencing it
#data.unique() -> unique is a method we are calling
#data.columns -> columns is not a method it is an attribute
#This method and attribute belong to object of  data class

class pd (                           #pd class is defined
class DataFrame (                    #Under class pd, DataFrame class is defined under which some attributes and method1 is defined, this will be used by object 'DataFrame'
attribute1
def method1())
def method2()                          #Under pd class, method2 is defined
)

#Ex-> method2 are pd.read_excel(), pd.merge()
#Ex-> method1 are data.unique(), data.rename()
#Ex-> attribute1 are data.columns, data.shape

#Pandas mein incorporated jo 'apply' function hai  woh most important function hai data science wale logon ke liye, kyunki hum sab dataframe pe kaam karte hai
#aur hume multiple column mein se kisi ek column ke each values ko treatment(function apply) karna hota hai, toh uske liye hum apply function use karte hai
1.data['column1'].apply(f)                        #f is a seperate function
2.data['column1'].apply(lambda input:output)
Ex-  movies.apply(lambda x: x.split()[0].upper())
Ex-  df['price'].str.split(' ').apply(treat_price)

#How to find if the account number is in data?Some of the suggestion
series_data[series_data.values=='Daaka']            #for series only b'coz Series has two elements index and values
series_data['Daaka']                                #for series, if 'Daaka' is an index
df[df.values=='A59296758']
df[df['property_id'].isin(['L47956793','S50764468','A59296758'])]
df[df['property_id'].isin(['L47956793','A59296758'])].index             #Series.index
np.where(df.values=='S50764468')                    #Why this works? df is dataframe, since df.values is a form of ndarray, each row is an 1-d array
df.iloc[8,0:]

#Series and Dataframe mein sabse bada difference?
series_data[5:7]                      #yeh to 1darray hota hai toh kaam chal jaata hai
dataframe_data.iloc[5:7,0:]           #isme loc and iloc ka sahara lena padta hai to extract a patch of rows and column
dataframe_data.values[5][7]                  #df.values is a 2d-array thus it traverse like an arrays

"""
datatype like int, float, string
Haan, list aur dictionary bhi Python mein data types hote hain. Yeh dono container data types hote hain jo multiple values ko store karne ki capability rakhte hain.

1. storing the individual values like int, float,string 
2. collection of object like storing the collection of int,float,string, list, dictionary, user- defined object 

"""

#Dictionary and Series and DataFrame difference?
#Dictionaries D has D.keys() and D.values() while Series S has S.index and S.values. without brackets
#D.keys() type are dict_keys and D.values() type are dict_values. Both are not of list type
#S.index is (not a list, it is pandas index type) and S.values is a array. Thus we can traverse like list. Thus, there are command like sort_values() and sort_index()
#Dataframe df has df.columns, df.index. Also, df.values work is python. In case of renaming it, we need to write if it is column or index
#Traversing elements in list and dataframe is like
#for i in list1:
#    print(i)   #it will print all the elements of the list
#for col in dataframe1:
#    print(col)  # it will print the column names of the dataframe 
# This will help us to see all the column names without having fullstop ....
# Also we get to know how to traverse in a dataframe 
analysis.rename(columns={'CMP':'CMP_Rs', 'MarCap_Cr':'MarCap_Cr_Rs'})

#String is identified by Python interpretor as -> a = ''
#String datatype can be split the word on the basis of /. And output it on list
#String datatype can concatenated the word on the basis of -. And output it as string
#String can be trimmed. And output it as string
#String can be transformed into list
movies['genres'].str.split('|').apply(lambda x:'Action' in x)   #The .str.split('|') method can be applied directly to a Pandas Series of strings to perform the split operation on each individual string within the Series, returning a Series of lists.
type(subs['genres'].str.split('|')[1])          #how to find type of the individual elements of returned series of lists
df['society'].apply(lambda x:str(x).split(' '))[0]      #Series[0]
df['society'].apply(lambda x:str(x).split(' ')[0])      #Series each element str[0]

#Number is identified by Python interpretor as -> a = 388

#List is identified by Python interpretor as -> a = []
#List contain any kind of datatype. While array contain same kind of datatype
#As the name suggest it will be list. List comprehension F=[Output loop condition]
#List does not behave like vector. In place of this, Numpy array behaves like vector. Meaning, vector addition, subtraction, multiplication,dot,cross possible in array and not in list
#List comprehension F=[Output loop condition], if F is dictionary then bracket in RHS used as {}
squares = {x: x*x for x in range(1, 6)}
#If you are dealing with one list/datatype L1 then you can use list comprehension, but what if you have to deal with three list then use list comprehension with zip function
#zip is an external function which in backend store the elements of first from this list and first from other list,second from this list and second from other list, Example -> List comprehension using zip using three different list,
L=[i+j+k for i,j,k in zip(L1,L2,L3)]
furnishings_df = df[['furnishDetails'] + columns_to_include]      #since columns_to_include is a list thus it works to sum the list

#Array bhi ek tarah ka datatype hai. Jo pd.Series mein use hota hai. Since Pandas, scikit np.array ke upar hi bana hai
#Array ki kuch khass baat, ek toh yeh same data type rakhta hai,np.array([1,4,6,6]), yeh aise hi create hota hai
#Iske paas ek special power hai reshape, transpose,transformation krne ka jo list ke paas nhi hai. Agar yeh sab kaam list pe kiye jayenge toh uska output array mein convert ho jayega
#np.reshape(L,(2,2))  where L is list .This code will reshape the list L into a 2x2 array and store it in reshaped_array
#np.exp(L) .The result will be a new array containing the exponential values of each element in the original list. exp(L) will not work
#Mujhe lagta hai since list can have different datatype, so isme exp() jaisa function nhi banaya. While numpy has it

#In summary, lists are mutable, allowing you to modify their elements, add new elements, or remove existing elements. Tuples, on the other hand, are immutable, meaning that their elements cannot be changed once the tuple is created.
df.shape is a tuple and not list. So it cannot be edited/change by me.
#However, you can add some elements(addition something is not an edit) to the existing tuple by using '+' sign. However, '+' sign works if both parties are of same datatype.
#And we know set is mutable thus 'add' and 'remove' method is written there, but elements is immutable thus index position is not there
#Basically, mujhe lagta hai ki list ka jo class banaya gya hai python mein usme append, pop, sort, changing the element ka function likha hua hai
#while, tuple class mein yeh saare function nhi likhe hue hai, jiske kaaran hum inme change nhi kar paate, jiske kaaran isko immutable keh dete hai

#List is all about passing a group of values and dynamic storing and modification of data.
#Tuples is group of values, but you don't modify the data
#Sets is to store and manipulate a collection of distinct values and perform set operations such as union, intersection, and difference.
#Dictionary is about assigning a value/weights corresponding to something/categories
# -Rating Excellent=1, Very good=2 ,good=3 ,Average=4
#Dictionary mein indexing se koi value nhi milta yahan pe indexing mein keys likhna padta hai- Ex-> d3[1] will not work while d3['college'] will give IIT. It is kind of analogous to list but you are deciding what would be the index
#Dictionary is also flexible like list- Accessing, Adding,editing,deleting
#List and Tuples are ordered collections of elements" means that the elements are stored in a specific sequence, and you can access or retrieve them based on their position in the collection using indices.

d={'p1':'I','p2':'me','p3':'mine'}
d[1]
d['p2']
for i in d:
    print(i)            #print keys
    print(d[i])         #print values

d.keys()
d.values()  


#if-else mein 'then' use nhi hota usme then ke badle colon use hota hai, ek aur baat colon ke baad dusre line mein jaane ki zaroorat nhi hai, usi line pe aage ki baat likh sakte ho
#Function -> Function -> what is the objective of making function and argumrnts(of three type variable,args,kwargs)
#            for loop -> for i(elements) in datatype(list,range,tuples,dictionary,sets)
#            elements -> datatype ke elements ke saath kya operation karna hai
#            return -> final result(which might be element,list,dictionary)
#Yahan pe function mein teen cheeze padhenge -> Function running for loop on data types
#                                               Function mein pass global or local variable(datatype)
#                                               Nested Function
#There is difference between Nested loop and Nested function.
#Nested function ka example -> maine ek number pass kiya kisi main function mein woh number apne aap check karke pata kar lega ki mujhe kis function mein jaana hai aur kya output dena hai

#value_counts()-> categories , isnull().sum()-> missing values, shape-> total values. You have to do this for a column -> proc freq replacement
1.df['facing'].value_counts()
1a. df['property_type'].value_counts(normalize=True)                  #value_counts in terms of percentage
1b. df['society'].value_counts(normalize=True).cumsum()               #The sum value is 1
2.df['facing'].isnull().sum()
3.df.shape
4.type(df['facing'][1])  => whether it is list or string we can do treatment on the basis of that
5.df['facing'].sample(5) => Look at the values bcoz, value_counts will give so many categories which is of no use thus look at the elements of columns
6.df.duplicates().sum()  => To check in the overall data whether it contains duplicates rows
7. If else condition-> df['attrition']=np.where(df['event']=='Close',1,0)
#For every column we need to check above six thing

a='l'
if type(a)==int:
    print('if condition ka yeh bhi use hai,jo mujhe pata nhi tha')
else:  print('aapne string daala hai')   

#proc sql group by
final_attr_seg=df.groupby(['segment']).agg({'act_bal_cap':'mean',
                                            'pred_bal_cap':'mean',
                                            'attrition':'count'}).reset_index()

#value_count jab bhut zyada ho toh usko bhi club krke modified value_count bana sakte hai in form of dictionaries

#This way we can take output of value_counts as a DataFrame
a = df['sector'].value_counts()[df['sector'].value_counts() >=3]
a = df['sector'].value_counts()[df['sector'].value_counts().values >=3]       #This will also work

#This way we can filter accountid of current dataset taking reference of accountid from different data
a = df['sector'].value_counts()[df['sector'].value_counts() >=3]
df = df[df['sector'].isin(a.index)]

#all_nan_df is another dataset and df is another dataset. You have fill missing value of a variable in all_nan_df. Now, you want to impute the same missing variable in df data then we can use df.update command
df.update(all_nan_df)

'hello-world'.replace('-',' ')   -> output -> 'hello world'     bcoz, 'hello-world' is automatically is a string
1 df['sector'].str.replace('-',' ')                      #df['sector'].str-> In Pandas, the .str accessor is used to perform vectorized string operations on a Series containing strings. When applied to a Series, it provides access to various string methods and functions that can be applied to each element of the Series efficiently, without needing to loop through each element individually.
2 df['sector'][1].replace('[','').replace(']','')                 bcoz, df['sector'][1] is automatically is a string not a series like 'hello-world'
3 df['sector'].str.replace('-',' '): Here, str.replace() is applied to a Pandas Series (df['sector']), so the str accessor is necessary to indicate that you're using a string method on each element of the Series.
'hello-world'.replace('-',' '): This is a simple string operation in regular Python. Since it's not part of a Pandas DataFrame or Series, there's no need for the str accessor. You're directly using the replace() method on a single string.
#Bcoz of .apply() method of Pandas we can apply any treatment to a column/series .Since,When applied to a Pandas Series, .apply() can execute a function element-wise on each value in the Series.
#4 DataFrame column -> string -> list -> list.extend() -> set -> List Comprehension
all_furnishing=[]
for detail in df['furnishDetails'].dropna():
    furnishings = detail.replace('[','').replace(']','').replace("'",'').split(', ')
    all_furnishing.extend(furnishings)
unique_furnishings = list(set(all_furnishing))

if sector: return x         # Checking if 'sector' exists or evaluates to True
columns_to_include = [furnishings for furnishings in columns_to_include if furnishings]         #list comprehension
# if sector or if furnishings means if sector is true, true is automatically understood by Python

#For each column of data frame we can do
#1. cleaning the column -> replace space/string, treatment of string
#2. Feature engineering -> making new columns , a weighted score

#sabse pehle fist data ko filter kiya on the basis of column jis mein null values hai
temp_df = df[df['features'].isnull()]
#uske baad dono data ko merge kiya on the basis of column name, aur uss merge dataset ko maine dataframe ke form mein nhi liya usko series form mein le liya
x = temp_df.merge(app_df,left_on='society',right_on='PropertyName',how='left')['TopFacilities']          #Series
#phir maine loc use krke main dataset ke column mein row-wise data fill kar diya uss series(series mein index and values hoti hai) ke values ko
df.loc[temp_df.index,'features'] = x.values
#Let's see how much columns we have covered and how much left
df.iloc[3000:3005,10:]
#filtering non numeric values
non_numeric_matches = ipl[ipl['MatchNumber'].astype(str).str.isdigit() == False]
#arranging data on the basis of two column
subs.sort_values(['year_of_release','title_x'],ascending=[True,False])
#f-literals is important
pd_columns = [f'Prob_Def_{i}' for i in range(1, 13)]
bl_1 = bl.loc[:, ['logical_acc_id'] + pd_columns]
for i in range(1,13):
    bl_1.rename(columns={f'Prob_Def_{i}':f'bl_Prob_Def_{i}',f'EAD_LT_{i}':f'bl_EAD_LT_{i}',f'lgd_pred_{i}':f'bl_lgd_pred_{i}'},inplace=True)
#reduce function is important to merge 5 datsets at a time
from functools import reduce
dfs=[bl_1,d1_1,d2_1,u1_1, u2_1]
combined_df=reduce(lambda a,b:pd.merge(a,b,on='logical_acc_id',how='left'),dfs)
#full list of column
combined_df.describe()
column_list = combined_df.columns.tolist()


#dictionary and list
df_dict=pd.DataFrame(
    {
    'col1':['access','activa','tvs','yamaha'],
    'col2':['125cc','110cc','125cc',np.nan],
    'col3':[112000,97000,110000,108000]
    }
)

L=[
    ['India',80,170],
    ['USA',70,165],
    ['Africa',75,180],
    ['China',90,190]
]
df_list= pd.DataFrame(L,columns=['Countries','avg.age','avg.height',])

# Create a DataFrame with specific shape (rows x columns) filled with NaN
rows = 5
cols = 3
null_df = pd.DataFrame(np.nan, index=range(rows), columns=range(cols))
null_df.iloc[1:3,0:2]=10

#Working with date and time variable
score_month = 202311
from datetime import datetime
from dateutil.relativedelta import relativedelta
year=int(str(score_month)[0:4])
month=int(str(score_month)[4:6])
day=1
dt=(datetime (year,month,day) + relativedelta(months=month))
dt_1=dt.strftime('%Y%m')
dt_2=int(dt_1)
dt_3=dt.strftime("%Y-%m-%d")
dt_4=dt.strftime("%d/%m/%Y")
type(dt_4)

#Python has dtype datetime64 like int,float,string
#It's format is like 2024-01-10
#Changes 01/10/2024 to 2024-01-10
rows = 5
cols = 3
null_df = pd.DataFrame(np.nan, index=range(rows), columns=range(cols))
null_df.iloc[1:3,0:2]=10
null_df_1=null_df.rename(columns={0:'col1'})
null_df_1.loc[0,'col1']= dt_4
null_df_1.loc[1,'col1']= dt_4
null_df_1.loc[2,'col1']= dt_4
null_df_1.info()
null_df_1['col1']=pd.to_datetime(null_df_1['col1']) 
type(null_df_1['col1'][0])
null_df_1.info()

#How to get end day of month and difference of month??
#dt_end=datetime (year,month,day) + relativedelta(months=month))

#Output and path joining
df.to_csv('gurgaon_properties_cleaned_v2.csv')
Path="C:/Users/Piyush/OneDrive/Desktop/tut_python"
file_path = os.path.join(Path, "v_300.csv")
v_3.to_csv(file_path)

import os
os.getcwd()
os.chdir(Path)
#Reading excel file having multiple sheet, sas file without importing sas7bdat and importing code and {}->format( , , ) and %s->%( , , )
os.chdir(r'C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning')
date=202311
bl_sas=pd.read_sas(r"C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning/{}/{}_v1/bl_d_{}.sas7bdat".format(date,date,date),format='sas7bdat',encoding='')
bl_sas_latin=pd.read_sas(r"C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning/%s/%s_v1/file_%s.sas7bdat" %(date,date,date),format='sas7bdat',encoding='latin1')
file_excel=pd.read_excel(r'C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning/{}/{}_v1/file_{}.xlsx'.format(date,date,date),sheet_name=None,engine='openpyxl')
bl_sas_latin=pd.read_excel(r"C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning/%s/%s_v1/file_%s.xlsx" %(date,date,date),sheet_name=None,engine='openpyxl')

file_excel.keys()
file_excel.values()
file_excel.items()
num=file_excel['bl']['Prob_Def_4'][1]
type(file_excel)        #dict
type(file_excel['bl'])  #DataFrame
type(file_excel['bl']['Prob_Def_4'])    #Series
type(file_excel['bl']['Prob_Def_4'][1]) #float64
#Reading code or importing code
F=__import__('func'+str(date))
type(F)
F.is_even(81)
F.is_even(5000)


#Writing excel file with multiple sheet
other_path = r'C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning'
bl=pd.read_excel(other_path + '/bl.xlsx')
d1=pd.read_excel(other_path + '/d1.xlsx')
d2=pd.read_excel(other_path + '/d2.xlsx')
u1=pd.read_excel(other_path + '/u1.xlsx')
u2=pd.read_excel(other_path + '/u2.xlsx')
bl=bl.set_index('logical_acc_id')   #Indexes automatically comes as a output in python.Thus, to have consistency in datasets we need to ensure no automatic indexes should present.
date=202311
os.chdir("C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning/{}/{}_v1/".format(date,date))
with pd.ExcelWriter('file_{}.xlsx'.format(date)) as writer:
    bl.to_excel(writer,sheet_name='bl')
    d1.to_excel(writer,sheet_name='d1')
    d2.to_excel(writer,sheet_name='d2')
    u1.to_excel(writer,sheet_name='u1')
    u2.to_excel(writer,sheet_name='u2')

#Popularly used
bl.columns
type(bl.columns)            #It is pandas.Index  
bl.columns=[col.lower() for col in bl.columns]  #ran successfully
bl.shape  
bl.shape[1]=361             #Error:'tuple' object does not support item assignment

del bl_1,bl_sas_latin,file_excel            #deleting the datasets to empty the memory
bl_drop=bl.drop(columns=['lgd_pred_120'])    #like rename
bl.lgd_pred_117                              #new way of choosing column
bl.lgd_pred_117.mean()
bl.describe().transpose()
bl['lgd_pred_120'].loc[bl['lgd_pred_120']>0.5] =10000   #without creating new column replace the rows value

bl['ranking'] = pd.qcut(bl['prob_def_1'], q=10, labels=range(1, 11))
bl[['ranking','prob_def_1']].groupby('ranking').describe()

pick_two_col=dict(zip(bl['lgd_pred_120'],u1['Prob_Def_1'])) #zip is also a datatype
bl_drop=(u1[['logical_acc_id','Prob_Def_1']]).set_index('logical_acc_id').to_dict()    #like rename

pivot=pd.pivot_table(bl,columns='ranking',values='prob_def_1',index='ranking_1',aggfunc='count')
pd.melt
bl['ranking_1']=bl['ranking'].shift(-1)





