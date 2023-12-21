str1=input("enter the string1: ")
str2=input("enter the string2: ")
s1=list(str1)
s2=list(str2)
s1.sort()
s2.sort()
index=0
while(index<len(s1)):
    if s1[index]==s2[index]:
        index=index+1
    else:
        print("its not anagram pair")
        exit()

print("its anagram pair")






