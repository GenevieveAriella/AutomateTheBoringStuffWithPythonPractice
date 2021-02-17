# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:36:14 2021

@author: mmagg

Chapter Two of Automate the boring stuff with Python
By AL Stweigart
Notes taken by Maggie Dooley

Boolean values are True and False
If you use lower case or use True or False as variable names, youget error message

Comparison Operators: compare two values and evaluate down to a single Boolean value

"""
#below expression True
print(42.0 == 42)
#below expression False
print(42 == '42')

#boolean operators are and, or, not
# and, or are binary operators
#not operator operates on only one boolean value, evalutes to its opposite

print(not True)

#can nest not operators
print(not not not True)

#order of operations is any not operators first, then and, then or
#conditions: evaluate down to a boolean value, True or False

"""
blocks of code:
    blocks begin when the indentation increaee
    blocks can contain other blocks
    blocks end when the indentation decreases to xero or to a containing blocks
    indentation
"""
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted')
    else: 
        print('Worng password')
    
#program execution: term for current instruction being executed
"""
if statement components:
    the if keyword
    a condition (that is, an expression that evaluates to True or False)
    a colon
    starting on the next line, an indented block of code (called the if clause)
    
elif: always follows an if or elif statement.  It provides 
another condition that is checked only if all of the previous conditions were false

it is not guarenteed that at least one of the clauses will be executed when only 
if-elif-elif clause, when there is a chain of elif statements, only one or none 
of the clauses will be executed.  Once one of the statements condition;s is found to 
be True, the rest of the elif clauses are automatically skipped

the order of the elif statements does matter
"""

if name == 'Alice':
    print('Hi, Alice.')
    
"""
else clause is executed only when the if statement's condition is False
the else clause, a colon, starting on the next line, an indented block of code

elif statement always follows an if or another elif. statement.  It provides another 
condition that is only checked if all preceding conditions false.  One one of the
statements conditions are found to be True, the rest of the elif clauses are skipped,
so order of the elif statements does matter, or you can have an else statement after 
the last elif.  In that case it is guarenteed that at least one (and only one) of the 
clauses will be executed

Always exactly one if statement.  Any elif statements you need shold follow the if 
statement.  Second, if you want to be sure that at least one clause is executed, close
the structure with an else statement
"""
age = 13
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not ALice, grannine')
elif age > 2000:
    print('Unlike you, ALice is not an undead immortal vampire') 
else:
    print('You are not Alice')
    
"""
the while keyword, a condition, a colon, starting on the next line, an indented block 
of code

in the while loop, the condition is always checked at the start of each iteration
(that is, each time the loop is executed)

"""
name = ''
while name !='your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


"""
break statements: the execution to break out of a while loop's clause early. 
If the execution reaches a break statement, it immediately exits the while loop's
clause
"""

#creates an infinite loop; it is a while loop whose condition is always True.  
#The program execution will always enter the loop and will exit it only when a 
#break statement is executed
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        #if this is true, the execution moves out of the loop to print 'Thank you'
        break
print('Thank you!')

"""
continue statements are used inside loops.  When the program execution reaches 
a continue statement, the program execution immediately jumps back to the start
 of the loop
"""
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        #if True, has to jump back to while loop
        continue
    print('Hello, Joe.  What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
    print('Access granted.')

"""
for loop if you want to execute a block of code only a certain number of times
elements it needs:
    the for keyword
    a variable name
    the in keywork
    a call to range method
    a colon
    for clause starting on the next line an indented block of code
"""

total = 0
for num in range(101):
    total = total + num
print(total)

#can put start and end as arguments in range function
for i in range(12,16):
    print(i)
    
#start, stop, and step argument in range function
for i in range(0, 10, 2):
    print(i)

"""
importing modules: each module is a python program that contains a related
group of functions that can be embedded in your programs.  Before you can use
the functions in a module, you must import the module with:
        -the import keyword
        -the name of the module
        -optionally, more module names, as long as they are separated by commas
        
an alternative form of import statement is composed of the from keyword,
followed by the module name, the import keyword, and a star; for example,
from random import *
with this form, calls to functions in random will not need the random.prefix.  
However, using the full name makes for more readable code, so it is better to use 
the normal form of the import statement
        
"""
import random, sys
for i in range(5):
    print(random.randint(1,10))
    
while True:
    print('Type exit too exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You type' + response + '.')
    
    
    