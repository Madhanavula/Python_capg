num=int(input("enter the num:"))
temp=num
mod=0
n1=len(str(num))
arm=0
while(temp!=0):
    mod=temp%10
    arm=arm+(mod**n1)
    temp=temp//10

if arm==num:
    print("its armstrong")
else:
    print("its not armstromg")