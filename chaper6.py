# Conditional Statements
# Making Decisions in Code
# Real programs don't run the same code every time — they make decisions. Conditional statements let your program choose what to do based on a condition. That's why they're also called control flow statements.

# if condition:
#     # runs when condition is True
# elif another_condition:
#     # runs if the above was False, this is True
# else:
#     # runs when nothing above was True

# age = int (input('Please enter your age:- '))

# if age >=18:
#     print('You Can Vote!')
# else:
#     print("You can not vote!")

# n1 = int(input("Enter First Number :- "))
# n2 = int(input("Enter Second Number :- "))

# if n1 > n2:
#     print(f'{n1} is greater')
# else:
#     print(f'{n2} is greater')

# gender = input('Enter Your Gender M / F := ')
# if gender == 'M' or 'm':
#     print('Good Moring Sir')
# elif gender == 'F' or 'f':
#     print('Good Moring Mam')
# else:
#     print('Please enter vauld info!')

# checkNum = int(input('Please enter int value to check number is Odd or Even :-- '))
# if checkNum % 2 == 0:
#     print(f'{checkNum} is Even')
# else:
#     print(f'{checkNum} is Odd')

# userName = input('Please enter your name:= ')
# userAge = int(input("Please enter your age:= "))

# if userAge >= 18:
#     print(f'Hey {userName}, you are a valid voter ✅')
# else:
#     print(f'Hey {userName}, you are not valid voter')

# year = int(input('Enter a year:- '))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')

temp = int(input('Please enter the temperature in °C := '))
if temp < 0:
    print('Freezing Cold 🥶')
elif temp > 0 and temp < 45:
    print("Pleasant 😊")
elif temp >= 45:
    print('Very Hot 🔥')
else:
    print('Enter Valid temperature in °C') 