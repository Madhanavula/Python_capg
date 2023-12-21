list1=[1,2,3,4,5,6,7]
count=0
f=int(input("enter the num to search in list:"))
for i in range(len(list1)):
    if f==list1[i]:
        count=count+1
        print(f"the num is finded successfully in index {i} ")
if count==0:
    print("not able to search")
    
