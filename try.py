import mymodules
import random
import urllib
import requests #Requesting info from webpage
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary

#print 3 ** 9;
#tuna = 5
#print 20+tuna;
#print '"Faizal\'s Vasaya"'
#print (r"Hey hwo are\new ") # r removes the special meaning of escape char
"""
firstname = "Faizal"
lastname = "Vasaya"
firstname+=" N."
print((firstname+ ' ' +lastname + ' ') * 5) # prints out string 5 times

user = "Tuna McFish"
print(user[0])  #String indexing starts from zero left to right
print(user[-1]) #String indexing starts from -1 from right to left
print(user[2:7]) #Get STring from start to stop position
print(user[:7])
print(len(user))
#Set
players = {23, 56, 78, 89}
#print(players) #Print entire set
#List
players = [23, 56, 78, 89]
print(players)
print(players[3])

players += [45 ,78.90, 90 +1, "myname" ] #append multiple to the list
print(players)

players.append("faizal")    #append single to the list
print(players[-1])

players[:3] = [-5 , -6 ,-8] #change the values of first 3 items
print(players)
players[:3] = [] #Delete items
print(players)
players[:] = [] #Delete all items
print(players)
#if else
age = 21
if age < 21:
    print("Sorry no beer!")
elif age > 30:
    print("Come on lets have one vodka!")

#String equality
name = "sunnyi"

if name is "faiz":
    print("Welcome man")
elif name is "sunny":
    print("Why are you here!")
else:
    print("no one here!")
#for loops
foods = ['Kadi','Paneer','Fish Curry','Biryani','Shawarma','Pepsi'];
#if statements are in the same loop indentation identifies it
for f in foods[:-1]:
    print(f)
    print(len(f))
for f in range(0,29,5-3):
    print(f)"""
#Infinite loop
"""
while 1:
    print(1)
magic=90

for n in range(0,100):
    if n%4 == 0:
        print(n , "Multiple")
#Function in python
def add(a,b):
    print("Inside the function beef")
    #print(a+b);
    return a+b
print(add(347,9));

def get_gender(sex='u'):
    if sex is 'm':
        print('Male');
    elif sex is 'f':
        print('Female')
    print(sex)
get_gender('f')
get_gender()

def add_numbers(*args):# args indicates any number of arguements
    total=0
    for f in args:
        total+=f
    return total;
print(add_numbers(23,89,98,"faizal",34))

def health_calculator(age,apples_ate,cig_smoked):
    ans = (100-age) + (apples_ate * 3.5) - (cig_smoked * 2)
    print(ans)

my_date=[27,20,0]

health_calculator(my_date[0],my_date[1],my_date[2])
health_calculator(*my_date)#unpacking an arguement list. takes each element from list and passses as an arguement

#Sets - A set cannot have duplicate items as an list can have.

groceries = {'cereal','milk','biscuit','beer','tape','lotion','beef','beer'}
print(groceries)

if 'milk' in groceries:
    print('You are milky !!')
else:
    print('No milk available !!')

clasmates = {'Tony':'cool guy','Shila' : 'TCS' , 'Mangu' : 'EMC2'}#Storing key value pairs in sets
print(clasmates['Tony'])# Accessing values using keys

for k,v in clasmates.items():# Traversing thriugh a key value pair
    print(k+ " " +v)

# print(addnumber(34,45)) cannot call a fucntion directly with name if in other file
print(mymodules.addnumber(34,56)) #Calling a function in mymodule.py
x = random.randrange(1,1000) #A function to print random numbers
print(x)


#Downloading an image file from internet

def download_web_img(url):
    file_name=random.randrange(1,1000)
    full_name = str(file_name) + ".jpg"; #Str  function converts a number into a string
    urllib.urlretrieve(url,full_name)

download_web_img('http://cdn.digital.guide/Proxy-Sites.png')

# Reading and writing a file
fw = open('file_example','w')
fw.write('Hello ! This is what you created \nVery good !!');
fw.close()

#File reading
fr = open('file_example','r')
mytext = fr.read();#Get all the contents of the file
print(mytext)
fr.close()
# Downloading a CSV file
goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=4&e=7&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_stoock_info(csv_url):
    urllib.urlretrieve(csv_url,'goo_file.csv')

download_stoock_info(goog_url)

#Building a web crawler importing BeautifulSoup
def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://christuniversity.in/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for subject_det in soup('tr',{'height':'25px'}):
            print(subject_det)
trade_spider(3)
#user input and exception handling :: please use ' ' while input
while True:
    try:
        age = int(input('What is your age?\n'))
        print(age)
        break
    except ValueError:
        print('Invalid value encountered')
    except ZeroDivisionError:
        print('Zero cannot be divided')
    except :
        print('An exception occurred !!')
    finally:
        print('Dont worry I am always executed')
#Object oriented programming using python
class Friend:   #Creating a class
    life = 3    #Instance variable

    def make_friend(self):  #Member function
        print('A new friend')
        self.life+=1

    def check_life(self):
        if self.life >= 5:
            print('Many friends found')
        else:
            print('You have' + str(self.life) + 'left')

friend1 = Friend() #Creating an object of class friend
friend1.make_friend() #Calling methods in class friend
friend1.check_life()
#Using a constructor in pyhton
class Tuna:
    def __init__(self): #Here self refers to this
        print('An object is created here')
    def  __init__(self,value):
        print('The value is' + str(value))
    def swin(self):
        print('I am swiming')
tun = Tuna(value=25)    #Calling a constructor
tun.swin()

class Girl:
    gender = 'female'       # A class variable

    def __init__(self,name):
        self.name=name            #An instance variable

r = Girl('Shina')
s = Girl('Dhimo')

print(r.gender)
print(r.name)

#Inheritance in python
class Parent:
    def print_last_name(self):
        print('Parent Name')


class Child(Parent):    #Inheriting class parent

    def child_name(self):
        print('Child')

    def print_last_name(self):  #Overrriding parent class method
        print('Parent second Name')


ch1 = Child()
pr1 = Parent()
ch1.child_name()
ch1.print_last_name()       #Accessing parent class method using base class object
pr1.print_last_name()

#MUltiple inheritance in python
class Mario:
    def move(self):
        print('I am moving!!')

class Shroom:
    def eat_shroom(self):
        print('hey ! I am big')

class BigMario(Mario,Shroom):   #MUltiple inheritance
        pass                    #No need to write anything in class by writing "pass"

bm = BigMario()
bm.move()       #Calling base class method move
bm.eat_shroom() #Calling base class method shroom

#Threading in python

import threading
class MyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            
message1 = MyMessenger(name='Sending messages\n')
message2 = MyMessenger(name='Receive messages\n')
message1.start()
message2.start()
word_count= {}
word_count['me'] = 1
word_count['we'] = 1
print(word_count)"""

dictionary = PyDictionary()
print(dictionary.synonym('name'))

