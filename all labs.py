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
#for i in range(100):
#     print("We like Python's turtles")



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


#third lab exercises
# import random
# for numbers in range(10):
#     print(random.random())

# import random
# for numbers in range(10):
#     print(random.randrange(25,35))

# import math 
# formula = math.hypot(5,12)
# print(formula)

# import math
# def areaOfCircle(r):
#     area = math.pi*(r**2)
#     return area
# print(areaOfCircle(9))


# import turtle
# star = turtle.Turtle()
# wn = turtle.Screen()
# def drawStar(t):
#     for i in range(5):
#         t.right(144)
#         t.forward(100)
# print(drawStar(star))
# wn.exitonclick()        

# import turtle
# square = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# square.pencolor("pink")
# square.pensize(3)
# def drawsquare(t,side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
    
# for i in range(5):
#     drawsquare(square,20)
#     square.penup()
#     square.forward(40)
#     square.pendown()
    
# wn.exitonclick()

# import turtle
# square = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# square.pencolor("pink")
# square.pensize(3)
# def drawSquare(t,side):
#     for i in range(4):
#         t.left(90)
#         t.forward(side)

# def growingsquares(t,length):
#     for i in range(5):
#         drawSquare(t,side=length)
#         length += 20
#         t.penup()
#         t.right(45)
#         t.forward(15)
#         t.left(45)
#         t.pendown()
        
# growingsquares(square,20)
# wn.exitonclick()

#fourth lab exercises
# import turtle 
# wn = turtle.Screen()
# polygon = turtle.Turtle()
# polygon.pencolor("pink")
# wn.bgcolor("lightgreen")
# polygon.pensize(3)
# def drawPoly(t,side,length):
#     for i in range(side):
#         t.forward(length)
#         t.left(360/side)
# print(drawPoly(polygon,9,100))
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# square = turtle.Turtle()
# wn.bgcolor("lightgreen")
# square.pencolor("blue")
# def drawSquare(t,side,length):
#     for i in range(side):
#         t.forward(length)
#         t.left(360/side)
# def turningSquare(t,angle,num):
#     for i in range(num):
#         angle = 360/num
#         drawSquare(square,4,100)
#         t.left(angle)
# print(turningSquare(square,18,20))
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# square1 = turtle.Turtle()
# square1.penup()
# square1.goto(200,0)
# square1.pendown()
# square1.speed(0)
# square2 = turtle.Turtle()
# square2.penup()
# square2.goto(-200,0)
# square2.pendown()
# square2.speed(0)
# wn.bgcolor("lightgreen")
# square1.pencolor("navyblue")
# square2.pencolor("navyblue")
# def drawSquare(t,side,length,angle):
#     for i in range(side):
#         t.forward(length*i)
#         t.left(angle)

# drawSquare(square1,100,2,90)
# drawSquare(square2,100,2,91)
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# triangle = turtle.Turtle()

# def drawtriangle(t,side,length):
#     for i in range(side):
#         t.forward(length)
#         t.left(360/side)
# print(drawtriangle(triangle,3,100))
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# star = turtle.Turtle()
# star.pencolor("pink")
# wn.bgcolor("lightgreen")
# def drawStar(t,side,angle):
#     for i in range(5):
#         t.right(angle)
#         t.forward(side)
# def draw5Star(t,angle):
#     for i in range(5):
#         t.penup()
#         t.right(angle)
#         t.forward(350)
#         t.pendown()
#         drawStar(star,100,144)
# print(draw5Star(star,144))
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# sprite = turtle.Turtle()
# def drawSprite(t,legnum,leglen):
#     for i in range(legnum):
#         t.stamp()
#         t.forward(leglen)
#         t.backward(leglen)
#         t.left(360/legnum)
# print(drawSprite(sprite,15,120))
# wn.exitonclick()


#fifth lab exercises
# def sumTo(n):
#     sum = (n*(n+1))/2
#     return sum
# print(sumTo(10))

# import turtle
# wn = turtle.Screen()
# star = turtle.Turtle()
# def drawStar(t,n,sidesize):
#     for i in range(n):
#         if n>=3 and n%2==1:
#             t.right(180-(180/n))
#             t.forward(sidesize)
# print(drawStar(star,33,100))
# wn.exitonclick()

# def sumTo(n):
#     sum = 0
#     for count in range(n):
#         sum = sum + n
#     return sum 
# print(sumTo(10))

# def takenum(n):
#         if n<0:
#             return "n is negative"
#         elif n>0:
#             return "n is positive"
#         else:
#             return "n is zero"
# print(takenum(-10))

#sixth lab exercises
# import random
# def Choosenum(n):
#     secretnum = random.randrange(1,10)
#     while n != secretnum:

#         if n > secretnum:
#             print("too big")
#         elif n < secretnum:
#             print("too small")
#         else:
#             print("correct")
# print(Choosenum(1))


#seventh lab exercises
# def is_odd(n):
#     if n%2 == 1:
#         return True
#     else:
#         return False
# print(is_odd(2))

# def LeapYear(year):
#     leap = False
#     if year//400:
#         leap= True
#     elif year//100:
#         leap = False
#     elif year//4:
#         leap= True
#     return leap
# print(LeapYear(2000))

#string exercises
# def reverses(s):
#     backward= ""
#     for letter in s:
#         backward = letter + backward
#     return backward
# print(reverses("hello"))

# def palindrom(word):
#     word2= ""
#     for letter in word:
#         word2 = letter + word2
#         if word2 == word:
#             return "word is palindrom"
#         else:
#             return "word is not palindrom"
#     return word2
# print(palindrom("hello"))


# text = "this is an example"
# print(text.count("example"))

# text = "this is an example"
# print(text.count("i"))

# def firstnonRepeating(s):
#     for char in s:
#         if s.count(char)==1:
#             return char

#     return " "
# print(firstnonRepeating("stress"))


# def chooseAlpha(s):
#     new = " "
#     Alphalist=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
#     for char in s:
#         if char in Alphalist:
#             new = new + char
#     return new
# print(chooseAlpha("2elif1asd35"))

# def compressString(s):
#     if not s:
#         return ""
#     new = s[0]
#     for i in range(1,len(s)):
#         if s[i] != s[i-1]:
#             new += s[i]
#     return new
# print(compressString("aabbccgddf"))


# def countwords(words):
#     total = 0
#     for word in words:
#         if word =="stop":
#             break
#         total = total + 1
#     return total
# print(countwords(["hello","world","my","stop","name","is","elif","stop","hi","exit"]))

# myList = [10,"apple",3.14,True,10,5]
# myList.append("banana")
# myList.append(False)
# myList.insert(1,"orange")
# print(myList.count(10))
# print(myList.pop(myList.index(10)))
# print(myList)

# def sumOfEvensSquares(nums):
#     total = 0
#     for number in nums:
#         if number %2==0:
#             total= total + number**2
#     return total
# print(sumOfEvensSquares([1,2,3,4,5]))

# import random 
# def guessNum(guess):
#     n = random.randint(1,10)
#     while guess!=n:
#         if n > guess:
#             print("too big")
#         elif n<guess:
#             print("too small")
#     print("correct")
# print(guessNum(5))

# def examMark(note):
#     if note >= 90:
#         return "A"
#     elif 90>note>=80:
#         return "B"
#     elif 80>note>=70:
#         return "C"
#     elif 70>note>=60:
#         return "D"
#     elif note<60:
#         return "F"
# print(examMark(87))

# def findVowels(sentence):
#     Vowels = ["e","u","i","o","a","u"]
#     for vowel in sentence:
#         if vowel in Vowels:
#             print(vowel)
# print(findVowels("Programming Fundamentals"))

# def LeapYear(year):
#     if year%400==0:
#         return True
#     elif year%100==0:
#         return False
#     elif year%4==0:
#         return True
#     else:
#         return False
# print(LeapYear(2000))
# print(LeapYear(1900))

# import turtle
# wn = turtle.Screen()
# polygon = turtle.Turtle()
# def drawPolygon(t,sidenum,sidesize):
#     for i in range(sidenum):
#         t.forward(sidesize)
#         t.left(360/sidenum)
# print(drawPolygon(polygon,13,100))
# wn.exitonclick()

# def sumUntilEven(numlist):
#     sum = 0
#     numlist = [1,3,5,7,12]
#     for number in numlist:
#         if number%2==0:
#             break
#         sum = sum +number
#     return sum
# print(sumUntilEven([1,3,5,7,12]))

# def averageevennumbers(numlist):
#     tot=0
#     cnt=0
#     if len(list)<1:
#         return 0
#     for i in numlist:
#         if i%2==0:
#                 tot +=i
#                 cnt +=1
#     return tot/cnt
# print(averageevennumbers([1,2,3,4,5,6,7]))

# import math
# def findhypot(side1,side2):
#     formula = math.hypot(side1,side2)
#     return formula
# print(findhypot(3,4))

# def wordslength(wordlist):
#     total = 0
#     for word in wordlist:
#         if len(word)==5:
#             total +=1
#     return total
# print(wordslength(["hello","world","my","name","is","apple"]))

# def SumOfSquares(numlist):
#     return sum(x**2 for x in numlist)
# List = [1,2,3,4,5]
# print(SumOfSquares(List))


# def SumOfSquares(numList):
#     squareList=0
#     for num in numList:  
#         squareList=squareList+num**2
#     return squareList
# print(SumOfSquares([1,2,3,4]))

# def averageEvenNumbers(list):
#     tot=0
#     cnt=0
#     if len(list) < 1:
#         return 0
#     for i in list:
#         if i % 2 == 0:
#             cnt+=1
#             tot+=i
#     return tot/cnt
# print(averageEvenNumbers([1,2,3,4,5]))

# sınavda yaptığın olabilir (son soru)
# def coreword(text):
#     Alpha1 =["A","B","R","I","S"]
#     Alpha2= ["D","E","F","G","H"]
#     for letter in text:
#         if letter in text:
#             print(text.replace(letter.index(),Alpha1,Alpha2))

# print(coreword("BARIS"))

import turtle
wn = turtle.Screen()
multi = turtle.Turtle()
minus = turtle.Turtle()
multi.penup()
multi.goto(-100,100)
multi.pendown()
minus.penup()
minus.goto(-100,-100)
minus.pendown()
def drawmulti(t,size):
    for i in range(1):
        t.left(53)
        t.forward(140)
        t.penup()
        t.left(127)
        t.forward(size)
        t.left(143)
        t.pendown()
        t.forward(140)
def drawminus(t,size):
    for i in range(1):
        t.forward(size)

print(drawmulti(multi,100))
print(drawminus(minus,100))
wn.exitonclick()