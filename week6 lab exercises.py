# import random
# for numbers in range(10):
#     print(random.random())


# import random
# for number in range(10):
#     print(random.randrange(25,35))


# import math
# theorem = math.hypot(5,12)
# print(theorem)


# import math
# def areaofcircle(r):
#     areaofcircle=math.pi*r*r
#     return areaofcircle
# print(areaofcircle(5))


# import turtle
# star = turtle.Turtle()
# wn = turtle.Screen()

# def five_pointed_star(l,a):
#     for i in range(5):
#         star.right(a)
#         star.forward(l)
        

# print(five_pointed_star(100,144))
# wn.exitonclick()


# import turtle
# square = turtle.Turtle()
# wn = turtle.Screen()
# square.pencolor("pink")
# wn.bgcolor("lightgreen")
# square.pensize(3)

# def drawsquare(side):
#     for i in range(4):
#         square.forward(side)
#         square.left(90)

# for i in range(5):
#     square.penup()
#     square.forward(40)
#     square.pendown()
#     drawsquare(20)
      


# wn.exitonclick()



# import turtle
# wn = turtle.Screen()
# s = turtle.Turtle()
# s.pensize(3)
# s.pencolor("pink")
# wn.bgcolor("lightgreen")
# def squares(t,side=20):
#     for i in range(4):
#         t.left(90)
#         t.forward(side)
       
        
         
# def growing_squares(t,length=20):
#     for i in range(5):

#         squares(t,side=length)

#         length +=20

#         t.penup()
#         t.right(45)
#         t.forward(15)
#         t.left(45)
#         t.pendown()
        


# growing_squares(s,20)
# wn.exitonclick()