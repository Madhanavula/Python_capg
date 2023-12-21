print("--------------SAMPLE CALCULATOR------------")
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def mod(x,y):
    return x%y

def div(x,y):
    return x/y

a=int(input("enter the num1: "))
sign=input("enter the sign to be performed +,-,*,%,/ : ")
b=int(input("enter the num2: "))
if sign == '+':
    sum=add(a,b)
    print("output is ",sum)

elif sign == '-':
    difference=sub(a,b)
    print("output is ",difference)

elif sign == '*':
    product=mul(a,b)
    print("output is ",product)

elif sign == '%':
    modulus=mod(a,b)
    print("output is ",modulus)

elif sign == '/':
    division=div(a,b)
    print("output is ",division)
