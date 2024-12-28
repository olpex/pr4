import turtle

def draw_sphere():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("3D Sphere")
    screen.bgcolor("white")
    
    # Create and set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    
    # Starting position
    radius = 150
    decrease = 5  # Amount to decrease each circle by
    
    # Draw circles with decreasing size to create sphere effect
    for i in range(radius, 0, -decrease):
        t.penup()
        t.goto(0, -i)  # Start from bottom of each circle
        t.pendown()
        
        # Make circles more transparent towards the edges
        # and darker in the middle for 3D effect
        if i > radius * 0.8:
            t.pensize(1)
            t.pencolor("#CCCCCC")
        elif i > radius * 0.5:
            t.pensize(2)
            t.pencolor("#999999")
        elif i > radius * 0.3:
            t.pensize(2)
            t.pencolor("#666666")
        else:
            t.pensize(1)
            t.pencolor("#333333")
            
        t.circle(i)
    
    screen.mainloop()

def main():
    draw_sphere()

if __name__ == "__main__":
    main()