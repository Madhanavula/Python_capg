list1=[1,2,3,4,5]
try:
    #print(list1[4])
    print(list1[6])
except:
    print("index error")
else:
    print("try is executed")
finally:
    print("out of index")