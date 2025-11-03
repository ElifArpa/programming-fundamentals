# import turtle
# wn = turtle.Screen()
# star = turtle.Turtle()
# star.pensize(3)
# star.speed(0)
# def drawStar(t,length,angle,color):
#         t.pencolor(color)
#         for i in range(5):
#             t.right(angle)
#             t.forward(length)

# def circle_of_star(t,distance,angle):
#     colors = ["blue","yellow","purple","pink","orange","green","red","black","lightgreen","lightblue"]
#     for i in range(10):
#         drawStar(star,100,144,colors[i % len(colors)])
#         t.penup()
#         t.forward(distance)
#         t.right(angle)
#         t.pendown()
       


# circle_of_star(star,120,36)
# wn.exitonclick()



# import turtle
# wn = turtle.Screen()
# flower = turtle.Turtle()
# flower.pencolor("pink")
# flower.pensize(3)
# flower.speed(0)
# wn.bgcolor("lightblue")

# def drawPolygonpPattern(t,sidenum,size,angle):
#     for i in  range(sidenum):
#         t.forward(size)
#         t.left(angle)

# def turningPolygons(t,angle):
#     for i in range(20):
#         drawPolygonpPattern(flower,6,100,60)
#         t.left(angle)

# turningPolygons(flower,18)
# wn.exitonclick()


#yapamadın aşağıdakini
# import turtle
# wn = turtle.Screen()
# square = turtle.Turtle()
# square.pencolor("brown")
# wn.bgcolor("lightgreen")
# square.pensize(3)
# def drawSquare(t,size,sidenum,angle):
#     for i in range(sidenum):
#         t.forward(size)
#         t.left(angle)

# def drawNestedSquares(t,startsize,step,count):
#     size = startsize
#     for i in range(count):
        

             
#         t.penup()
#         t.goto(-size/2, -size/2)  
#         t.pendown()
#         drawSquare(square,size=200,sidenum=4,angle=90)
#         size -= step

# drawNestedSquares(square,200,20,5)
# wn.exitonclick()


# import turtle
# wn = turtle.Screen()
# circle = turtle.Turtle()
# circle.pensize(3)
# circle.speed(0)
# wn.bgcolor("lightblue")
# def drawCircle(t,radius,color):
#     t.pencolor(color)
#     for i in range(360):
#         t.forward(radius)
#         t.left(1)

# def drawSpirograph(t,distance,angle):
#     colors = ["blue","yellow","purple","pink","orange","green","red","black","lightgreen","lightblue","turquose","cyan"]
#     for i in range(12):
#          drawCircle(circle,1,colors[i % len(colors)]) 
#          t.penup()
#          t.left(angle)
#          t.forward(distance)
#          t.pendown()


# drawSpirograph(circle,15,30)
# wn.exitonclick()



# import turtle
# wn = turtle.Screen()
# house = turtle.Turtle()
# house.pensize(3)
# house.pencolor("purple")
# wn.bgcolor("pink")
# def drawHouse(t,sidesize,angle1,angle2):
#     for i in range(4):
#         t.forward(sidesize)
#         t.right(angle1)

#     for i in range(1):     
#         t.left(angle2)
#         t.forward(sidesize)
#         t.right(120)
#         t.forward(sidesize)

# def fivehouse(t,gap):
#     for i in range(5):
#         drawHouse(house,100,90,60)
#         t.penup()
#         t.left(60)
#         t.forward(gap)
#         t.pendown()

# fivehouse(house,50)
# wn.exitonclick()