# [] is called List 

a = [10,20,30,40]

# print(type(a))

# List ko hum order sa control kar sate ha 
#print(a[-1]) # is ka hum list ka last element ko access kar sate ha 

# Hum list kie value ko changes kar sate ha os ka order sa 

# a[1] = 22

# print(a)

# List ma hum Duplicates data be store kar sate ha 

l = [1,1,1,2,2,2,3,3,3,4,4,4]

# Agher hum na list ko loop ka sate use karna ho 
# is ko karne ka 2 way ha using value or using index

# List loop using by Values
# for i in a:
#     print(i)


# or agher hum na list ma index ka base ma loop run karne ho to 
# index sa hum value or index dono ko access kar sate ha 

# for i in range(0,len(a)):
#     print(f"{i} : {a[i]} ")


#Key List Methods
lst = [3, 1, 4, 1, 5]

lst.append(9)       # [3,1,4,1,5,9]   — add to end
lst.insert(0, 0)    # [0,3,1,4,1,5,9] — insert at index
lst.remove(1)       # removes first 1
lst.pop()            # removes last element
lst.sort()           # sort ascending
lst.reverse()        # reverse in place
len(lst)             # numbe



list2 = [1,2,3]
list2.append(4) # is sa hum list ka last ma value add karte ha 
list2.insert(2,4) # is method ma index ka value add kar sate ha 
list2.pop() # pop method last value ko delete karta ha or vo he value return be karna ha or hum is ko index ka sate he use kar sate ha 
list2.remove(2) # remove method list ma se vo value remove karta ha jo hum is ko pass karte ha or return kons nahi karta 

list2.clear() # list ma sab element ko remove kar data ha or list ko empty kar data ha 

list3 = [50,10,40,30,20,90,60,100]
# print(f"Before: {list3}")
list3.sort()
# print(f"After: {list3}")

# 📝 List Questions

# Q1
# Print all positive and negative elements separately.
# Input: [3, -1, 4, -5, 9]
# Positive: [3,4,9] Negative: [-1,-5]

# q1List = [3,-1,4,-5,9,20,-20,50,-100]
# positive = []
# negative = []

# for i in q1List:
#     if(i > 0):
#         positive.append(i)
#     else:
#         negative.append(i)

# print(f"Positive: {positive} Negative: {negative}")

# Q2
# Find the mean (average) of all list elements.
# Input: [10, 20, 30, 40]
# Mean = 25.0

# q2list = [10,20,30,40]
# average = 0
# length = len(q2list)

# for i in q2list:
#     average+=i

# print(average/length)
# print(float(average%len(average)))


# Q3
# Find the greatest element and print its index.
# Input: [4, 8, 2, 9, 1]
# Greatest = 9 at index 3

q3list = [4,8,2,9,1,20,30,500]
bigger = q3list[0]
index = 0
for i in range(0,len(q3list)):
   if q3list[i] > bigger:
      bigger = q3list[i]
      index = i


# print(f"Largest value {bigger} at index {index}")


# Q4
# Find the second greatest element.
# Input: [4, 8, 2, 9, 1]
# Second greatest = 8

# q4list = [4, 7, 2, 21, 1,11,18]
# largest = q4list[0]
# sec_largest = q4list[0]

# for i in q4list:
#    if i > largest:
#       sec_largest = largest
#       largest = i

#    elif i > sec_largest:
#       sec_largest = i

# print(f"Second Largest {sec_largest}")

# Check if the list is already sorted.
# Input: [1, 3, 5, 7]
# List is sorted ✅
# Input: [3, 1, 4]
# Not sorted ❌

q5list = [1, 3, 5, 7,6]

for i in range(len(q5list)-1):
   if (q5list[i] > q5list[i+1]):
      print("Not sorted ❌")
      break
else:
   print("List is sorted ✅")