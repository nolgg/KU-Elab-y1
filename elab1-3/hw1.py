from turtlelab4 import turtle,check 

def paint_square(size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)


def paint_triangle(size):
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)


paint_square(100)
check()
paint_triangle(200)
check()
turtle.left(30)
paint_square(120)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
paint_triangle(120)
check()







