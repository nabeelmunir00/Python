# Input, Output & Operators

name = "nabeel"
age = 21
# format string 
print(f"my name is {name} and my age is {age}")

print("Hello my name is",name,"and my age is" ,age)

inputValue =  input('Hello bro how are you!:')

print(f"Value of input: {inputValue}" )

# Arithmetic Operatores
# number - int , float ,complex
# (+,-,/,//,*,%,,**)

value1 = 10
value2 = 20

print(value1 + value2) # => 10 + 20 = 30 
print(value1 - value2) # => 10 - 20 = -10 
print(value1 / value2) # => value return karta ha float ma

# agher hum ko int ma value chaye. to hum // ka use kare ga 

print(value1 // value2) # => int ma value return karta ha 

print(value1* value2) # => 10 x 20 = 
print(value1** value2) # => agher hum ko kis power add karna ha to hum  =

print(value1 % value2) # hum ko mode return karta ha

"""
BoardMark Rules
() -> Brackets
** -> Exponent (right to left: 2**2**3 = 2**(2**3))
* / // % -> Multiplication,Division,Floor Division
"""

# Comparison Operators 
# (==,>=,<=,!=, > ,< )

print(10 > 5)
print(10 == 100)
print(10>=20)
print(10<=20)
print(10 != 20)

# Logical Operators
# and  both condition are true
# or atleast one condition are true 
# not change the value true to false || false to true

print( 10 > 20 and 10 == 10)
print(10 < 20 or 10 < 1)
print(not (10 > 20))