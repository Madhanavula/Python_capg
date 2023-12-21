import turtle as t
import time
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t.bgcolor('black')
for x in range(30):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
	
time.sleep(10)
