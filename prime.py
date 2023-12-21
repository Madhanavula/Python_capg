n=int(input("enter the num:"))
count=0
if n>1:
    for i in range(1,n):
        if n%i==0:
            count+=1
        else:
            continue
    if count==1:
        print("its prime number")
    else:
        print("its composite number")
else:
    print("plz enter the num greater than 1")