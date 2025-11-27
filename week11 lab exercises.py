# myList = [76,92.3,"hello",True,4,76]
# myList.append("apple")
# myList.append(76)
# myList.insert(2,"cat")
# print(myList.index("hello"))
# myList.insert(0,99)
# print(myList.count(76))
# myList.remove(76)
# myList.pop(myList.index(True))
# print(myList)

# list_of_nums = [2,3,4]
# def sum_of_squares(nums):
#     sum = 0
#     for number in nums:
#         sum = sum + number**2

#     return sum
# print(sum_of_squares(list_of_nums))


# list = [1,2,3,4,5,6,7,8,9]
# def sum_evens(evens):
#     sum = 0
#     for number in evens:
#         if number%2 ==0:
#             sum += number

#     return sum 
# print(sum_evens(list))


# list = ["local","apple","glass","computer","output","python"]
# count = 0
# for word in list:
#     if len(word) ==5:
#         count +=1

# print(count)


# list = [1,2,3,4,5,6,7,8,9]
# def sum_nums(numbers):
#     sum = 0
#     list.remove(2)
#     for number in numbers:
#         sum += number
#     return sum
# print(sum_nums(list))


# list = ["local","apple","glass","sam","computer","output"]
# count = list.index("sam")+1
# print(count)


def replace_word(s,old,new):
    return new.join(s.split(old))
    return s.replace(old,new)
print(replace_word("Mississippi","i","I"))



# def maxValue(list):
#     max= list[0]
#     for number in list:
#         if number>max:
#             max = number
#     return max
# list =[1,2,3,4,5,6,7,8,9]
# print(maxValue(list))



