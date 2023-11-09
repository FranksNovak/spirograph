from turtle import Turtle, Screen
import random
import turtle

# Generování a základní nastavení objektu
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)

# Změna barevného modu
turtle.colormode(255)

# funkce na vytvoření random barvy
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# radius kružnice
radius = 80
# funkce na vytvoření spirographu
def spirograph(gap):
    for _ in range (int(360 / gap)):
        # nakreslí kružnici
        tommy.pencolor(random_color())
        tommy.circle(radius) 
        # otoč se o 360 stupnu děleno počet kruhů aby to rovnoměrně rozvrhlo kružnice kolem dokola
        tommy.left(gap)
spirograph(10)

my_screen = Screen()
my_screen.exitonclick()
