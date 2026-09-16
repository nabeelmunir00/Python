def menu():
    print("1. Add Data")
    print("2. Read Data")
    print("3. Clear Data")
    print("4. Exit")


def addData(data):
    with open('note.txt','a') as f:
        f.write(data)

def readDate():
    with open('note.txt','r') as f:
        content = f.read()
        print(f'Content: {content}')

def clearData():
    with open ('note.txt','w') as f:
        f.write('')
        print('clear data successfully!')


menu()
selectMenu = (input("Please your options: "))
print(selectMenu,type(selectMenu))

