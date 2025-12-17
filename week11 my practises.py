#s = "   Hello World"
#print(str.ljust(s,14,"!"))
#print(str.rjust(s,14,"*"))
#print(s.index("World"))
#print(s.count("Hello"))
#print(s.replace("World","Python"))
#print(str.strip(s))
#print(s.rstrip("d"))



# def count_vowels(s):
#     vowels = ["e","u","o","ü","a","i","ö"]
#     vowel = 0
#     for letter in s:
#         if letter in vowels:
#             vowel += 1
#     return vowel
# print(count_vowels("hello world"))



# def sum_of_digit(s):
#     sum = 0
#     for digit in s:
#         if digit.isdigit():
#             sum += int(digit)
#     return sum
# print(sum_of_digit("ax3g5jd6"))



# words = ["hello","world","my","name","is","Elif"]
# total = 0
# for word in words:
#     if len(word) == 5:
#         total +=1
# print(total)




# words = ["hello","world","my","name","is","Elif","and","his","name","is","Sam"]
# sum = 0
# for word in words:
#     if word =="Sam":
#         break
#     sum += len(word)
# print(sum)



# def replace_all(s,old,new):
#     return new.join(s.split(old))
#     return s.replace(old,new)
# print(replace_all("hello world","o","a"))
