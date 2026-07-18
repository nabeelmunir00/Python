# What are Functions?
# A function is a reusable block of code with a name. Instead of writing the same logic 10 times, you write it once as a function and call it 10 times.

# def greet():
#     print("Hello, welcome to Python!")

# greet()   # ← this is calling the function


# def hello():
#     print('Hello How Are You !')
# hello()


# Parameters & Arguments
# 📋 Parameter
# The variable name in the function definition. Like a placeholder.

# def greet(name):  # ← parameter
#     ...
# 📦 Argument
# The actual value you pass when calling the function.

# greet("Alice")  # ← argument

# def addition(a,b):  
#     print(a+b)

# addition(5,6)


def checkNumPal(num):
    copy = num
    rev = 0 

    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    if copy == rev:
        print('Number is palindrome')
    else:
        print('Number is not a palindrome')


checkNumPal(1234)
checkNumPal(121)

#Types of Arguments
# 1. Positional — order matters
def add(a, b):
    return a + b
add(5, 3)       # → 8

# 2. Default — works even without passing a value
def greet(name="Guest"):
    print(f"Hello {name}")
greet()            # Hello Guest
greet("Akarsh")  # Hello Akarsh

# 3. Keyword — pass in any order
def info(name, age):
    print(f"{name} is {age}")
info(age=25, name="Akarsh")  # order doesn't matter
