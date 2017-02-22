import turtle
for i in range(2):
    turtle.setup(800, 600)
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Project")

    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")

    tess.penup()                    # this is new
    size = 20
    for i in range(30):
        tess.stamp()                # leave an impression on the canvas
        size = size + 3             # increase the size on every iteration
        tess.forward(size)          # move tess along
        tess.right(24)              # and turn her

    wn.exitonclick()