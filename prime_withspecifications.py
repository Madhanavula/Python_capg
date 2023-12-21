start=int(input("enter the start num:"))
end=int(input("enter the end num:"))
digit=int(input("enter the digit specification: "))
def checkprime(n):
    count=0
    if n>1:
        for i in range(1,n):
            if n%i==0:
                count+=1
            else:
                continue
        if count==1:
            return 1
        else:
            return 0
def checkdigit(a,digit):
    temp=a
    while(temp!=0):
        mod=temp%10
        if mod==digit:
            return 1
        temp=temp//10
    return 0

def testascend(n):
    temp=n
    max=9
    while(temp!=0):
        mod=temp%10
        if mod>=max:
            return 0
        max=mod
        temp=temp//10
    return 1

def testdecend(n):
    temp=n
    max=9
    while(temp!=0):
        mod=temp%10
        if mod<=max:
            return 0
        max=mod
        temp=temp//10
    return 1

for i in range(start,end):
    if checkprime(i):
        if checkdigit(i,digit):
            if testascend(i) or testdecend(i):

                print(i)

