# Datas ="joe 10 15 20 30 40\n" \
# "bill 23 16 19 22\n" \
# "sue 8 22 17 14 32 17 24 21 2 11 17\n" \
# "grace 12 28 21 45 26 10\n" \
# "john 14 32 25 16 89"
# data_file= "C:/Users/elifa/OneDrive/Desktop/students.txt"
# with open(data_file,"w") as file:
#     file.write(Datas)


# with open(data_file,"r") as file:

#     for line in file:
#         items = line.split()
#         if len(items[1:])>6:
#             print(items[0])

# with open(data_file,"r") as file:
#         for line in file:
#             items = line.split()
#             student_name = items[0]
#             student_grade = items[1:]
#             try:
#                  grades = [int(g) for g in student_grade]
#             except ValueError:
#                  print("there are wrong value in the grades of",student_name)
#                  continue
#             if grades:
#                  average = sum(grades)/len(grades)
#                  print("student Name:",student_name,"/Average grade:",average)
                 
               
# with open(data_file,"r") as file:
#     for line in file:
#         items = line.split()
#         student_name = items[0]
#         student_grade = items[1:]
#         try:
#             grades = [int(g) for g in student_grade]
#         except ValueError:
#             print("there are no suitable values in grades of",student_name)
#         if grades:
#             maxgrade = max(grades)
#             print("student name:",student_name,"/max grade:",maxgrade)
        

# datas = ("44 71\n"
# "79 37\n"
# "78 24\n"
# "41 76\n"
# "19 12\n"
# "19 32\n"
# "28 36\n"
# "22 58\n"
# "89 92\n"
# "91 6\n"
# "53 7\n"
# "27 80\n"
# "14 34\n"
# "8 81\n"
# "80 19\n"
# "46 72\n"
# "83 96\n"
# "88 18\n"
# "96 48\n"
# "77 67")
# filename = "C:/Users/elifa/OneDrive/Desktop/labdata.txt"
# with open(filename,"w") as file:
#     file.write(datas)







# import turtle

# def plotRegression(filename):
#     # ----------------------------
#     # Veriyi dosyadan oku
#     # ----------------------------
#     x_vals = []
#     y_vals = []

#     with open(filename, "r") as file:
#         for line in file:
#             x, y = line.split()
#             x_vals.append(float(x))
#             y_vals.append(float(y))

#     n = len(x_vals)

#     # ----------------------------
#     # Ortalama hesapları
#     # ----------------------------
#     x_bar = sum(x_vals) / n
#     y_bar = sum(y_vals) / n

#     # ----------------------------
#     # Eğim (m) hesaplama
#     # ----------------------------
#     numerator = 0
#     denominator = 0

#     for i in range(n):
#         numerator += x_vals[i] * y_vals[i]
#         denominator += x_vals[i] ** 2

#     m = (numerator - n * x_bar * y_bar) / (denominator - n * x_bar ** 2)

#     # ----------------------------
#     # Turtle ayarları
#     # ----------------------------
#     screen = turtle.Screen()

#     min_x, max_x = min(x_vals), max(x_vals)
#     min_y, max_y = min(y_vals), max(y_vals)

#     screen.setworldcoordinates(
#         min_x - 10, min_y - 10,
#         max_x + 10, max_y + 10
#     )

#     t = turtle.Turtle()
#     t.speed(0)
#     t.hideturtle()

#     # ----------------------------
#     # Noktaları çiz
#     # ----------------------------
#     t.color("blue")
#     for x, y in zip(x_vals, y_vals):
#         t.penup()
#         t.goto(x, y)
#         t.dot(6)

#     # ----------------------------
#     # Regresyon doğrusunu çiz
#     # y = ȳ + m(x − x̄)
#     # ----------------------------
#     t.color("red")
#     t.penup()
#     x1 = min_x
#     y1 = y_bar + m * (x1 - x_bar)
#     t.goto(x1, y1)
#     t.pendown()

#     x2 = max_x
#     y2 = y_bar + m * (x2 - x_bar)
#     t.goto(x2, y2)

#     screen.mainloop()


# # Fonksiyon çağrısı
# plotRegression(filename)

       
# with open(data_file,"r") as file:
#     for line in file:
#         items = line.split()
#         student_name = items[0]
#         student_grade = items[1:]
#         try:
#             grades = [int(g) for g in student_grade]
#         except ValueError:
#             print("there are no suitable values in grades of",student_name)
#         if grades:
#             maxgrade = max(grades)
#             mingrade = min(grades)
#             print("student name:",student_name,"/min grade:",mingrade,"/max grade:",maxgrade)



mystery_datas ="""UP
-218 185
DOWN
-240 189
-246 188
-248 183
-246 178
-244 175
-240 170
-235 166
-229 163
-220 158
-208 156
-203 153
-194 148
-187 141
-179 133
-171 119
-166 106
-163 87
-161 66
-162 52
-164 44
-167 28
-171 6
-172 -15
-171 -30
-165 -46
-156 -60
-152 -67
-152 -68
UP
-134 -61
DOWN
-145 -66
-152 -78
-152 -94
-157 -109
-157 -118
-151 -128
-146 -135
-146 -136
UP
-97 -134
DOWN
-98 -138
-97 -143
-96 -157
-96 -169
-98 -183
-104 -194
-110 -203
-114 -211
-117 -220
-120 -233
-122 -243
-123 -247
-157 -248
-157 -240
-154 -234
-154 -230
-153 -229
-149 -226
-146 -223
-145 -219
-143 -214
-142 -210
-141 -203
-139 -199
-136 -192
-132 -184
-130 -179
-132 -171
-133 -162
-134 -153
-138 -145
-143 -137
-143 -132
-142 -124
-138 -112
-134 -104
-132 -102
UP
-97 -155
DOWN
-92 -151
-91 -147
-89 -142
-89 -135
-90 -129
-90 -128
UP
-94 -170
DOWN
-83 -171
-68 -174
-47 -177
-30 -172
-15 -171
-11 -170
UP
12 -96
DOWN
9 -109
9 -127
7 -140
5 -157
9 -164
22 -176
37 -204
40 -209
49 -220
55 -229
57 -235
57 -238
50 -239
49 -241
51 -248
53 -249
63 -245
70 -243
57 -249
62 -250
71 -250
75 -250
81 -250
86 -248
86 -242
84 -232
85 -226
81 -221
77 -211
73 -205
67 -196
62 -187
58 -180
51 -171
47 -164
46 -153
50 -141
53 -130
54 -124
57 -112
56 -102
55 -98
UP
48 -164
DOWN
54 -158
60 -146
64 -136
64 -131
UP
5 -152
DOWN
1 -150
-4 -145
-8 -138
-14 -128
-19 -119
-17 -124
UP
21 -177
DOWN
14 -176
7 -174
-6 -174
-14 -170
-19 -166
-20 -164
UP
-8 -173
DOWN
-8 -180
-5 -189
-4 -201
-2 -211
-1 -220
-2 -231
-5 -238
-8 -241
-9 -244
-7 -249
6 -247
9 -248
16 -247
21 -246
24 -241
27 -234
27 -226
27 -219
27 -209
27 -202
28 -193
28 -188
28 -184
UP
-60 -177
DOWN
-59 -186
-57 -199
-56 -211
-59 -225
-61 -233
-65 -243
-66 -245
-73 -246
-81 -246
-84 -246
-91 -245
-91 -244
-88 -231
-87 -225
-85 -218
-85 -211
-85 -203
-85 -193
-88 -185
-89 -180
-91 -175
-92 -172
-93 -170
UP
-154 -93
DOWN
-157 -87
-162 -74
-168 -66
-172 -57
-175 -49
-178 -38
-178 -26
-178 -12
-177 4
-175 17
-172 27
-168 36
-161 48
-161 50
UP
-217 178
DOWN
-217 178
-217 177
-215 176
-214 175
-220 177
-223 178
-223 178
-222 178
UP
-248 185
DOWN
-245 184
-240 182
-237 181
-234 179
-231 177
-229 176
-228 175
-226 174
-224 173
-223 173
-220 172
-217 172
-216 171
-214 170
-214 169
UP
-218 186
DOWN
-195 173
-183 165
-175 159
-164 151
-158 145
-152 139
-145 128
-143 122
-139 112
-138 105
-134 95
-131 88
-129 78
-126 67
-125 62
-125 54
-124 44
-125 38
-126 30
-125 27
-125 8
-126 5
-125 -9
-122 -15
-115 -25
-109 -32
-103 -39
-95 -42
-84 -45
-72 -47
-56 -48
-41 -47
-31 -46
-18 -45
-1 -44
9 -43
34 -45
50 -52
67 -61
83 -68
95 -80
112 -97
142 -115
180 -132
200 -146
227 -159
259 -175
289 -185
317 -189
349 -190
375 -191
385 -192
382 -196
366 -199
352 -204
343 -204
330 -205
315 -209
296 -212
276 -214
252 -208
237 -202
218 -197
202 -193
184 -187
164 -179
147 -173
128 -168
116 -164
102 -160
88 -158
78 -159
69 -162
57 -164
56 -165
51 -165
UP
68 -144
DOWN
83 -143
96 -141
109 -139
119 -146
141 -150
161 -155
181 -163
195 -169
208 -179
223 -187
241 -191
247 -193
249 -194
UP
-6 -141
DOWN
-15 -146
-29 -150
-42 -154
-51 -153
-60 -152
-60 -152
UP
-90 -134
DOWN
-85 -131
-79 -128
-78 -123
-80 -115
-82 -106
-80 -101
-76 -101
UP
-81 -132
DOWN
-76 -130
-71 -126
-72 -124
UP
43 -118
DOWN
44 -125
47 -135
41 -156
37 -160
40 -166
47 -171
47 -171
UP
-106 -153
DOWN
-107 -167
-106 -178
-109 -192
-114 -198
-116 -201""" 
data_file = "C:/Users/elifa/OneDrive/Desktop/mysterydatas.txt"
with open(data_file,"w") as file:
    file.write(mystery_datas)

import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # hızlı çizmesi için

file = open(data_file, "r")

for line in file:
    line = line.strip()

    if line == "UP":
        t.penup()
    elif line == "DOWN":
        t.pendown()
    else:
        x, y = line.split()
        t.goto(int(x), int(y))

file.close()

turtle.done()
wn.exitonclick()
