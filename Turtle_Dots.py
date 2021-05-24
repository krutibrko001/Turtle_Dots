from turtle import Turtle, Screen
from random import choice

new_color_list = [(243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63)]



screen = Screen()
my_turtle = Turtle()
screen.setup(800, 800)
screen.colormode(255)

my_turtle.shape("circle")
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.speed(0)
my_turtle.pensize(10)

my_turtle.goto(-300, -300)

for i in range(156):
  my_turtle.dot()
  my_turtle.forward(50)
  my_turtle.color(choice(new_color_list))
  if my_turtle.xcor() >= 300:
    my_turtle.setx(-300)
    my_turtle.sety(my_turtle.ycor()+50)
