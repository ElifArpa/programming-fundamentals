import turtle
# polygon = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("gray")
# polygon.pencolor("purple")
# polygon.pensize(3)
# def drawPoly(t,sidenum,sidesize):
#     angle = 360/sidenum
#     for i in range(sidenum):
#         t.forward(sidesize)
#         t.left(angle)

# drawPoly(polygon,9,100)        
# wn.exitonclick()
# 
# 
 
# square = turtle.Turtle()
# wn = turtle.Screen()
# square.pencolor("pink")
# wn.bgcolor("white")
# square.pensize(3)
# def squares(t,length,sidenum):
#     for i in range(sidenum):
#         t.forward(length)
#         t.left(90)

# def rotatingsquares(t,angle):
#     for i in range(20):
#         squares(square,100,4)
#         t.left(angle)

# rotatingsquares(square,18)
# wn.exitonclick()


# wn = turtle.Screen()
# wn.bgcolor("purple")
# rotating_spiral_square = turtle.Turtle()
# rotating_spiral_square.pencolor("blue")
# rotating_spiral_square.pensize(3)
# rotating_spiral_square.penup()
# rotating_spiral_square.goto(200,0)
# rotating_spiral_square.pendown()
# spiral_square = turtle.Turtle()
# spiral_square.pencolor("blue")
# spiral_square.pensize(1)
# spiral_square.penup()
# spiral_square.goto(-200,0)
# spiral_square.pendown()


# def drawSpiralSquares(t,sidesize,sidenum,angle):
#     for i in range(sidenum):
#         t.forward(sidesize * i)
#         t.left(angle)



# drawSpiralSquares(rotating_spiral_square,10,20,91)  
# drawSpiralSquares(spiral_square,10,20,90) 
# wn.exitonclick()     



# wn = turtle.Screen()
# wn.bgcolor("lightblue")
# triangle = turtle.Turtle()
# triangle.pencolor("pink")
# triangle.pensize(3)
# def drawPolygon(t,sidenum,sidesize,angle):
#     angle = 360/sidenum
#     for i in range(sidenum):
#         t.forward(sidesize)
#         t.left(angle)

# def drawEquitriangle(t,sidenum,sidesize):
#     drawPolygon(triangle,sidenum,sidesize,360/sidenum)

# drawEquitriangle(triangle,3,100)
# wn.exitonclick()



# star = turtle.Turtle()
# wn = turtle.Screen()
# star.pencolor("red")
# wn.bgcolor("white")
# star.pensize(3)
# def drawStars(t,sidesize,angle):
#     for i in range(5):
#         t.right(angle)
#         t.forward(sidesize)

# def walkingstars(t,walksize):
#     for i in range(5):
#         drawStars(star,100,144)
#         t.penup()
#         t.forward(walksize)
#         t.right(144)
#         t.pendown()

# walkingstars(star,350)
# wn.exitonclick()


# sprite = turtle.Turtle()
# wn = turtle.Screen()
# sprite.pencolor("red")
# wn.bgcolor("black")
# sprite.pensize(3)
# def drawSprite(t,legnum,leglen,angle):
#     t.dot()
#     for i in range(legnum):
#         t.forward(leglen)
#         t.penup()
#         t.backward(leglen)
#         t.pendown()
#         t.left(angle)

# drawSprite(sprite,15,120,24)
# wn.exitonclick()




