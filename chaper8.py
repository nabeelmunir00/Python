# For Loop

# The range() Function
# range() generates a sequence of numbers. Think of it as saying "count from here to there".

# range(stop)             # 0 up to stop-1
# range(start, stop)      # start up to stop-1
# range(start, stop, step)# start, jumping by step

# ranges
# 10 - 100
# 23 - 56
# 0 - 15

# range(10,101)
# range(23,57)
# range(0,46)

# list(range(5))         # [0, 1, 2, 3, 4]
# list(range(1,6))       # [1, 2, 3, 4, 5]
# list(range(0,10,2))   # [0, 2, 4, 6, 8]

# for var in range(1,11):
#     print(f'5x{var} = {5 * var}')


# for loop with string

# sti = 'Hello'
# print("ok")
# for i in sti:
#     print(i)

# for i in range(len(sti)):
#     print(str[i])


# solve for loop question 
# Q1
# Print "Hello World" n times.
# Input: 3
# Hello World × 3 lines

# for i in range(1,4):
#     print('Hello Word')

# Q2
# Print natural numbers from 1 to n.
# Input: 5
# 1 2 3 4 5

# num = int(input('Please enter a natural numbers to:-'))

# for i in range(1,num+1):
#     print(i)

# Reverse for loop — print n down to 1.
# Input: 5
# 5 4 3 2 1

# for i in range(num,0,-1):
#     print(i)
    
#     Q4
# Print the multiplication table of a number.
# Input: 5
# 5×1=5, 5×2=10 … 5×10=50

# for i in range(1,11,1):
#     print(f'{num}x{i}={num*i}')

# Q5
# Sum of first n natural numbers.
# Input: 5
# Sum = 15
# sum = 0
# for i in range(1,num+1):
#     print(i)
#     sum+=i
# print(f'Sum = {sum}')


# Q6
# Factorial of a number.
# Input: 5
# 5! = 120

# fac = 1
# for i in range(1,num+1):
#    fac = fac * i
# print(f'{num}! = {fac}')

# Q7
# Print sum of all even and odd numbers in a range separately.
# Input: 1 to 10
# Even sum = 30, Odd sum = 25

# start = int(input('Please enter a number to start:'));
# end = int(input('Please enter a number to end:'));

# sum_even = 0
# sum_odd = 0
# allEvenNum = []
# allOddNum = []

# for i in range(start,end+1):
#     if i % 2 == 0:
#         sum_even+=i
#         allEvenNum.append(i)
#     else:
#         sum_odd+=i
#         allOddNum.append(i)
# print("Even sum =", sum_even,allEvenNum)
# print("Odd sum =", sum_odd,allOddNum)
