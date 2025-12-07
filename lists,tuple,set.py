# collection = single "variable" used to store multiple values
#  List = [] ordered and changeable. Duplicates OK
#  Set = {} unordered and immutable, but  Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicate OK. FASTER
# 
# fruits = ["apple","banana","coconut","orange"]
# print(fruits)   #writes the list
# print(fruits[0])  #writes the element in the index of 0
# print(fruits[0:3]) #writes the elements 0,1,2 first include second not
# print(fruits[2:4]) #writes 2,3 elements
# print(fruits[::2]) #starts from 0 and jump 2 
# print(fruits[::-1]) #writes list from reverse

# for fruit in fruits:   
#     print(fruit)      #bottom to bottom in order
 
#print(dir(fruits))  # that show the commands of list
#print(help(fruits)) # that show how us use these commands
# print(len(fruits))   # that writes the length of the list
# print("apple" in fruits) #that writes a boolean if its true or false
# fruits[0] = "pineapple" #that changes the value of the index which we are inputted
#fruits.append("pineapple") #that add an element to the end of the list
#fruits.remove("apple")  #that removes the element which we inputted from list
#fruits.insert(0,"pineapple") #that insert the element at the index which we both inputted
#fruits.sort() #that is sorted the elements of the list (alphabetical)
#fruits.reverse() #that is reversed the list
#fruits.clear() #to clear the list its give the empty list
#print(fruits.index("apple")) #that gives the index of element which we inputted
#print(fruits.count("apple")) #that count the number of element which we are inputted
# print(fruits)


# fruits = {"apple","banana","coconut","orange","coconut"}
# print(dir(fruits))  #that show the commands of the set
# print(help(fruits)) #that show how us use the commands
# print(len(fruits))  #that writes the length of the set
# print("pineapple" in fruits) #that writes a boolean if its true or false
#fruits.add("pineapple") #that add the element to the list again inordered
#fruits.remove("apple") #that removes the element which we inputted
#fruits.pop() #that remove whatever element is first so it can be change
#fruits.clear() #that is clear the our set
# print(fruits)


#fruits = ("apple","banana","coconut","orange","coconut")
#print(dir(fruits)) #display the methods
#print(help(fruits)) #display a description of these methods
#print(len(fruits))  #writes the length of the tuple
#print("pineapple" in fruits) #that writes a boolean if its true or false
#print(fruits.index("apple")) #that gives the index of element which we inputted
#print(fruits.count("coconut")) #that count the number of element which we are inputted
#print(fruits)


#BEGINNER EXERCİSES
# alist = ["apple","coconut","date","banana","mango"]
# print(alist[0::2])
# alist.append("pineapple")
# alist.insert(1,"blackberry")
# print(alist.pop())
# print(len(alist))
# print(alist.count("date"))
# blist = alist[:3]
# clist = alist[1:-1]
# dlist = alist[::-1]
# alist.sort()
# alist.reverse()
# blist = alist.copy()
# print(blist)


# atuple =("Jack",[35,1.87])
# (Name, Age, Height) = atuple
# print(Name)
# print(Age)
# print(Height)
# btuple =("Mary",33,1.79)
# ctuple = (atuple + btuple)
# alist = list(atuple)
# alist.append("Mary")
# alist = tuple(atuple)
# btuple = (1,2,1,3,4,3,5,5,3,7)
# print(btuple.count(3))
# print(btuple.index(3))
# print(btuple)

# aset ={"pink","blue","gray","yellow","black"}
# aset.add("white")
# aset.add("gray")
# zlist = ["gray","yellow","gray","black","gray","blue"]
# zset = set(zlist)
# zset = list(zlist)
# print(zset)

#setA = {"cat","dog","bird","fish"}
#setB = {"bird","donkey","dog","owl"}
#print(setA.intersection(setB))
#print(setA.union(setB))
#print(setA.difference(setB))

setC = {"bird","dog","cat","horse","fish","dog"}
# setC.remove("bird")
# setC.remove("black")  #key error
setC.discard("black")

print(setC)



