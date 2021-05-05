print("Tjenare gruppen!!")

print("hej hopp")

print("hej hopp två")

print("Jag är supertaggad på detta arbetet!!!!")
import turtle 


print("Plugghästen for president")
t=turtle.Turtle()
t.speed(10)


t.left(90)
t.color("saddle brown")
t.pensize(5)
t.forward(200)
t.right(90)
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(0,250)
t.pendown()
t.color("white")

for i in range(55):
    t.forward(i/4)
    t.left(15)


turtle.done()