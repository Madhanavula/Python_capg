num=int(input("enter the number:"))
temp=num
mod=0
reverse=0
while(temp!=0):
    mod=temp%10
    reverse=reverse*10+mod
    temp=temp//10

print(reverse)