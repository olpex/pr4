import turtle

# Create and set up the turtle
t = turtle.Turtle()
t.speed(2)  # Set drawing speed (1-10)

# Optional customizations
t.pensize(5)  # Make the line thicker
t.color("blue")  # Change the color
t.fillcolor("red")  # Set fill color
t.begin_fill()  # Start filling

# Draw a circle
radius = 100  # Circle radius in pixels
t.circle(radius)

t.end_fill()  # End filling

# Keep the window open until clicked
turtle.done()
