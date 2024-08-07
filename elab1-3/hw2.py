from turtlelab7 import turtle,check 

def paint_polygon(n,size):
    degree = int(360 / n)
    rotation = int(360 / degree)
    for i in range(rotation):
        turtle.forward(size)
        turtle.left(degree)

# paint a triangle on the +x axis
turtle.forward(100);
paint_polygon(3,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

# paint a square on the +y axis
turtle.right(90);
turtle.forward(100);
paint_polygon(4,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

# paint a pentagon (5-side) on the -x axis
turtle.right(90);
turtle.forward(100);
paint_polygon(5,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

# paint a hexagon (6-side) on the -y axis
turtle.right(90);
turtle.forward(100);
paint_polygon(6,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

check()
        