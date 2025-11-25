# def examMark(note):
#     if note>=90:
#         return "A"
#     elif 90>note>=80:
#         return "B"
#     elif 80>note>=70:
#         return "C"
#     elif 70>note>=60:
#         return "D"
#     else:
#         return "F"
    
# print(examMark(60))

# import math
# def findHypot(side1,side2):
#     formula = math.hypot(side1,side2) 
#     return formula
# print(findHypot(7,24))


# import random

# def guessNum(number):
#     secretnum = random.randint(1,10)

#     while number != secretnum:
#         if number < secretnum:
#             print("Too small, try again!")
#         elif number > secretnum:
#             print("Too big, try again!")

#         number = int(input("What is your guess? "))

#     print("Correct!")

# guessNum(4)


# import turtle
# import random
# star = turtle.Turtle()
# wn = turtle.Screen()
# star.pensize(3)
# wn.bgcolor("black")
# colors = ["purple","pink","blue","red","green"]

# count = 0
# while count<=20:
#     count +=1 
#     star.color(random.choice(colors))
#     x = random.randint(-300,300)
#     y = random.randint(-250,250)

#     star.penup()
#     star.goto(x,y)
#     star.pendown()
#     for i in range(5):
#         star.right(144)
#         star.forward(100)

# wn.exitonclick()







