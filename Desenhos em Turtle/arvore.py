import turtle
import random

a = int(input("Você quer plantar uma árvore? (utilize 1 e 2) "))
if a >= 1:
    print ("Booa :) ")
else:
    print ("Estou triste ")
    

def color_size(isatti, l):
    color = '#444C38'  
    if l <= 8:  
        color = '#00FF00' if random.uniform(0, 10) > 3.5 else '#FF69B4'
    elif l <= 30: 
        color = '#006600'
    isatti.pencolor(color)
    isatti.pensize(l / 10)


def angle():
    return random.uniform(10, 40)


def new_length(l):
    return l + random.gauss(-5, 1)


def tree(isatti, l, tree_on_middle=False):
    if l <= 0:
        return

    angle_r = angle()
    angle_l = angle()
    angle_m = (angle_l + angle_r) / 2

    color_size(isatti, l)
    isatti.forward(l)  

    isatti.left(angle_l)
    tree(isatti, new_length(l), tree_on_middle) 

    isatti.right(angle_m)
    if tree_on_middle:
        tree(isatti, new_length(l), tree_on_middle) 

    isatti.right(angle_m)
    tree(isatti, new_length(l), tree_on_middle) 

    isatti.left(angle_r)  

    color_size(isatti, l)
    isatti.backward(l)  


my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(300)
my_turtle.left(90)
my_turtle.penup()
my_turtle.backward(200)
my_turtle.pendown()
my_turtle.speed(10)

tree(my_turtle, 40, False)


turtle.Screen().exitonclick()
