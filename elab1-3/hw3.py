import turtle
from random import randint


turtle.colormode(255)
turtle.speed(0)
turtle.Screen().bgcolor(1, 50, 32) 


def paint_polygon(n,size):
    degree = int(360 / n)
    rotation = int(360 / degree)
    for i in range(rotation):
        turtle.forward(size)
        turtle.left(degree)

def flower_leaf(n,size):
    degree = int(360 / n)
    rotation = int(360 / degree)
    turtle.pencolor("red")
    for _ in range(rotation):

        turtle.circle(size)
        turtle.rt(degree)



def full_flower_leaf(n,size):
    degree = int(360 / n)
    rotation = int(360 / degree)
    random_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
    turtle.pencolor("green")
    turtle.pensize(size/2)
    turtle.backward(size*4)
    turtle.pensize(0)
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(size/2)
    turtle.end_fill()
    turtle.rt(270)
    turtle.up()
    turtle.forward(size/2)
    turtle.down()
    for _ in range(rotation):
        turtle.color(random_color)
        turtle.penup()
        turtle.fd(size/8 + size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        turtle.penup()
        turtle.backward(size/8 + size)
        turtle.rt(degree)
    
    


def green_garden(flower):
    for i in range(flower):
        random_size = randint(5, 10)
        random_leaf = randint(3, 6)
        turtle.penup()
        turtle.goto(randint(-500, 500), randint(-300, 270))
        turtle.rt(90)
        turtle.pendown()
        full_flower_leaf(random_leaf, random_size)

    

green_garden(200)


turtle.done()