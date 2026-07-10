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

range(10,101)
range(23,57)
range(0,46)

list(range(5))         # [0, 1, 2, 3, 4]
list(range(1,6))       # [1, 2, 3, 4, 5]
list(range(0,10,2))   # [0, 2, 4, 6, 8]

for var in range(1,11):
    print(f'5x{var} = {5 * var}')