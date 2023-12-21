n=int(input("enter the number : "))
temp=n
mod=0
rev=0
while(temp!=0):
    mod=temp%10
    rev=rev*10+mod
    temp=temp//10

if rev==n:
    print("its palindrome number")
else:
    print("its not palindrome number")

'''n=(input("enter the number : "))
m=n[::-1]
if n==m:
    print("its palindrome")
else:
    print("its not palindrome")'''
