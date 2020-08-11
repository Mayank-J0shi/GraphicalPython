import turtle

bob=turtle.Turtle()

bob.color("blue","green")  #if we need certain color we got get their #hexadecimal nummbers
#if we want to fill the color inside the shape the we need to define the parameter of color (outline,inside)

bob.begin_fill()

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)

bob.end_fill()

bob.penup()
bob.forward(150)
bob.pendown()

bob.begin_fill()

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)

bob.end_fill()



turtle.done()