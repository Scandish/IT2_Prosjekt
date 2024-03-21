import random
import turtle

# Set up the screen
win = turtle.Screen()
win.title("Snowfall Simulation")
win.bgcolor("black")
win.tracer(5, 0)  # Update the screen more frequently

# Create a list to store the snowflakes
snowflakes = []

# Function to create snowflakes
def create_snowflake():
    snowflake = turtle.Turtle()
    snowflake.shape("circle")
    snowflake.color("white")
    snowflake.penup()
    snowflake.speed(0)
    snowflake.shapesize(0.5)  # Set snowflake size
    snowflake.goto(random.randint(-win.window_width() // 2, win.window_width() // 2),
                    random.randint(win.window_height() // 2, win.window_height()))
    snowflakes.append(snowflake)

# Create initial snowflakes
num_snowflakes = 50
for _ in range(num_snowflakes):
    create_snowflake()

# Function to move snowflakes
def move_snowflakes():
    for snowflake in snowflakes:
        y = snowflake.ycor()
        y -= 10  # Move snowflake upwards faster
        snowflake.sety(y)

        # If snowflake goes off-screen, reposition it at the top
        if y < -win.window_height():
            y = win.window_height()
            snowflake.goto(random.randint(-win.window_width() // 2, win.window_width() // 2), y)

# Main loop
while True:
    win.update()
    move_snowflakes()