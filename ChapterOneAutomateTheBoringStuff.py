# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:29:21 2021

@author: mmagg
"""


"""
Chapter One of Automate the boring stuff with Python
By AL Stweigart
Notes taken by Maggie Dooley

expressions consist of values, and operatorsand can always evaluate down to a single value
data tyoe is a category for values and every value belongs to exactly one data type
string concatenation = when + is used on two string values it joins the strings
"""

Name = 'Maggie' + 'Dooley'
print(Name)

"""
can't concatenate string and number, 'Maggie" + 42 = error
will have to explicitly convert 42 to a string to concatenate
string replication using * sign with string times one INTEGER value
"""
print('Alice'*5)

"""
variable is like a box in the computer's memory where you can store a single value
assignment statement: store values in variables with equal = sign
a variable is initialized the first time a value is stored in it
variable names: it can be only one word, it can use only letters, 
numbers and underscore characters also can't begin with a number
hyphens, spaces, special characters, can't begin with number not allowed
variable names are case-sensitive
"""
#this program says hellow and asks for my name
print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you')
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+1)+ ' in a year.')

#when there are no more lines of code to execute, the python program terminates
"""
with print('hello world') when python execture this line, you could say Python is 
calling the print() function and the string value is being passed to the function, 
a value that is passed to a function call is an argument
can print either string or integer, not float or concatenated string and integer
"""
#print('I am' + 29 + 'years old')
"""
the above will produce an error, + can add or conctenate strings
 we use str(), int(), or float() functions to convert data types
 the int() function is also useful if you need to round a floating-point number down
"""
print('I am ' + str(29)+' years old')
#int() rounds 7.7 down to 7
print(int(7.7))


"""
the input() function waits for the user to type some text on the keyboard and press 
ENTER
"""
#int(), str() and input() functions in effect
print('What is your age') #asks for their age
myAge = input()
print('You will be ' + str(int(myAge)+1)+ ' in a year.')

"""
You can pass the len() function a string value or variable containing string 
and the function evaluates to the integer value of the number of characters in that string
"""
#flow control: what code to run, what code to skip, and what code to repeat 
#based on the values it has