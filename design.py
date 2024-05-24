import turtle
import colorsys


def draw_petal(t, radius, angle):
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)


def draw_flower(t, num_petals, radius, hue_start):
    for i in range(num_petals):
        # Calculate the current color using HSV to RGB conversion
        hue = hue_start + i / num_petals
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.color(r, g, b)

        # Draw one petal
        draw_petal(t, radius, 60)

        # Rotate to the next position
        t.left(360 / num_petals)


def draw_layered_flower(t, num_layers, petals_per_layer, radius_increment):
    hue_start = 0.0
    for layer in range(num_layers):
        draw_flower(t, petals_per_layer, radius_increment * (layer + 1), hue_start)
        hue_start += 0.1  # Change hue for the next layer


def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    turtle.colormode(1.0)  # Use color mode that allows floats in the range 0-1
    return t


def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = setup_turtle()
    num_layers = 6
    petals_per_layer = 18
    radius_increment = 30

    draw_layered_flower(t, num_layers, petals_per_layer, radius_increment)

    turtle.done()


if __name__ == "__main__":
    main()
