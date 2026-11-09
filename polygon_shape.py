"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        if side_length <= 0:
            raise ValueError("Side length must be greater than 0.")
        if pen_size <= 0:
            raise ValueError("Pen size must be greater than 0.")

        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle

        self.t = turtle.Turtle()
        self.t.hideturtle()

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.setheading(self.angle)
        self.t.pencolor(self.color)
        self.t.pensize(self.pen_size)
        self.t.pendown()

        for _ in range(self.sides):
            self.t.forward(self.side_length)
            self.t.left(360 / self.sides)

        self.t.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        self.x = x
        self.y = y
        self.t.clear()
        self.draw()
