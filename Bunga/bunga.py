
import turtle


li = turtle.Turtle()
li.screen.bgcolor("black")
li.pensize(2)
li.color("green")
li.left(90)
li.backward(100)
li.speed(20000)
li.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
         li.forward(i)
         li.color("light blue")
         li.circle(2)
         li.color("blue")
         li.left(30)

         tree(3*i/4)

         li.right(60)

    tree(3*i/4)

    li.left(30)
    li.backward(i)
    
    

tree(100)

#For My Be Loved Rania Dhiya Fakhira
li.color('light blue')
li.penup()
li.goto(0, -175)
li.write('For My Beloved Rania Dhiya Fakhira', align='center', font='times 25 normal')
li.hideturtle()
turtle.done()
