"""
Each character in a string is stored with its own Unicode number. That's why strings use more memory than integers.
"""

a = 'A' 

# how to check unicode 


#print(ord(a))

# string indexing
b = 'COLLEGE'

#print((b[0],b[1],b[2],b[3]))

# string slicing

# Slicing cuts out a piece of a string. Syntax: string[start : stop : step] — note that stop index is excluded.


#print(b[3:6:1])
# COLLEGE is ma sa hum ko  C L E E print karna ha 
# print(b[0:7:2])

# Test Question 

word = 'Hello how are you'

# how print karna ha 
print(word[6:10:1])
# you print karna ha 
print(word[10:14:1])
# Hello print karna ha
print(word[0:6:1])

# Type Conversion
# You can convert a value from one type to another using these built-in functions:

value = '12'
newValue = int(value)


print("Value ",value,"Type ", type(value))
print("Value ",newValue,"Type ", type(newValue))

# you can convert string if it holds vaild intergers 


