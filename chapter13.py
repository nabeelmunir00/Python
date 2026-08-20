# Tuple — The Immutable List
# A tuple is exactly like a list, except you cannot change it once created. Use tuples for data that should stay constant — like days of the week, coordinates, or config values.

# days = ("Mon", "Tue", "Wed")

# print(days[0])   # Mon
# days[0] = "X"   # ❌ TypeError — tuples are immutable


# () > sign off tuple 
    # 0  1  2  3  
a = (10,20,30,40,10,10)

print(type(a))

# tuple ka only 2 methods ha 

# agher hum na tuple ma kis value ka index find karna ho 
print(a.index(20)) # is sa vo hum ko value ka index daye ka to hum na pass kiea ha 

# aghar hum na tuple ka check karna ho ka same value kinte par ha 
print(a.count(10));


# or hum agher () ka elave ak he variable ma multiple value add kare to vo be tuple hota ha 
def student():
    return "nabeel",21,"nabeel@gmail.com"

info = student()

print(f"Data: {info} Type: {type(info)}")

# Tuple unpacking
name,age,mail = info # is tara hum tuple sa data ko unpack kar sate ha 
print(f"Name:{name} Age:{age} Email:{mail}")