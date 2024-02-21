#same logical acc number comes multiple times(for some acc it comes 4 times for some it comes 6 times etc.)
#multiple segment 1,2,3,4
#flag for close and default for attrition
#Output -> to mean the bal on the basis of logical account number 
#Output -> segment wise mean bal

import numpy as np
import pandas as pd
df=pd.read_excel("C:/Users/Piyush/OneDrive/Documents/GitHub/dsmp-capstone-project/Capstone_pk_version/Lec1_2/0.Archive/Learning/Attrition.xlsx")
df.sample(5)
df['attrition']=np.where(df['event']=='Close',1,0)
df['event'].value_counts()
df['event'].isnull().sum()
df['attrition'].value_counts()
df['act_bal_cap']=df['act_bal']/df['ead_cap']
df['pred_bal_cap']=df['pred_bal']/df['ead_cap']
final_attr=df.groupby(['logical_acc_num','segment']).agg({'act_bal_cap':'mean',
                                              'pred_bal_cap':'mean',}).reset_index()
final_attr_seg=df.groupby('segment').agg({'act_bal_cap':'mean',
                                            'pred_bal_cap':'mean',
                                            'attrition':'count'}).reset_index()
#how to name these
final_attr_seg=df.groupby('segment').agg(actual=('act_bal_cap','mean'),predicted=('pred_bal_cap','mean')).reset_index()