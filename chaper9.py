# While Loop
# The while loop keeps running as long as a condition is True. You use it when you don't know how many times you'll need to repeat.

#  while loop syntax
# while condition:
#     code to be executed
#     code to be executed


# a = 1
# while True:
#     print(a)
#     a+=1


# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# # Output: 1  2  3  4  5

# eparate each digit of a number and print on a new line.
# Input: 1234
# 4 → 3 → 2 → 1

num = int(input('please enter a number:'))

# while num > 0:
#     print(num%10)
#     num = num // 10

# Q2
# Accept a number and print its reverse.
# Input: 12345
# 54321
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print(rev)
