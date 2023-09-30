from turtle import Turtle, Screen

jordan = Turtle()
my_screen = Screen()


def move_forwards():
    jordan.forward(10)


def move_backwards():
    jordan.backward(10)


def move_left():
    jordan.left(10)


def move_right():
    jordan.right(10)


def clear():
    jordan.clear()
    jordan.penup()
    jordan.home()
    jordan.pendown()


my_screen.listen()
my_screen.onkeypress(key="w", fun=move_forwards)
my_screen.onkeypress(key="s", fun=move_backwards)
my_screen.onkeypress(key="a", fun=move_left)
my_screen.onkeypress(key="d", fun=move_right)
my_screen.onkey(key="c", fun=clear)

my_screen.exitonclick()
