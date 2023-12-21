start=int(input("enter the minimum range: "))
end=int(input("enter the maximum range: "))
for i in range(start,end):
    temp=i
    mod=0
    sum=0
    while(temp!=0):
        mod=temp%10
        sum=sum+mod
        temp=temp//10

    if sum%2==0:
        print(i)