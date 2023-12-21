def palindrome_range(a,b):
    for i in range(a,b):
        rev=0
        temp=i
        while(temp!=0):
            mod=temp%10
            rev=rev*10+mod
            temp=temp//10
        if rev==i:
            print(i)
        
start=int(input("enter the start num:"))
end=int(input("enter the end num:"))
palindrome_range(start,end)