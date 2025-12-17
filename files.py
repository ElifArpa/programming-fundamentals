# students = ["jack","ben","alice"]
# file_path = "C:/Users/elifa/OneDrive/Desktop/output.txt"


# try:
#     with open(file_path,"a") as file: #"r"=read,"a"=append file,"w"=write,"x"=give error if that file is created 
#         for student in students:
#             file.write(student+"\n")
#         print("txt file",file_path,"was created")
# except FileExistsError:
#     print("That file already exists!")

# file_path = "C:/Users/elifa/OneDrive/Desktop/output.txt"
# try:  #if we forgot the file road we can use try except
#     with open(file_path,"r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("you do not have permission to read that file")


Datas ="joe 10 15 20 30 40\n" \
"bill 23 16 19 22\n" \
"sue 8 22 17 14 32 17 24 21 2 9 11 17\n" \
"grace 12 28 21 45 26 10\n" \
"john 14 32 25 16 89"
data_file= "C:/Users/elifa/OneDrive/Desktop/students.txt"
with open(data_file,"w") as file:
    file.write(Datas)


with open(data_file,"r") as file:

    for line in file:
        items = line.split()
        if len(items[1:])>6:
            print(items[0])



