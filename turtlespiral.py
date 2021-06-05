import turtle
print("What Angle?:")
angle=float(input())
colors=['red','pink', 'purple', 'blue', 'cyan', 'green', 'yellow', 'orange']
t=turtle.Pen()
t.speed()
turtle.bgcolor('black')
for x in range(180):
#    t.pencolor(colors[x%7])
    t.pencolor(colors[x%len(colors)])
    t.width(x/100+1)
    t.forward(x)
    t.left(angle)
    
turtle.hideturtle()

done()
print ("hit enter to close...")
x=input()
