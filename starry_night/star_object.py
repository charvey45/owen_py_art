import random
import turtle

class star():
    x=0
    y=0
        
    def __init__(self,screen_width,screen_height):
        foo=int(screen_width/2)
        bar=int(screen_height/2)
        self.x = random.randint(-1*foo,foo)
        self.y = random.randint(-1*bar,bar)
        self.size = random.randint(3,10)
        


    def draw_star(self, turtles, color="yellow"):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(144)
        for i in range(5):
            turtle.forward(self.size)
            turtle.right(144)
            turtle.forward(self.size)
        turtle.end_fill()
        turtle.setheading(0)