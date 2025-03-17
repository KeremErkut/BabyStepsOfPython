import turtle 

wn = turtle.Screen()
wn.bgcolor("green")
wn.title("uolp")

alex = turtle.Turtle()

def penup(size):
    alex.penup()
    alex.forward(size)
    alex.pendown()

def shape(sides, size):
    angle = 360 / sides 
    for _ in range(sides):
        alex.forward(size)
        alex.right(angle)


shape(3, 50)

penup(70)

shape(4, 50)

penup(80)

shape(6, 50)

wn.mainloop()