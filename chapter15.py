# A dictionary stores data as key: value pairs — like a real dictionary where you look up a word (key) to find its meaning (value).

dic = {} # is the sign to create ka dictionary is ma hum key value pair ka sate data ko store kar sate ha 


dic1 = {"name":"Nabeel","age":19} # or hum na key ko "" | '' ma write karna ha 

# print(dic1)
# or gis tara hum list or tuple ko index ka sate os ka data access karta ha ise tara dicitonary ma hum key ka use kar os ka data ko access kar sate ha 

# print(f"Name: {dic1['name']}")

dic1["Course"] = "BSSE" # is tara hum dictionary ma ak new value add kar sate ha key value ka sate
dic1.update({"name":"Adil"}) # is tara hum kis be key value ko update kar sate agher key nahi ha to new value add ho gaye
dic1.pop("name")
# print(dic1.values()) # dictionary kie sab values return karna ha without key 
# print(dic1.get("age"))  # os key kie value return kar ta ha jo hum os ko pass karte ha 
# print(dic1.items()) # all data return karta ha key and value dono
# print(dic1.clear()) # dicitonary ko empty kar data ha 


#traversing (loops)

# d = {10:100,20:200,30:300,40:400}

# for i in d:
#     # print(f"key:{i} -> Value:{d[i]} ")

# 📝 Dictionary Questions
# Q1
# Merge two dictionaries into one.
# d1={a:1}, d2={b:2}
# {a:1, b:2}

d1 = {"a":10,"b":20}
d2 = {"c":30,"d":40}

for i in d2:
    print(f"Key:{i} --> value:{d2[i]}")
    d1[i] = d2[i]

print(d1)
# Q1
# Merge two dictionaries into one.

# d1={a:1}, d2={b:2}
# {a:1, b:2}
dics1 = {1:10,2:20,3:30}
dics2 = {4:40,5:50}

dics1.update(dics2)

print(f"New Data: {dics1}")


