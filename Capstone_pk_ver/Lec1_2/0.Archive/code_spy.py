
import numpy as np
'''Importing numpy'''
print ("numpy is imported")
'''Importing numpy'''
import pandas as pd
print ("Pandas is imported")
datt = pd.read_csv("C:/Users/Piyush/OneDrive/Desktop/tut_python/tut_venv/movies.csv")
datt
datt.shape
datt.info()
def datt_exclusion(data):
    v_1= data[data["runtime"]>'140']
    v_2= v_1[v_1["runtime"]>'170']
    return v_2
v_3= datt_exclusion(datt)
print ("Hekdn",np.arange(1,10))
import os
Path="C:/Users/Piyush/OneDrive/Desktop/tut_python"
file_path = os.path.join(Path, "v_300.csv")
v_3.to_csv(file_path)
LogisticRegression()
    