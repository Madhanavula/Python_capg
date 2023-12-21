n=5
def horizantal_line():
    print("--------------------------------------------------")
def hallow():
    print("-----hallow------")
    for i in range(n):
        for j in range(n):
            if i==n-1 or j==n-1 or i==0 or j==0:
                print("*",end="")
            else:
                print(" ",end="")
        print()
def half_diamond():
    print("----half_diamond---------")
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print() 
    
def square():
    print("-----square------")
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
def right_triangle():
    print("------right_triangle-------")
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
def left_triangle():
    print("------left_triangle-------")
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print()

def pyramid():
    for i in range(1,n):
        for j in range(n-1-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()

def inverted_pyramid():
    print("-------inverted_pyramid-------------")
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,i):
            print("* ",end="")
        print()
def diamond():
    print("-------diamond-----------")
    for i in range(1, n+1):
        for j in range(1,n-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print()
    for i in range(n-1,0, -1):
        for j in range(1,n-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print()



if __name__=='__main__':
    half_diamond()
    horizantal_line()
    hallow()
    horizantal_line()
    square()
    horizantal_line()
    right_triangle()
    horizantal_line()
    left_triangle()
    horizantal_line()
    pyramid()
    horizantal_line()
    inverted_pyramid()
    horizantal_line()
    diamond()

