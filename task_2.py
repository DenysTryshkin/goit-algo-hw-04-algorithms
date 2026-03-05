import turtle

def koch_curve(t, order, size):
    """
    Recursive function to draw a Koch curve.
    
    t     : turtle object
    order : recursion level
    size  : length of the segment
    """
    if order == 0:
        t.forward(size)  # If we reach the lowest level, draw a straight line
    else:
        # Recursively draw 4 parts of the Koch curve
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    """
    Draws a Koch snowflake made of three Koch curves.
    
    order : recursion level
    size  : length of one side of the main triangle
    """
    # Create a window for drawing
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake")

    # Create a turtle
    t = turtle.Turtle()
    t.speed(0)  # Maximum speed
    t.penup()
    t.goto(-size / 2, size / 3)  # Position to the left
    t.pendown()

    # Draw three sides of the snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()  # Keep the window open

# --- Main part ---
if __name__ == "__main__":
    try:
        # Ask the user to enter the recursion level
        level = int(input("Enter recursion level (e.g., 0–5): "))
        draw_koch_snowflake(level)
    except ValueError:
        print("Error: please enter an integer.")