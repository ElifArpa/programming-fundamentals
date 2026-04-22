# student_datas ="""joe 10 15 20 30 40
# bill 23 16 19 22
# sue 8 22 17 14 32 17 24 21 2 9 11 17
# grace 12 28 21 45 26 10
# john 14 32 25 16 89""" 
# data_file = "studentDatas.txt"
# with open(data_file,"w") as  file:
#     file.write(student_datas)

# with open(data_file,"r") as file:
#     for line in file:
#         items = line.split()
#         student_name = items[0]
#         student_grade = items[1:]
#         try:
#             grades = [int(g) for g in student_grade]
#         except ValueError:
#             print("there are no suitable value for ",student_name)
#             continue
#         if grades:
#             average = sum(grades)/len(grades)
#             print("student name:",student_name,"average grade:",average)


# with open(data_file,"r") as file:
#     for line in file:
#         items = line.split()
#         student_name = items[0]
#         student_grade = items[1:]
#         try:
#             grades = [int(g) for g in student_grade]
#         except ValueError:
#             print("there are no suitable value for",student_name) 
#         if grades:
#             mingrade = min(grades)
#             maxgrade = max(grades)
#             print("student name:",student_name,"/min grade:",mingrade,"/max grade:",maxgrade)



# import turtle
# dino = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("gray")
# dino.pencolor("purple")
# dino.pensize(2)
# with open("mystery.txt","r") as file:
#     for line in file:
#         items = line.strip()

#         if items == "UP":
#             dino.penup()
#         elif items == "DOWN":
#             dino.pendown()
#         else:
#             x,y = map(int,line.split())
#             dino.goto(x,y)
# wn.exitonclick()

# def savenumbers(filename):
#     numbers = []
#     for i in range(5):
#         number = int(input("enter a number:"))
#         numbers.append(number)
#     with open(filename,"w") as file:
#         for num in numbers:
#             file.write(str(num) + "\n")

# def read_and_sum(filename):
#     total = 0
#     with open(filename,"r") as file:
#         for line in file:
#             total += int(line)
#         return total
# savenumbers("numbers.txt")
# result = read_and_sum("numbers.txt")
# print("Sum:",result)


#yanlış çalışıyor
# def countpython(filename):
#     count=0
#     with open("text.txt","r") as file:
#         for line in filename:
#             items = line.strip()
#             if items in filename:
#                 count +=1
#         return count  
# print(countpython("text.txt"))    


def readnames(filename):
    with open("students.txt","r") as file:
        return file.read().splitlines()
def sortList(students):
    students.sort()
    return students

    


