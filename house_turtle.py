import turtle as t
import time
t.bgcolor("white")
t.pensize(2)
t.pencolor("white")
t.backward(300)
t.speed(0.5)
def rectangle1():
    t.pencolor("blue")
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)

def rectangle2():
    t.left(45)
    t.forward(250)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(100)

def triangle():
    t.right(45)
    t.forward(141)
    t.right(90)
    t.forward(141)

def parallelogram():
    t.left(45)
    t.forward(141)
    t.right(135)
    t.forward(250)
    t.right(45)
    t.forward(141)
def up1():
    t.right(135)
    t.forward(250)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(80)
    pass

def door():
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(50)

def window():
    t.left(135)
    t.forward(100)
    t.down()
    for i in range(4):
        t.left(90)
        t.forward(20)

    t.up()
    t.left(135)
    t.forward(100)
    t.down()
    
    t.right(45)
    t.forward(20)
    for i in range(3):
        t.left(90)
        t.forward(20)
    t.up()
    t.right(135)
    t.forward(70)
    t.down()
def line():
    t.right(90)
    t.forward(800)
    t.backward(1000)
if __name__=='__main__':
    rectangle1()
    triangle()
    rectangle2()
    parallelogram()
    t.up()
    up1()
    t.down()
    door()
    t.up()
    window()
    line()



    time.sleep(5)