def prime(a,b):
    if a>1:
        for i in range(a,b):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)

start=int(input("enter the start num:"))
end=int(input("enter the end num:"))
prime(start,end)