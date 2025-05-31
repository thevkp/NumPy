import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("cyan")
t.speed(0)
t.pensize(2)

# Move turtle to starting position
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw the 3 sides of the snowflake
for _ in range(3):
    koch_snowflake(t, 300, 4)  # Change level here (e.g. 3, 4, 5)
    t.right(120)

t.hideturtle()
screen.mainloop()