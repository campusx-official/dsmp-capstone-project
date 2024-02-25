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
#7. Class mein constructor special function hai jo 1500 magic methods mein se ek hai. Constructor ka sabse accha use hai
#(a) isme aap configuration related code likh sakte hai jisko aap apne junior ko access nhi dete
#(b) yeh automatic execute ho jaata hai. dusre method ko call karna padta hai lekin yeh automatic execute ho jaata hai

"""Ab sawal yeh hai ki self kahan-kahan lagaye??
1. 'self' constructor mein ke har variable mein use hota hai
2. 'self' ka use ek function agar kisi dusre function mein use karna hai toh self.function_name
3.  har ek function ko jab banate hai toh uske argument me 'self' daalte hai"""

"""OOPs ka golden rule yeh hai ki class ke andar 
(a) koi function apne variable ko access nhi kar sakta
(b) and, koi ek function dusre function ko call nhi kar sakta""" 
"""Isiliye self ka concept aaya hai jiska kaam yahi hai ki kisi bhi variable or function ke piche lag ke yeh mediator ke roop mein 
kisi function ko kisi variable se ya kisi function ko kisi function se interact karata hai
1.Jaise Atm wale code mein self __init__ function ko uske variable pin and balance ke saath interact karaya hai 
2.Waise hi '__init__' function 'menu' function ko use karta hai self lagake
"""

class Atm:

  #constructor
  def __init__(self):                                 
    self.pin=9876                
    self.bal=500000          
    #self.menu()                                      

  #menu
  def menu(self):
    user_input = input("""
    Hi, Welcome How can I help you?
    Press 2 to change pin
    Press 3 to check balance
    Press 4 to withdraw
    Press 5 for Anything else
    """)

    if user_input=='2':                   
      self.change_pin()                  
    elif user_input=='3':                 
      self.check_bal()                    
    elif user_input=='4':
      self.withdraw()
    else:
      exit()
  #methods
  def change_pin(self):
    old_pin=input('Enter your current pin')
    if old_pin == self.pin:
      new_pin=input('Enter new pin')
      self.pin=new_pin
      print('pin change successfully')
    else:
      print('Incorrect pin')
    self.menu()

  def check_bal(self):
    user_pin=int(input('Enter pin'))
    if user_pin==self.pin:
      print(self.bal)
    else:
      print('jasoos')
    self.menu()

obj_Atm=Atm()
obj_Atm.bal
obj_Atm.pin=89
obj_Atm.menu()
obj_Atm1=Atm()
obj_Atm1.pin
"""obj_Atm ka pin change ho gya jab aapne change kiya toh, while obj_Atm1 ka pin wahi rha jab tak ki aapne usko change nhi kiya"""
print(id(Atm()))
print(id(obj_Atm))
print(id(obj_Atm1))
"""Here is the concept 
1. of reference variable 'obj_Atm' and 'obj_Atm1' are reference variable which means this is not object this is just a variable called reference variable
which have the address of object Atm()
So, the reason why the memory addresses are changing for id(Atm()) but remaining fixed for id(obj_Atm) and id(obj_Atm1) is 
because Atm() creates a new instance of the Atm class each time it's called, while obj_Atm and obj_Atm1 likely refer to the same instance 
of the class throughout your code.
Also jo bhi humne changes kiye hai woh uss class(Atm) mein nhi hua hai, woh uss particular object(obj_Atm) mein hua hai,yeh baat prove hota hai 
agar hum ek aur object(obj_Atm1) banaye aur usme hum check kare data ko toh woh change nhi hua hota milta hai
"""
#Through OOPs map diagram we say that Class is a rule and various object can exist there called insstance of class, but by the help
#of reference variable we can point to certain one object out of many and can do the changes to that particular object,
"""So
1. Class-rule is not changing
2. All Object is also not changing
3.Only that object is changing which we have referenced"""
"""So, the object is mutable. Mutable means we have changed the object data, add variable, but id of that object is immutable.
Just like list/sets/dictionary
Aisa lagta hai ki tuple main shayad id bhi badal jaata hoga"""

obj_Atm=Atm()
a=obj_Atm.menu()
b=obj_Atm.change_pin()
c=obj_Atm.check_bal()
""" If we need to use the rule of some class then we require to have object of that class and use that object to access the function of that class
"""

def main(self, loan_id: pd.Series, projected_period: pd.Series) -> pd.Series:
""" So, overall, the main function takes two parameters (loan_id and projected_period), both of which are expected to be pandas Series objects,
and it returns a pandas Series object. The self parameter suggests that this function might be intended to be part of a class definition, 
as it is a convention in Python for methods within a class to have self as the first parameter to refer to the instance of the class."""

def main(a:int,b:int)->float:
    """ expecting integer in the argument and expecting return float """
    return float(a*b)
main(8,9)
type(main(8,9))



"""Encapsulation"""
#Encapsulation -> isme sirf aapko jo bhi variable aapne constructor mein banayae hai usme double underscore laga dena hai, jiska phayda yeh 
#hai ki koi bhi aadmi apne client ka constructor ka data change nhi kar sakega. Par agar circumstance aa gya ki change karna padega toh
#Python mein getter and setter method ke through kar sakte hai. So Encapsualation ek technique/design hai class ka code likhne ka jisme aap constructor
#ka data change karna har kisi ko allow nhi karta.   
#Encapsulation = data + getter + setter

class Atmencap:
  __counter=1
  def __init__(self):
    self.__outstanding_bal=39000
    self.__pinn=5678
    self.__cid=Atmencap.__counter
    Atmencap.__counter=Atmencap.__counter+1

obj_Atmencap1=Atmencap()
obj_Atmencap1.outstanding_bal
obj_Atmencap1.__outstanding_bal
obj_Atmencap1._Atmencap__outstanding_bal
""" '__outstanding_bal' is '_Atmencap__outstanding_bal' under the constructor/class. But outside the class this __outstanding_bal is considered as different variable like a normal one"""
obj_Atmencap1.

#obj_Atmencap1. - why can I see the variable of constructor after dot when I create an object, since in the above code I have made them public
""""In Python, even though you have used name mangling to make the attributes private by prefixing them with double underscores (__), they are not entirely inaccessible from outside the class.
When you create an instance of the class Atmencap and then use the dot (.) operator, you can still see the attributes in the list of available attributes. This is because Python does not enforce strict private access control like some other programming languages.
Name mangling in Python only changes the name of the attribute internally to avoid naming conflicts in subclasses, but it does not actually restrict access to the attribute.

Therefore, even though you have used double underscores (__) to make the attributes "private", they can still be accessed from outside the class. However, it is considered good practice not to access or modify these "private" attributes directly from outside the class to prevent unintended side effects and to encapsulate the implementation details of the class.
If you want to prevent direct access to these attributes from outside the class, you can consider using proper encapsulation techniques such as property methods or getter and setter methods."""

#Static variable is a class variable 
#and instance variable is an object variable
"""
instance variable self se start hoga jo har customer ke liye alag hota hai. ANd self hi toh object hai-> self.cid
class variable class ke naam se start hoga -> Atmencap.counter

if '__cid' variable and double underscore (__cid) variable. Python recognize this '_Atmencap__cid'
if '__counter' is a class variable then Python recognizes as 'Atmencap._Atmencap__counter'
"""
customer1=Atmencap()                #object created for customer1
customer2=Atmencap()                #object created for customer2
customer3=Atmencap()                #object created for customer3
print(customer1._Atmencap__cid)     #printing the cid variable with the help of classname since it is private
print(customer2._Atmencap__cid)
print(customer3._Atmencap__cid)
print(Atmencap._Atmencap__counter)  #Accessing the counter variable of class with the help of classname and it is private so with the help of classname we turn on the variable
print(counter)        #yeh error dega bcoz 'counter' ka naam class/constructor ke andar 'Atmencap.counter' hai
Atmencap.counter=50   #changng the variable counter of class but this is not the counter variable of class
print(Atmencap.counter)
customer4=Atmencap() 
print(customer4._Atmencap__cid)
customer5=Atmencap() 
print(customer5._Atmencap__cid)
Atmencap._Atmencap__counter=50
customer6=Atmencap() 
print(customer6._Atmencap__cid)
customer7=Atmencap() 
print(customer7._Atmencap__cid)

#Static variable (counter) and Static method (getter and setter function jo class ka method hoga)
"""
class ke method ko static methods kehte hai jisko decorator ke through highlight karwate hai

class ke variable ko static variable kehte hai
Iss method ko access karne ke liye object create nhi karna padta.
"""

#AGGREGATION and INHERITANCE
#
"""Aggregation is using object of other class when creating object. 
Aur yahin jab hum dusre ke class ko koi class mein use krte hai toh usko Inheritance kehte hai"""
#
"""obj_address = Address()
obj_customer = Customer(name,obj_address)
Customer class(main class) ka object banane ke liye aapne dusre class ka object as input bhejna

Yeh generally wahan use hota hai jahan link hai
Address to customer 
menu to Restaurant """
#
"""ek cheez gaur karne layak hai, class Customer ke niche class Address likha hai, class upar se niche nhi chalta, class niche se upar chalta hai,
yeh shayad class ke maamle mein hota hai. Kyunki function upar se niche kaam karta hai

Aggregation bhut use hota hai and kisi ke code ko padhne ke liye class map banana sabse shi hota hai. To understand the code of another guy.""" 


#Encapsulation
#Aggregation
#Inheritance
#Polymorphism
#Abstraction




#MAGIC Methods
#Yeh Class ka alag use hai-jisme aap datatype banate ho, yeh java wale ke liye hai
"""
1. Datatype banana
2. Magic methods used
3. '+','-' operator directly trigger to the method in the class
"""
class Fraction:
  #constructor which takes input
  def __init__(self,x,y):
    self.num=x
    self.den=y
  #humne numerator and denominator bana liya lekin jab hum x & y jab input denge toh humara object 'fr1' x/y dikhna chahiye,
  #pad x/y dikhne ke liye hume iss class ke andar ek print function daalna hoga tabhi toh yeh aisa dikhega. Toh iska matlab list, tuple, set classes
  #classes ke andar bhi creator ne print function banaya hoga tabhi toh list [] iss bracket ke andar dikhta hai
  def __str__(self):
    return '{}/{}'.format(self.num,self.den)
  #adding two fraction and adding more fraction by args
  def __add__(self,other):
    new_num=self.num*other.den + other.num*self.den
    new_den=self.den*other.den
    return '{}/{}'.format(new_num,new_den)               #agar hum self.num and self.den ko new_num and new_den se replace krte then self.str() function yahan kaam nhi krta
  #subtraction
  def __sub__(self,other):
    new_num=self.num*other.den - other.num*self.den
    new_den=self.den*other.den
    return '{}/{}'.format(new_num,new_den)
  #multiplication
  def __mul__(self,other):
    new_num=self.num*other.num
    new_den=self.den*other.den
    return '{}/{}'.format(new_num,new_den)
  #divison
  def __truediv__(self,other):
    new_num=self.num*other.den
    new_den=self.den*other.num
    return '{}/{}'.format(new_num,new_den)
  #one more method which will not take not any input and return the float value of the fraction
  def convert_to_decimal(self):
    return self.num/self.den

fr1=Fraction(3,4)         #iss point pe constructor run ho gya lekin abhi str magic method run nhi hua
fr2=Fraction(1,2)  

print(fr1)
print(fr2)
print(fr1+fr2)
print(fr1*fr2)
