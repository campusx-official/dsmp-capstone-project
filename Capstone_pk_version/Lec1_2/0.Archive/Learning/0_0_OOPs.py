import numpy as np
import pandas as pd

L=[1,3,5]                   #[ ], this symbol is called literal
M=list((7,9,5))             #list() is an object of class list(which is written in Python)

#customise datatype banane ka phayda kya hai
#1. ek toh class ka naam apne hisab se rakh sakte jisse yaad ho jaat hai ki kisko call karna hai
#Ex-> agar ECL code run karna hai toh then we must have PD class formed in python so that we provide data, pdcurve, macroeconomics data to 
#calculate PD. When we have to calculate PD on certain data then just call pd object an instance of pd class and that will provide a series of pdscore 
#2. Thus, different class should be formed in python like forming LGD class, EAD class, Staging class, ECL class so that provide required
#data and macrovariable to have a series of LGD score, EAD score, staging classification table and ECL series column. By series word I mean to get 
#one column returned from calling each object from each class
#3. uss class ke andar usi tarah ke function likhe jaate hain jaise LGD ke andar ka method(function) hoga LGD1, LGD2, recovery index
#while PD ke andar function be like PD12m, LTPD, linearly regressed with macrovariable etc., aise function milenege
#4. Humlog dekh sakte hai ki different components means differnt class banaya hai ek IFRS9 model suite mein
#5. It will tell agar kisi model mein dikkat hoga toh we can detect the error.
#6. Basically, Class ka use wahin hai jab model suite mein bhut saare components hote hain and unn components ke bhi multiple subcomponents hote hai
#iske do phayde hai 1. ki har ek subcomponents  ke prati ek class bana denge aur usko hum apna naam de denge taaki hum yaad rakh sake aur 
#second phayda yeh hai ki hum har ek subcomponents mein ek exception handling daal denge jisse hume pata chal jayega ki kis subcomponent se error aa rha hai
  

class MyAtm:
