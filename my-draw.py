import turtle

def draw_turtle():

    window = turtle.Screen()
    window.bgcolor("blue")
    kevin = turtle.Turtle()
    kevin.color("red")
    kevin.shape("arrow")
    kevin.speed(6)
    for j in range(0,36):
        for i in range(2):
            kevin.forward(100)
            kevin.left(120)
            kevin.forward(100)
        kevin.left(10)

    window.exitonclick()

draw_turtle()
