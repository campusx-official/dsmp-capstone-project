import numpy as numpy
import pandas as pd
pd.set_option('display.max_rows', 360)
pd.set_option('display.max_columns', 360)
pd.set_option('display.max_colwidth',360)
bl=pd.read_excel('bl.xlsx')
d1=pd.read_excel('d1.xlsx')
d2=pd.read_excel('d2.xlsx')
u1=pd.read_excel('u1.xlsx')
u2=pd.read_excel('u2.xlsx')

#List comprehension
pd_columns = [f'Prob_Def_{i}' for i in range(1, 13)]
EAD_columns = [f'EAD_LT_{i}' for i in range(1, 13)]
lgd_columns = [f'lgd_pred_{i}' for i in range(1,13)]
bl_1 = bl.loc[:, ['logical_acc_id'] + pd_columns + EAD_columns + lgd_columns]
d1_1 = d1.loc[:, ['logical_acc_id'] + pd_columns + EAD_columns + lgd_columns]
d2_1 = d2.loc[:, ['logical_acc_id'] + pd_columns + EAD_columns + lgd_columns]
u1_1 = u1.loc[:, ['logical_acc_id'] + pd_columns + EAD_columns + lgd_columns]
u2_1 = u2.loc[:, ['logical_acc_id'] + pd_columns + EAD_columns + lgd_columns]

for i in range(1,13):
    bl_1.rename(columns={f'Prob_Def_{i}':f'bl_Prob_Def_{i}',f'EAD_LT_{i}':f'bl_EAD_LT_{i}',f'lgd_pred_{i}':f'bl_lgd_pred_{i}'},inplace=True)
    d1_1.rename(columns={f'Prob_Def_{i}':f'd1_Prob_Def_{i}',f'EAD_LT_{i}':f'd1_EAD_LT_{i}',f'lgd_pred_{i}':f'd1_lgd_pred_{i}'},inplace=True)
    d2_1.rename(columns={f'Prob_Def_{i}':f'd2_Prob_Def_{i}',f'EAD_LT_{i}':f'd2_EAD_LT_{i}',f'lgd_pred_{i}':f'd2_lgd_pred_{i}'},inplace=True)
    u1_1.rename(columns={f'Prob_Def_{i}':f'u1_Prob_Def_{i}',f'EAD_LT_{i}':f'u1_EAD_LT_{i}',f'lgd_pred_{i}':f'u1_lgd_pred_{i}'},inplace=True)
    u2_1.rename(columns={f'Prob_Def_{i}':f'u2_Prob_Def_{i}',f'EAD_LT_{i}':f'u2_EAD_LT_{i}',f'lgd_pred_{i}':f'u2_lgd_pred_{i}'},inplace=True)

from functools import reduce
dfs=[bl_1,d1_1,d2_1,u1_1, u2_1]
combined_df=reduce(lambda a,b:pd.merge(a,b,on='logical_acc_id',how='left'),dfs)

combined_df.describe()
column_list = combined_df.columns.tolist()

for i in range(1,13):
    combined_df[f'weighted_pd_{i}'] = 0.3*combined_df[f'bl_Prob_Def_{i}'] + 0.1*combined_df[f'd1_Prob_Def_{i}'] + 0.2*combined_df[f'd2_Prob_Def_{i}'] + 0.2*combined_df[f'u1_Prob_Def_{i}'] + 0.2*combined_df[f'u2_Prob_Def_{i}']
    combined_df[f'weighted_EAD_{i}'] = 0.3*combined_df[f'bl_EAD_LT_{i}'] + 0.1*combined_df[f'd1_EAD_LT_{i}'] + 0.2*combined_df[f'd2_EAD_LT_{i}'] + 0.2*combined_df[f'u1_EAD_LT_{i}'] + 0.2*combined_df[f'u2_EAD_LT_{i}']
    combined_df[f'weighted_lgd_{i}'] = 0.3*combined_df[f'bl_lgd_pred_{i}'] + 0.1*combined_df[f'd1_lgd_pred_{i}'] + 0.2*combined_df[f'd2_lgd_pred_{i}'] + 0.2*combined_df[f'u1_lgd_pred_{i}'] + 0.2*combined_df[f'u2_lgd_pred_{i}']

#Another method to do from 33 to 36 line
d = {'bl': 0.3, 'd1': 0.1, 'd2': 0.2, 'u1': 0.2, 'u2': 0.2}
# Initialize the new columns
for i in range(1, 13):
    combined_df[f'weighted_pd_{i}'] = 0
    combined_df[f'weighted_EAD_{i}'] = 0
    combined_df[f'weighted_lgd_{i}'] = 0
# Loop to calculate the weighted values
for i in range(1, 13):
    for key in d:
        combined_df[f'weighted_pd_{i}'] += d[key] * combined_df[f'{key}_Prob_Def_{i}']
        combined_df[f'weighted_EAD_{i}'] += d[key] * combined_df[f'{key}_EAD_LT_{i}']
        combined_df[f'weighted_lgd_{i}'] += d[key] * combined_df[f'{key}_lgd_pred_{i}']



