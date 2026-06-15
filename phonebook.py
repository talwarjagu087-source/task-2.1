#PHONE BOOK APPLICATION

numberList = []
def showmenu():
    print("""
        1. ADD
        2. UPDATE
        3. DELETE
        4. EXIT OR QUIT
        5. VIEW
        """)
def askuser():
    choice = input("ENTER CHOICE : ")
    return choice
def add():
    username = input("ENTER USERNAME : ")
    usernumber = input("ENTER USER PHONE NUMBER : ")
    contact = {
        "NAME" : username,
        "NUMBER" : usernumber
        }
    numberList.append(contact)
    print("CONTACT SAVE :) ")

def update():
    i = 0
    for contct in numberList:
         print(i, "- ",contct)
         i+=1
    select = int(input("SELECT Contatct"))
    username = input("ENTER USERNAME : ")
    usernumber = input("ENTER USER PHONE NUMBER : ")
    contact = {
        "NAME" : username,
        "NUMBER" : usernumber
        }
    numberList[select] = contact
    
     




def delete():
    i = 0
    for contct in numberList:
         print(i, "- ",contct)
         i+=1
    select = int(input("SELECT Contatct"))
    numberList.pop(select)  

def view():
        print(numberList)

while True:
     showmenu()
     ch = askuser()
     match(ch):
          case '1':
               add()
          case '2':
               update()
          case '3':
               delete()
          case '4':
               exit or quit()
          case '5':
               view()
          case '6':  
               print("INVALID CHOICE") 
               