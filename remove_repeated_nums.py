list1=list(map(int,input().split()))
uniques=[]
for i in list1:
    if i not in uniques:
        uniques.append(i)
print(uniques)
