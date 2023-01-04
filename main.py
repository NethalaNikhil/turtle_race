import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race")
colors = ['red', 'orange', 'yellow', "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6, 1):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_position[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_turtle = i.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! the {winning_turtle} turtle is the winner!")
            else:
                print(f"You have lose! the {winning_turtle} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)

screen.exitonclick()
