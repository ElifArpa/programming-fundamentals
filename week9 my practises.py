# def converter(value,scale):
#     formula1 = (value - 32) * 5/9
#     formula2 = (value * 9/5) + 32

#     value = int(input("write temperature value:"))
#     scale = str(input("write scale:"))

#     if scale == "F":
#         return formula1
#     elif scale == "C":
#         return formula2 
    
# print(converter(100,"F or C"))


# import random
# import turtle
# star = turtle.Turtle()
# wn = turtle.Screen()
# star.pensize(3)
# wn.bgcolor("black")
# colors = ["cyan","purple","pink","red","blue"]

# starscount = 0
# while starscount<=20:
#     starscount +=1

#     x =random.randint(-300,300)
#     y =random.randint(-250,250)
#     star.penup()
#     star.goto(x,y)
#     star.pendown()
#     for i in range(5):
#         star.right(144)
#         star.color(random.choice(colors))
#         star.forward(100)

# wn.exitonclick()



# def factorial(n):

#     n = int(input("write a number:"))
#     while n>=0:
#         return n*(n-1)   
        

#     if n<0:
#         return "n cant be negative,try again"

# print(factorial(1))




        


