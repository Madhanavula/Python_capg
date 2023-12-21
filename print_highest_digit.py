list1=list(map(int,input("enter the valuse : ").split()))
max=list1[0]
for i in list1:
    if i > max:
        max=i

print(max)
