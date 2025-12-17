# name = "hello world"
# print(str.capitalize(name))

# name = "HELLO WOrld"
# print(str.casefold(name))

# name = "hello world"
# print(str.center(name,17,"$"))

# neo = "hi I like your name and I like your hat"
# print(str.count(neo,"I",2,38))

# neo = "hi I like your name and I like your hat"
# print(str.find(neo,"like",10,39))

# neo = "hi I like your name and I like your hat"
# print(str.endswith(neo,"hat",5,44))

# neo = "E\tl\ti\tf"
# print(str.expandtabs(neo,7))

# neo = "hi I like your hat and I like your name"
# print(str.index(neo,"name",4,40))

# neo = "hi I like your name and I like your hat"
# neo2 = "jamesbond007"
# print(str.isalnum(neo))
# print(str.isalnum(neo2))

# neo = "Hi I like your name and I like your hat"
# neo2 = "HiIlikeyournameandIlikeyourhat"
# print(str.isalpha(neo))
# print(str.isalpha(neo2))

# neo = "240709029"
# print(str.isdecimal(neo))

# neo = "0234"
# print(str.isdigit(neo))

# neo = "neo_21"
# print(str.isidentifier(neo))

# neo = "i like your name"
# print(str.islower(neo))

# neo =  "569346592"
# print(str.isnumeric(neo))

# neo = "hi i like your name and i like your hat"
# print(str.isprintable(neo))

#neo = "     "
#print(str.isspace(neo))

# neo = "Himynameiselif"
# print(str.istitle(neo))

# neo = "ELİFISSUCCESSFUL"
# print(str.isupper(neo))

# neo = {"","MynameisElif ",""} 
# sep = "&"
# print(sep.join(neo))

# neo = "My name Is ELİf"
# print(str.lower(neo))

#neo = "iiii Hi Im Elif "
#print(str.lstrip(neo,"iiii"))

# neo = "Hi my name is Elif"
# print(str.replace(neo,"a","b"))

# neo = "hi I like your hat and I like your name"
# print(str.rfind(neo,"hat",))

# neo = "hi I like your hat and I like your name"
# print(str.rindex(neo,"name",))

#neo = "Elif"
#print(str.rjust(neo,7,"o"))

# neo = "My name is Elif"
# print(str.rsplit(neo,"e"))

# neo = "My name is Elif aaaa"
# print(str.rstrip(neo,"a"))

# neo = "my name is elif"
# print(str.split(neo, " ",2))

# neo = "my name is Elif"
# print(str.splitlines(neo,4))

# neo = "my name is Elif"
# print(str.startswith(neo,"my",))

# neo = "My NAme is ELif"
# print(str.swapcase(neo))

# neo = "my name is elif"
# print(str.title(neo))

#neo = "my name is elif"
#print(str.upper(neo))

# neo = "my name is elif"
# print(str.zfill(neo,30))

# neo = "   my name is elif    "
# print(str.strip(neo))

#EXERCİSES

# def reverseword(word):
#     word = word.upper()
#     backwards = ""
#     for letter in word:
#         backwards = letter+backwards
#     return backwards
# print(reverseword("python"))

# sentence = str(input("please write a sentence:"))
# def findVowels():
#     Vowels =["e","u","o","a","i","A","E","U","I","O"]
#     total = 0
#     for letter in sentence:
#         if letter in Vowels:
#             total= total + 1
#     return total
# print(findVowels())

# word = str(input("please enter a word:"))
# def isPalindrome():
#     backward= ""
#     for letter in word:
#         backward= letter+backward
#     if backward == word:
#             return "word is palindrome"
#     else:
#             return "word is not palindrome"
#     return backward
# print(isPalindrome())

# alist=[14,25,30,7,42,19,50,11]
# def isEven(alist):
#     blist=[]
#     for numbers in alist:
#         if numbers%2==0:
#             blist.append(numbers)
#     return blist
# print(isEven([14,25,30,7,42,19,50,11]))