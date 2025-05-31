import matplotlib.pyplot as plt
import math

def koch_curve(p1, p2, depth):
    if depth == 0:
        return [p1, p2]
    else:
        x1, y1 = p1
        x5, y5 = p2

        dx = (x5 - x1) / 3
        dy = (y5 - y1) / 3

        x2, y2 = x1 + dx, y1 + dy
        x3 = (x1 + x5) / 2 + math.sqrt(3) * (y1 - y5) / 6
        y3 = (y1 + y5) / 2 + math.sqrt(3) * (x5 - x1) / 6
        x4, y4 = x1 + 2*dx, y1 + 2*dy

        return (koch_curve((x1, y1), (x2, y2), depth - 1) +
                koch_curve((x2, y2), (x3, y3), depth - 1)[1:] +
                koch_curve((x3, y3), (x4, y4), depth - 1)[1:] +
                koch_curve((x4, y4), (x5, y5), depth - 1)[1:])

def koch_snowflake(depth):
    size = 1
    height = math.sqrt(3)/2 * size
    p1 = (0, 0)
    p2 = (1, 0)
    p3 = (0.5, height)

    side1 = koch_curve(p1, p2, depth)
    side2 = koch_curve(p2, p3, depth)
    side3 = koch_curve(p3, p1, depth)

    # Combine and remove overlapping duplicates
    snowflake = side1 + side2[1:] + side3[1:]
    return snowflake

# Plot and count
depth = 3
points = koch_snowflake(depth)
segments = len(points) - 1

plt.figure(figsize=(6, 6))
xs, ys = zip(*points)
plt.plot(xs, ys, color='cyan')
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title(f"Koch Snowflake (Level {depth}) - {segments} Segments", color='white')
plt.gca().set_facecolor("black")
plt.show()

# Print segment count
expected = 3 * (4 ** depth)
print(f"Segments drawn: {segments}")
print(f"Expected segments: {expected}")
