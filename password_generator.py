import random
print("RANDOM PASSWORD GENERATOR ")
print("--------------------------")
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?"
num=int(input("enter the no.of password you need:"))
length=int(input("enter the length u need:"))
print("your {0} passwords are generated successfully with {1} characters".format(num,length))
for i in range(num):
    password=''
    for j in range(length):
        password+=random.choice(characters)
    print(password)
