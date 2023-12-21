def welcome(name):
    print("hi welcome,",name)

def hi(name):
    print("hi ",name)

def fact():
    n=int(input("enter the number : "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i

    print(fact)