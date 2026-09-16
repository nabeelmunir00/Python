# Errors vs Exceptions
# ❌ Errors (unfixable)
# SyntaxError — wrong syntax
# IndentationError — bad spacing
# TabError — mixing tabs/spaces
# ✅ Exceptions (handleable!)
# ZeroDivisionError
# TypeError
# ValueError
# FileNotFoundError

# Error handling 
# syntax error -> syntax os time ata ha jab hum syntax ma mistake karte ha 

# print('Hello bro) example hum na ' ka use nahi kiea gis ma syntax error a raha ha 


# or hum error handling ka lea in keyword ka use karte ha 

# Keyword	Purpose
# try	Wrap the risky code
# except	Handle the exception
# else	Runs only if no exception occurred
# finally	Always runs — good for cleanup
# raise	Manually throw your own exception

# example ak case ha gis ma hum agher hum kis be number ko 0 sa divide kare to ZeroDivisionError wala error ata ha 
n1 = int(input("Please enter 1 number:- ")) # user na n1 ma 10 pass kiea
n2 = int(input("Please enter 2 number:- ")) # or n2 ma 0 to ZeroDivisionError wala error aye ga hum is ko is tara handle kar sate ha 
try:
    print(f"Result:> {n1/n2}")
except Exception as err:
    print("ERR Found!")
    print("n2 ma 0 enter na karo! please!!!!!",err)
else:
    print("ERR Not Found!!")




