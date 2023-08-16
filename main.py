from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet", prompt="Who will win the race , enter color")
colors = ["red","orange","blue","yellow","green","purple"]
y_positions = [-70, -40, -10, 20, 50, 80 ]


for turtle_index in range (0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()
