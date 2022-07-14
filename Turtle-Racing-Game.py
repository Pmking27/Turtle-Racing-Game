# Turtle race game product
from turtle import Turtle,Screen
from random import randint

screen = Screen()
screen.setup(width = 500,height = 400)
colors = ["red" , "orange" , "yellow" , "green", "blue" , "purple"]
y_position=[-125,-75,-25,25,75,125]

user_bit=screen.textinput(title="Make your Bet",prompt="Which turtle will the race?\n(red turtle, orange turtle, yellow turtle, green turtle, blue turtle, purple turtle)\nEnter a turtle colour").lower()

if user_bit in colors:
    finsh_line=Turtle()
    finsh_line.speed(0)
    finsh_line.penup()
    finsh_line.goto(x=200,y=200)
    finsh_line.right(90)
    finsh_line.pendown()
    finsh_line.pensize(5)
    finsh_line.forward(400)
    all_turtle=[]
    
    for turtle_index in range(0,6):
        new_turtle=Turtle(shape = "turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230,y=y_position[turtle_index])
        all_turtle.append(new_turtle)

    if user_bit:
        race_is_on=True

    while race_is_on:
        for turtle in all_turtle:
            if turtle.xcor()>201:
                race_is_on=False
                winner_turtle=turtle.pencolor()
                if winner_turtle==user_bit:
                    print(f"You win!.The {winner_turtle} turtle is winner of race.")
                else:
                    print(f"You lose!.The {winner_turtle} turtle is winner of race.") 

            turtle.forward(randint(0,10))

    screen.exitonclick()
else:
    print("Invalid Input")    