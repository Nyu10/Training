    #Python Syntax Excercises
print("Hello World!")
if 5>2:
    print ("Five is greater than two!")
    #Python Comments Excercises

#this is a comment
"""this is a comment
using multiple lines
"""
    #Python Variables Excercises
carname = "Volvo"
x=50
x=5
y=10
print(x+y)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#A variable name cannot start with a number (2myvar = "John" does not work)
def myfunc():
    global x
    x = "fantastic"

    #Python Data Types Excercises

x=5 #x is an int
x="hello World" #x is a str
x=20.5 #x is a float
x = ["apple","banana","cherry"] #x is a list
x = ("apple", "banana", "cherry") #x is a tuple? tuple is a collection which is ordered and unchangeable
x = {"name" : "John", "age" : 36}#x is a dictionary
x = True #x is a boolean

    #Python Numbers Excercises
x=5
x=float(x)#converts into decimal
x=5.5
x=int(x)#converts into integer
x=5
x=complex(5)#converts into complex number
    #Python Strings Excercises
x = "Hello World"
print(len(x)) #length of string x
txt = "Hello World"
x = txt[0]  #first character of the string txt
txt = "Hello World"
x =txt[2:5] #Get the characters from index 2 to index 4 (llo).
txt = " Hello World "
x = txt.strip() #Without white space
txt = "Hello World"
txt = txt.upper() #value of txt to upper case.
txt = "Hello World"
txt = txt.lower() #value of txt to lower case
txt = "Hello World"
txt = txt.replace("H","J") #Replace the character H with a J.
age = 36
txt = "My name is John, and I am {}" #.format lets you replace the {} with the argument
print(txt.format(age))
    #Python Boolean Excercises
# Any string is True except empty strings, Any number is true except zero, Any list, tuple, set and dictionary are true except empty ones

    #Python Boolean Excercises

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!") #in checks if apple is in the list
if 5 == 10 or 4 == 4: # or is the operator
  print("At least one of the statements is true")

    #Python List Excercises
print(fruits[1]) #prints second item in fruits list
fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi" #Change the value from "apple" to "kiwi", in the fruits list.
fruits.append("orange")# adds orange to end of list
fruits.insert(1,"lemon")#Use the insert method to add "lemon" as the second item in the fruits list.
fruits.remove("banana")#removes banana
print(fruits[-1])#prints last item
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])#prints indexes 2 to 5 in the list
print(len(fruits)) #len of fruits

    #Python Sets Excercises Sets are {} are unordered and unindexed
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) #combines them
print (fruits)
fruits.remove("banana")#if the item does not exist, remove will give an error
fruits.discard("banana")# if item does not exist, discard will not give an error
    #Python Dictionaries Excercises Sets are {} are unordered and unindexed
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(car.get("model")) #prints model
car["year"]=2020 #changes year 
car["color"]="red" #adds key value pair 
car.pop("model") #removes model
i = 1
    #Python Functions
while i < 6:
  if i == 3:
      break #breaks if i==3
  i += 1
for x in fruits: #for loop
  print(x)
def my_function(): #function
  print("Hello from a function")
class MyClass: #class
  x = 5  
p1 = MyClass() #object
print(p1.x) #uses p1 object to print value of x
#init function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#class Student(Person): #creates class that will inherit Person

#import mymodule as mx refers to module as mx