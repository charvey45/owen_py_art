import random
import turtle

class star():
    x=0
    y=0
        
    def __init__(self,screen_width,screen_height):
        self.x = random.randint(0,screen_width)
        self.y = random.randint(0,screen_height)
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