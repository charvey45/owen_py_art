###
# Python Turtle Program to create stars in the sky
###


import turtle
from star_object import star


def closeout():
    canvas.onclick(None)


scale_factor=80
star_count=1000
turtle.speed(0)
canvas = turtle.Screen()
canvas.title("Stars in the sky")
canvas.bgcolor("black")
canvas_width=16*scale_factor
canvas_height=9*scale_factor
canvas.setup(width=canvas_width,height=canvas_height)

## Make list of Starts
star_list=[]
for x in range(0,star_count):
    foo = star(canvas_width, canvas_height)
    star_list.append(foo)

for one_star in star_list:
    one_star.draw_star(canvas)

canvas.onkey(closeout,"x")
canvas.mainloop()





