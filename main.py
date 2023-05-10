from turtle import Turtle, Screen
import random


def is_race_over(turtle_x, finish_line_x):
    return turtle_x >= finish_line_x


is_race_on = False
colors = ["blue", "red", "green", "orange", "yellow", "purple"]
turtle_y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen = Screen()
screen_width = 500
screen_height = 400
screen.setup(width=screen_width, height=screen_height)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0, 10)
    random_turtle = random.randint(0, 5)
    all_turtles[random_turtle].forward(random_distance)
    if is_race_over(all_turtles[random_turtle].xcor(), screen_width/2 - 30):
        print(f"Turtle {colors[random_turtle]} won the race!")
        is_race_on = False


screen.exitonclick()
