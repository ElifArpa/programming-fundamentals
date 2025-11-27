#first lab exercises
# width = int(input("enter the width:"))
# height = int(input("enter the height:"))
# area = height*width
# print("the area of rectangle is:",area)

# miles = int(input("enter the miles you driven:"))
# gallon = int(input("enter the gallon that you used:"))
# mpg = miles/gallon
# print("your mpg value is:",mpg)

# F = float(input("please write a degree fahrenheit value:"))
# convert = (F-35) * (5/9) 
# print("degree celcius value is:",convert,"Celcius")

# start_Day = int(input("write your first day of vacation(1-6):"))
# length = int(input("write your length of the vacation:"))
# convert = (start_Day + length)%7
# print("your end day is:",convert) 

# import math
# radius = int(input("write the radius of the circle:"))
# circumference = 2 * math.pi * radius
# print("circumference of the circle is:",circumference)

# birth_Year = int(input("please write your birth year:"))
# current_year = 2025
# age = current_year - birth_Year
# print("your age is:",age)

# import  turtle
# square = turtle.Turtle()
# wn = turtle.Screen()
# square.forward(100)
# square.left(90)
# square.forward(100)
# square.left(90)
# square.forward(100)
# square.left(90)
# square.forward(100)
# wn.exitonclick()

#second lab exercises
for i in range(100):
     print("We like Python's turtles")



# for months in ["january","february","march","april","may","june","july","august","september","october","november","december"] :
#     print("one of the months of the year is",months)

# for numbers in [(12 , 144) , (10  ,  100) , (32 ,  1024) , (3 ,   9) , (66  ,  4356) , (17  ,  289) , (42  ,  1764) , (99  ,  9801) , (820  ,  400)]:

#     print(numbers)

# import turtle
# polygon = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(8):
#     polygon.forward(100)
#     polygon.left(360/8)

# wn.exitonclick()


# side = int(input("enter the number of sides:"))
# length = int(input("enter the length of the side:"))
# colorname = str(input("enter the pencolor:"))
# fillcolorname = str(input("enter the fillcolor"))

# import turtle
# polygon = turtle.Turtle()
# wn = turtle.Screen()
# polygon.pencolor(colorname)
# polygon.fillcolor(fillcolorname)
# polygon.begin_fill()
# for i in range(side):
#     polygon.forward(length)
#     polygon.left(360/side)
# polygon.end_fill()

# wn.exitonclick()


# import turtle
# pirate = turtle.Turtle()
# wn = turtle.Screen()

# for i in [160,-43,270,-97,-43,200,-940,17,-86]:
#     pirate.left(i)
#     pirate.forward(100)
# print(pirate.heading())
# wn.exitonclick()


# import turtle
# star = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(5):
#     star.right(144)
#     star.forward(100)
# wn.exitonclick()


# import turtle
# clock = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# clock.pencolor("navyblue")
# clock.shape("turtle")
# for i in range(12):
#     clock.stamp()
#     clock.penup()
#     clock.forward(100)
#     clock.pendown()
#     clock.stamp()
#     clock.penup()
#     clock.backward(100)
#     clock.left(360/12)

# wn.exitonclick()


# import turtle
# spider = turtle.Turtle()
# wn = turtle.Screen()
# for i in range(9):
#     spider.stamp()
#     spider.forward(100)
#     spider.backward(100)
#     spider.left(360/9)

# wn.exitonclick()


