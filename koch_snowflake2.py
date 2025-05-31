import turtle

# Counter to track number of segments
segment_count = 0

def koch_curve(t, length, level):
    global segment_count
    if level == 0:
        t.forward(length)
        segment_count += 1  # Count this segment
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

# Setup turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("cyan")
t.pensize(2)
t.speed(0)  # Fastest

# Move to center
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw full snowflake (closed triangle)
side_length = 300
level = 2

for _ in range(3):
    koch_curve(t, side_length, level)
    t.right(120)

# Print segment count
expected_segments = 3 * (4 ** level)
print(f"Segments drawn: {segment_count}")
print(f"Expected segments: {expected_segments}")

t.hideturtle()
screen.mainloop()
