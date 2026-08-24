# A dictionary stores data as key: value pairs — like a real dictionary where you look up a word (key) to find its meaning (value).

dic = {} # is the sign to create ka dictionary is ma hum key value pair ka sate data ko store kar sate ha 


dic1 = {"name":"Nabeel","age":19} # or hum na key ko "" | '' ma write karna ha 

print(dic1)
# or gis tara hum list or tuple ko index ka sate os ka data access karta ha ise tara dicitonary ma hum key ka use kar os ka data ko access kar sate ha 

# print(f"Name: {dic1['name']}")

dic1["Course"] = "BSSE" # is tara hum dictionary ma ak new value add kar sate ha key value ka sate
dic1.update({"name":"Adil"}) # is tara hum kis be key value ko update kar sate agher key nahi ha to new value add ho gaye
dic1.pop("name")
print(dic1.values()) # dictionary kie sab values return karna ha without key 
print(dic1.get("age"))  # os key kie value return kar ta ha jo hum os ko pass karte ha 
print(dic1.items()) # all data return karta ha key and value dono
print(dic1.clear()) # dicitonary ko empty kar data ha 

