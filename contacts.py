def menu():
    print("1. add contact")
    print("2. view contact")
    print("3. quit")

def add_contact():
    name=input("enter the name: ")
    number=input("enter the contact number: ")
    with open("contacts.txt","a") as f:
        f.write("name =" + name + " | " + "contact_number =" + number + "\n")

    print(name,"added successfully to the contact.txt file")

def view_contact():
    print("below are the contacts that u added in contacts.txt file")
    with open("contacts.txt","r") as f:
        for i in f.readlines():
            print(i)

while True:
    menu()
    ch=int(input("please enter your choice: "))
    if ch==1:
        add_contact()
    elif ch==2:
        view_contact()
    elif ch==3:
        print("bye bye.............")
        quit()
    else:
        print("please enter the mentioned option")

