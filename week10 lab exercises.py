# def is_odd(n):
#     if n%2==1:
#         return True
#     else:
#         return False
# print(is_odd(-100))



# def takeYears(year):
#     if year%400==0:
#         return "year is a Leap Year"
#     elif year%100==0:
#         return "year is NOT a Leap Year"
#     elif year%4==0:
#         return "year is a Leap Year"
#     else:
#         return "year is NOT a Leap Year"
    
# print(takeYears(2023))



# def print_triangular_numbers(n):
#     for i in range(n,n+1):
#         formula = n*(n+1)/2
#         return formula
    
# print(print_triangular_numbers(5))



# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
        
# def until_prime(n):
#     primes = []
#     for i in range(2,n):
#         if is_prime(i):
#             primes.append(i)
#     return primes
# print(until_prime(8))


# def reverse(text):
#     backwards = ''
#     for char in text:
#         backwards = char  + backwards
#     return backwards
    
# print(reverse('Elif'))


# def remove(text):
#     print(str.replace(text,"i","a"))

# remove("hi my name is Elif")


# def remove_dups(text):
#     text2 = " " 
#     for i in range(len(text)):
#         if str.find(text,"o")==-1:
#             text2 += text
#     return text2

    
# print(remove_dups("hello world"))



