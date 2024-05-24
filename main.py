import turtle
import colorsys


def draw_flower(t, num_petals, radius, hue_start):
    for i in range(num_petals):
        # Calculate the current color using HSV to RGB conversion
        hue = hue_start + i / num_petals
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.color(r, g, b)

        # Draw one petal
        t.circle(radius, 60)
        t.left(120)
        t.circle(radius, 60)
        t.left(120)

        # Rotate to the next position
        t.left(360 / num_petals)


def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    turtle.colormode(1.0)  # Use color mode that allows floats in the range 0-1
    return t


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = setup_turtle()
    num_petals = 36
    radius = 100

    hue_start = 0.0
    draw_flower(t, num_petals, radius, hue_start)

    turtle.done()


if __name__ == "__main__":
    main()
