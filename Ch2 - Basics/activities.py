#Guess number from 1-9
#guess= 7

#yourNum= int(input("Guess a number between 1 and 9: "))

#while (yourNum != guess):
#        yourNum= int(input("Guess a number between 1 and 9: "))
#print("Well guessed!")

#==============================

#Triangle
#n= 5
#for i in range(n):
#    for j in range(i):
#        print("*", end="")
#    print('')

#for i in range(n, 0, -1):
#    for j in range(i):
#        print("*", end="")
#    print('')

#==============================

#Reverse Word

#word= input("Enter a word: ")

#for char in range(len(word) -1, -1, -1):
#    print(word[char], end="")
#print("\n")

#==============================
#Count Even Odd Numbers

#num= int(input("Enter number: "))

#if num % 3 == 0 and num % 5 ==0 : print("FizzBuzz")
#elif num % 5 == 0 : print("Buzz")
#elif num % 3 == 0 : print("Fizz") 
#else: print(num)

#Palindrome

#str=input("Enter word :")
#i=0
#for i in range(len(str)):
#    if str[i]!=str[-1-i]:
#        print('It is not a palindrome')
#        break
#else:
#    print('It is a palindrome')

#UNPACKING

# fruits = ["orngae", "apple", "pineapple"]
# x, y, z = fruits
# print(fruits)
# print(x)
# print(y)
# print(z)

# student = ["2018","Cruz", 21, 93245, "Calumpit, Bulacan", True]
# stud_id, name, age, num, address, status = student
# print(stud_id)
# print(name)
# print(age)
# print(num)
# print(address)
# print(status)

# a= '1'
# b = "1"

# print(a + b)



#PRINT NATURAL NUMBERS 1-10

# i = 0
# while (i < 10):
#     i += 1
#     print(i)


#INCREMENT USING LOOP

# row = 5
# # start: 1
# # stop: row+1 
# # step: 1
# # run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")


#===========================================
#Calculate the sum of all numbers from 1 to a given number    
# num = int(input("Enter a number: "))
# sum=0
# for i in range(0, num+1, 1):
#     sum += i
# print("Sum is: " , sum)


#===========================================
#Write a program to print multiplication table of a given number

# num= int(input("Enter num: "))
# product=0
# for i in range(1, 11):
#     product = i * num
#     print(product)



#============================================
#Display numbers from a list using loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
# # iterate each item of a list
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # check if number is divisible by 5
#     elif item % 5 == 0:
#         print(item)


#================================================
#Count the total number of digits in a number

# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10

#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)


#================================================
#Print the following pattern (triangle)



# for i in range(0, 5+1):
#      for j in range(1, i+1, 1):
#          print(j, end=" ")
#      print()

# for i in range(0,5+1):
#      for j in range(5-i,0,-1):
#          print(j,end=' ')
#      print()



# year= int(input("Leap year: "))
# if (year %4 == 0 and year %100 !=0) or (year % 400 == 0): print("Leap year") 

#===================================================
#Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]

# size= len(list1) -1

# for i in range(size,-1, -1):
#     print(list1[i])

#===============================================
#Display numbers from -10 to -1 using for loop

# for i in range(-10, 0, 1):
#     print(i)

#======================================================
#Use else block to display a message “Done” after successful execution of for loop

# for i in range(5):
#     print(i)
# else:
#     print("Done!")

#=====================================================
#Write a program to display all prime numbers within a range

# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)


#===================================================== TRY!!!!!!!!
#Fibonacci
# count= 10
# num1=0
# num2=1
# print(num1, end=" ")
# for i in range(1,count):
#     temp = num1 + num2 
#     num1 = num2 
#     num2 = temp  
#     print(num1, end=" ")

#0  1  1  2  3  5  8  13  21  34

#===================================================== TRY!!!!!!!!
#Reverse a Number


#Rectangle
# height = int(input("Enter the height: "))
# print("+" + "=" * 10 + "+")
# print(("+" + " " * 10 + "+\n") * (height - 2), end="")
# print("+" + "=" * 10 + "+")

#========================================================
#Reverse
#word= (input("Enter a word: "))

# for char in range(len(word) -1, -1, -1 ):
#     print(word[char], end='')


#print(word[::-1])







    

