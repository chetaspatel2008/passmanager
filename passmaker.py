def task():
    print("1. append password")
    print("2. view password")
    print("3. edit password")
    

inffo = []
def info():
    website = input("Enter website : ")
    username = input("Enter username : ")
    password = input("Enter password : ")
    account = {
        
        "website" : website,
        "username" : username,
        "password" : password,
        }
    inffo.append(account)

def main():
    if work == 1:
        info()

    elif work == 2:
        print(inffo)

    elif work == 3:
        edit = int(input("which one do you want to edit from the index(0, 1, 2,...) : "))
        edit_what = int(input("1-username, 2-password, 3-both : "))
        if edit_what == 1:
            inffo[edit]["username"] = input("Enter new username : ")
        elif edit_what == 2:
            inffo[edit]["password"] = input("Enter new password : ")
        elif edit_what == 3:
            inffo[edit]["username"] = input("Enter new username : ")
            inffo[edit]["password"] = input("Enter new password : ")
        


print("************************************")
print("Hello user, wellcome to passmanager")
print("************************************")

TorF = True
TorF2 = True
while TorF:
    task()
    work = int(input("Enter your task (1, 2, 3): "))
    main()

    again = input("Do you want to add again (yes/no) : ")

    TorF = False
while TorF2:

    if again == "yes":
        TorF = True
        TorF2 = False
    elif again == "no":
        TorF = False
       
        print("************************************")
        print("             THE END                ")
        print("************************************")

        
