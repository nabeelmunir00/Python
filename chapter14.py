# Set — Unique Values Only
# A set automatically removes duplicates and has no guaranteed order. Great for checking membership and performing math-style set operations.

# s = {1, 2, 2, 3, 3, 3}
# print(s)   # {1, 2, 3} — duplicates removed!


# set ko hum {} ma define karte ha or set duplicate value auto remove ho gate ha 


s = {1,2,2,2,3,4,5}

print(f"Data:{s} Type:{type(s)}")


# Set Operations
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# a | b   # Union         → {1,2,3,4,5,6}
# a & b   # Intersection  → {3,4}
# a - b   # Difference    → {1,2}
# a ^ b   # Symmetric diff→ {1,2,5,6}

set1 = {1,3,4,6}
set2 = {2,5,7,3,1}

print(f"Union of Sets: {set1 | set2}") # agher hum na dono sets ka union find karna ho to hum is tara kar sate ha 

print(f"Intersection of Sets:{set1 & set2}") # instersection ma vo value ate ha jo dono ma common ho 

print(set1 - set2)
print(set1 | set2)
