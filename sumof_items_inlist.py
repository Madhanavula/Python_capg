x=input("enter the nums: ").split(",")
list1=list(map(int,x))
sum=0
for i in list1:
    sum=sum+i

print(sum)
