import turtle

# Create and set up the turtle
t = turtle.Turtle()
t.speed(2)  # Set drawing speed (1-10)

# Optional customizations
t.pensize(3)  # Set line thickness
t.pencolor("red")  # Set line color to red
t.fillcolor("green")  # Set fill color to green
t.begin_fill()  # Start filling

# Draw a triangle
for _ in range(3):
    t.forward(100)  # Each side is 100 pixels
    t.left(120)    # Turn 120 degrees for equilateral triangle

t.end_fill()  # End filling

# Keep the window open until clicked
turtle.done()
