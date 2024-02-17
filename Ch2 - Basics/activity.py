# # Get input from the user
# input_string = input("Enter the string: ")

# # Clean the input string using list comprehension
# cleaned_string = ''.join(char for char in input_string if char.isalnum())

# # Print the cleaned string
# print("The cleaned string is:", cleaned_string)


#------LONGEST WORD----------------
# input_string = input("Enter a string: ")

# words = input_string.split()

# longest_word = ""
# max_length = 0

# for word in words:
#     if len(word) > max_length:
#         max_length = len(word)
#         longest_word = word


# print("Longest word:", longest_word)


#-----Duplicate Strings (*)---------
# s = "Python"

# # print(s*3)


# #-------LENGTH-----------
# print(len(s))

# #-------UPPER CASE--------
# print(s.upper())

# #------CAPETALIZED-------
# print(s.capitalize())

# #-----LOWE----------
# print(s.lower())

# #------SWAPCASE------
# print(s.swapcase())

#-----BOOLEAN MEDTHODS (is numeric and alpha)-----------
# number = "5"
# letters = "abcdef"

# print(number.isnumeric())
# print(letters.isnumeric()) 

# print(number.isalpha())
# print(letters.isalpha()) 


# password1 = "abcd1234"
# password2 = "abcd1234@"

# print(password1.isalnum())
# print(password2.isalnum()) 


# str1 = "This is Lower caps"
# str2 = "this is lower caps"

# print(str1.islower())
# print(str2.islower()) 

# str1 = "This Is What We Do"
# str2 = "This is What we do"

# print(str1.istitle())
# print(str2.istitle()) 

# str1 = "This is All Caps"
# str2 = "THIS IS ALL CAPS"

# print(str1.isupper())
# print(str2.isupper()) 


# str1 = "Alpha Beta Delta"
# str2 = "Alpha Beta Delta Epsilon"

# print(str1.endswith("lta"))
# print(str2.endswith("lta")) 

# str1 = "Alpha Beta Delta"
# str2 = "Alpha Beta Delta Epsilon"

# print(str1.endswith("lta"))
# print(str2.endswith("lta")) 

# print(str1.startswith("Al"))
# print(str2.startswith("Ae"))



#-------- JOINING STRINGS --------------
# s = "Mary Queen Casaclang"

# print(" ".join(s))

# #Join a List
# names = ["Paul", "Jordan", "Marcus"]
# names2 = ", ".join(names)
# print(", ".join(names))


#------- SPLITTING STRINGS-----------
#TURN INTO A LIST

# names = "Paul Jordan Marcus"
# print(names.split(" ")) #split using a delimiter space

# names1 = "Paul,Jordan,Marcus"
# print(names1.split(","))



#------- FINDING STRINGS-----------
#returns an index
#-1 if not present
# names = "Paul,Jordan,Marcus"
# names = "Paul,Jordan,Marcus"

# print(names.find("Jordan"))
# print(names.find("Michael"))



#------- REPLACING STRINGS-----------
# names = "Paul,Jordan,Marcus"

# print(names.replace(","," ")) #replace first argument into second argument



#------- REMOVING SPACES-----------
# names = " hello "

# print("["+names.lstrip()+"]") #remove leading spaces

# print("["+names.rstrip()+"]") #remove ending spaces



#------- STRING ORDINAL-----------
# char_1 = 'a'
# char_2 = ' '  # space

# print(ord(char_1))
# print(ord(char_2))

# #string chr if code point giver
# print(chr(97))
# print(chr(945))




#------- STRING INDEX METHOD-----------
# print("aAbByYzZaA".index("b")) #error if none
# print("aAbByYzZaA".index("Z"))
# print("aAbByYzZaA".index("A"))


#-------STRING IN LOOPS----------------
# a = "STRING"
# i = 0
# # while i < len(a):
# #      c = a[i]
# #      print(c)
# #      i = i + 1

# # for i in range(0, len(a)):
# #      print(a[i], end=" ")
     
# a = "STRING"
# for i in a:
#      print(i)



#-------LISTS----------------
# info = ['cellphone', 23, 8.5, 'name']
# print(info[1])

# #access list
# hairs = ('violet', 'red', 'black', 'brown', 'blond', 'red', 'black')
# print(hairs[-1])

# #start-stop
# print(hairs[1:6])
# print(hairs[-6:-1])
# print(hairs[3:])
# print(hairs[:3])

# print(hairs[::2]) #STEP / SKIP

# #REVERSE A TUPLE
# print(hairs[::-1])


# #-------------DICTIONARIS----------------

# #--Accessing Dictionary Elements--
# info = {
#     "name" : "Paul",
#     "age" : 28,
#     "course" : "DIT"
# }
# print(info["name"])
# print(info.get("course"))

# #----change value of element----
# info = {
#     "name" : "Paul",
#     "age" : 28,
#     "course" : "DIT"
# }

# info["name"] = "Aaron"
# print(info["name"])

# #----add new elements----------
# info = {
#     "name" : "Paul",
#     "age" : 28,
#     "course" : "DIT"
# # info["status"] = "dissertation writing"
# print(info)



#-------------- SETS ------------------------

# hairs = {'violet', 'red', 'black', 'brown', 'blond', 'red', 'black'}
# print(hairs)

# for hair in hairs:
#     print(hair)


# var = input()
# var = var.split()

# for i in range(0, len(var)):
#     reverse = var[i]
#     var[i] = reverse[::-1]

# print(" ".join(var))

word = "listen"
word2 = "silent"
# flag = True
# for i in word:
#     if i not in word2:
#         flag = False
#         break

# if flag == True:
#     print("anagram")



# #--Accessing Dictionary Elements--
# info = {
#     "name" : "Paul",
#     "age" : 28,
#     "course" : "DIT"
# }

# for x in info.keys():
#     print(x)



#Most Occurence

# var = "ljwherkjnmssdfkljtowuoijdksl"
# result= {}

# for c in var:
#     result[c] = 0
#     for l in var:
#         if c == l:
#             result.update({c: result[c]+1})

# print(result)


# var = {
#     "name":"jeays"
#     } 

# var["age"] = 20
# var.setdefault


# print(var)


# from collections import deque
# dq = deque('aeiou')
# for element in dq:
#    print(element)


# from collections import deque
# dq = deque('aeiou')
# for element in dq:
#    print(element)


#------ REVERSE----------

# Python code
# To reverse words in a given string
 
# input string
# string = "geeks quiz practice code"
# # reversing words in a given string
# s = string.split()[::-1]
# l = []
# for i in s:
#     # appending reversed words to l
#     l.append(i)
# # printing reverse words
# print(" ".join(l))


# # Input two texts from the user
# text1 = input("Enter the first text: ")
# text2 = input("Enter the second text: ")

# # Remove spaces and convert to lowercase
# text1 = text1.replace(" ", "").lower()
# text2 = text2.replace(" ", "").lower()

# # Sort the characters in each text
# sorted_text1 = sorted(text1)
# sorted_text2 = sorted(text2)

# # Check if the sorted texts are the same
# if sorted_text1 == sorted_text2:
#     print("The texts are anagrams.")
# else:
#     print("The texts are not anagrams.")

# string1= input("Enter first string: ")
# string2= input("Enter second string: ")

# string1 = string1.replace(" ", "").lower()
# string2 = string2.replace(" ", "").lower()

# new_string1 = sorted(string1)
# sorted_string2 = sorted(string2)


# if sorted_text1 == sorted_text2:
#      print("The texts are anagrams.")

     

# print(string1)
# print(string2)

# anagrams = lambda input1, input2: sorted(input1.lower().replace(" ", "")) == sorted(input2.lower().replace(" ", ""))
# print("Anagrams" if anagrams(input("Enter first string: "), input("Enter second string: ")) else "Not anagrams")

# print (True if (sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))) else False)


# # Input a string from the user
# input_string = input("Enter string: ")

# # Remove spaces and other non-alphabetical characters
# filtered_string = ''.join(char for char in input_string if char.isalpha())

# # Print the original string
# print(filtered_string)

# # Print the box pattern
# [print(filtered_string[i] + ' ' * (len(filtered_string) - 2) + filtered_string[-(i + 1)]) for i in range(1, len(filtered_string) - 1)]

# # Print the reversed original string
# print(filtered_string[::-1])


# text= input("Enter a string: ")a

# skipping spaces and common special characters and ignoring  th case of the letter arranged in alphabetical order. lastry, display inputted string in an inverted triangle
# skipping spaces and other common speacial characters.

# Sample output: 

# Enter a string: Queen

# No. of Uppercase Characters: 1
# No. of Uppercase Characters: 4

# q: 1
# u: 1
# e: 2
# n: 1

#  neeuQueen
#   neeueen
#    neeen
#     nen 
#      n


#-------------- FUNCTION ACTIVITY --------------------------
# def list_factors(num):
#     factors = list(filter(lambda x: num % x==0, range(1, num)))
#     return factors

# i = int(input("HM? "))
# print(list_factors(i))


#----------- ARGS------------

# def subjectsEnrolled(name,*subjects):
#     print(f"Name: {name}")
#     i = 1
#     for subject in subjects:
#         print(f"Subject {i}: {subject}")
#         i+=1

# # highlighted in yellow are the *args
# # highlighted in blue is a normal parameter
# subjectsEnrolled(
#     input("Enter Name: "),
#     input("Subject 1: "),
#     input("Subject 2: "),
#     input("Subject 3: "),
# )



#----- NORMAL PARAMETERS AND KWARGS----------------
def computeAverage(name,**grades):
    sum = 0
    for v in grades.values():
        sum += v
    print(f"\n{name}'s grades ({', '.join([f'{k}={v}' for k,v in grades.items()])}) and the average is {sum/len(grades):.2f}")

# highlighted in green are the **kwargs
# highlighted in blue is a normal parameter
# computeAverage(
#     input("Enter name: "),
#     Math=int(input("Math grade: ")),
#     Science=int(input("Science grade: ")),
#     English=int(input("English grade: ")),
#     Music=int(input("Music grade: ")),
#     Arts=int(input("Arts grade: ")),
# )

#----------Using *args and **kwargs---------------------
# def subjectsEnrolled(*subjects,**descriptions):
#     print(f"\nName: {descriptions['name']}")
#     i = 1
#     for subject in subjects:
#         print(f"Subject {i}: {subject}")
#         i+=1
#     for k,v in descriptions.items():
#         print(f"{k} => {v}")

# # highlighted in yellow are *args
# # highlighted in green are *kwargs
# subjectsEnrolled(
#     input("Subject 1: "),
#     input("Subject 2: "),
#     input("Subject 3: "),
#     name=input("Enter Name: "),
#     IT401=input("Enter Description for IT 401: "),
#     IT402=input("Enter Description for IT 402: "),
#     IT403=input("Enter Description for IT 403: "),
# )

# def list_positives():
#     numbers = []  
    
#     while True: 
#         num = int(input("Enter a positive number: "))
        
#         if num == 0:
#             break  
        
#         if num > 0:
#             numbers.append(num)  
    
#     return numbers


# numbers = list_positives()
# print(numbers)

#-----------------------------------
# def list_positives():
  
#     numbers = []  # Initialize an empty list to store positive numbers
    
#     while True:  # Continue the loop until the user enters 0
#         num = int(input("Enter a positive number: "))
        
#         if num == 0:
#             break  # Exit the loop if the input is 0
        
#         if num > 0:
#             numbers += [num]  # Add the positive number to the list
    
#     return numbers

# # Example usage:
# numbers = list_positives()
# print(numbers)

#----------------------------san---------------------------

# def list_positives():
 
#     numbers = []  # Initialize an empty list to store positive numbers
    
#     while True:  
#         num = int(input("Enter a positive number: "))
        
#         if num == 0:
#             break  
        
#         if num > 0:
#             numbers.append(num) 
    
#     return numbers

# def list_indexes(values, target):
   
#     locations = []  

#     for index, value in enumerate(values):
#         if value == target:
#             locations.append(index)  
    
#     return locations

# # Example usage:
# values = list_positives()  
# target = int(input("Enter the target number: "))  
# indexes = list_indexes(values, target) 
# print(indexes)


#--------------yon --------------------------
# def list_positives():
#     """
#     Gets a list of positive numbers from a user. Negative numbers are ignored. Enter 0 to stop entries.

#     Returns:
#     numbers (list): A list of positive integers (list of int)
#     """
#     numbers = []  # Initialize an empty list to store positive numbers
    
#     while True:  # Continue the loop until the user enters 0
#         num = int(input("Enter a positive number: "))
        
#         if num == 0:
#             break  # Exit the loop if the input is 0
        
#         if num > 0:
#             numbers.append(num)  # Add the positive number to the list
    
#     return numbers

# def subtract_lists(minuend, subtrahend):
#     """
#     Updates the list minuend removing from it the values in subtrahend.

#     Parameters:
#     minuend (list): List of values (list of int) to be updated.
#     subtrahend (list): List of values (list of int) to remove from minuend.

#     Returns:
#     None
#     """
#     for value in subtrahend:
#         if value in minuend:
#             minuend.remove(value)

# # Example usage:
# print("Values for Minuend:")
# minuend = list_positives()  # Get a list of positive numbers for minuend
# print("Values for Subtrahend:")
# subtrahend = list_positives()  # Get a list of positive numbers for subtrahend

# subtract_lists(minuend, subtrahend)  # Update minuend by removing values from subtrahend

# print("Updated Minuend:", minuend)


#-----------------------jyuu-------------------------
# def color_frequencies(*colors):
#     frequencies = {}
    
#     for color in colors:
#         if color in frequencies:
#             frequencies[color] += 1
#         else:
#             frequencies[color] = 1
    
#     return frequencies

# # Example usage:
# colors = ('red', 'green', 'blue', 'red', 'blue')
# color_frequencies_dict = color_frequencies(*colors)
# print(color_frequencies_dict)

#COLORjyuu---------------------------------------------------------

# def color_frequencies(*colors):
#     frequencies = {}
#     for color in colors:
#         if color in frequencies:
#             frequencies[color] += 1
#         else:
#             frequencies[color] = 1
#     return frequencies

# #INPUT VERSION
# colors = []
# while True:
#     try:
#         color = input("Enter a color (or 'stop' to finish): ").strip().lower()
#         if color == "stop":
#             break
#         elif color.isalpha():
#             colors.append(color)
#         else:
#             raise ValueError("Invalid input. Please enter a valid color name.")
#     except ValueError as e:
#         print(e)

# #PRE DEFINED VERSION
# #colors = ("red", "green", "blue", "red", "blue")

# result = color_frequencies(*colors)
# print(result)


#flat---------------------------------------------
# def flatten(matrix):
#     flat = [elem for row in matrix for elem in row]
#     return flat

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# flat = flatten(matrix)
# print(flat)

#ADDRESS--------------------------------------------
# def get_address(st):
#     try:
#         words = st.split()
        
#         # Check for the right length
#         if len(words) < 6:
#             raise ValueError("Input has too few words")
#         elif len(words) > 6:
#             raise ValueError("Input has too many words")

#         name = ' '.join(words[:2])
#         street = ' '.join(words[2:4])
#         city = ' '.join(words[4:6])
#         postal_code = ' '.join(words[-2:])

#         return (name, street, city, postal_code)
    
#     except ValueError as e:
#         return str(e)
    
# st = input("Enter the address: ")
# address = get_address(st)
# print(address)


# # David Brown King St Waterloo, ON Q1Q 1Q1

# # Duran Duran Rock Ave Kitchener, ON ROK ON3


#FACTORS-----------------
# def list_factors(num):
#     factors = list(filter(lambda x: num % x == 0, range(1, num)))
#     return factors

# num = int(input())

# factors = list_factors(num)

# print(factors)

#LIST INDEXES-----------------
# def list_indexes(values, target):
#     indexes = []
#     index = 0
#     for value in values:
#         if value == target:
#             indexes.append(index)
#         index += 1
#     return indexes

# def list_positives():
#     numbers = []
#     while True:
#         num = int(input("Enter a positive number: "))
#         if num > 0:
#             numbers.append(num)
#         elif num == 0:
#              break
#     return numbers

# values = list_positives()

# print(values)

# indexes = list_indexes(values, int(input("Enter the target number: "))) 

# print(indexes)

#LIST POSITIVES----------------------
# def list_positives():
#     numbers = []
#     while True:
#         num = int(input("Enter a positive number: "))
#         if num > 0:
#             numbers.append(num)
#         elif num == 0:
#              break
#     return numbers

# positive_numbers = list_positives()

# print(positive_numbers)


#MATRIX ROTATE RIGHT------------------
# def matrix_rotate_right(matrix):
#     if not matrix:
#         return []

#     nRows, nCols = len(matrix), len(matrix[0])
#     rotated = []

#     for j in range(nCols):
#         rotatedRow = []
#         for i in range(nRows - 1, -1, -1):
#             rotatedRow.append(matrix[i][j])
#         rotated.append(rotatedRow)

#     return rotated

# #I added this hehe
# def matrix_rotate_left(matrix):
#     if not matrix:
#         return []

#     nRows, nCols = len(matrix), len(matrix[0])
#     rotated = []

#     for j in range(nCols - 1, -1, -1):
#         rotatedRow = []
#         for i in range(nRows):
#             rotatedRow.append(matrix[i][j])
#         rotated.append(rotatedRow)

#     return rotated

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rotated = matrix_rotate_right(matrix)
# for row in rotated:
#     print(row)

#STR INTEGERS----------------------------
# def str_integers(st):
#     numbers = []

#     splitStr = st.split(',')

#     for token in splitStr:
#         try:
#             num = int(token)
#             if num > 0:
#                 numbers.append(num)
#         except ValueError:
#             pass

#     return numbers

# st = input()
# numbers = str_integers(st)
# print(numbers)

#STR_STATS------------------------------
# def str_stats(st):
#     ucount = 0 
#     lcount = 0
#     dcount = 0
#     wcount = 0

#     for char in st:
#         if char.isupper():
#             ucount += 1
#         elif char.islower():
#             lcount += 1
#         elif char.isdigit():
#             dcount += 1
#         elif char.isspace():
#             wcount += 1

#     return ucount, lcount, dcount, wcount

# st = input()
# ucount, lcount, dcount, wcount = str_stats(st)

# print("Uppercase:", ucount)
# print("Lowercase:", lcount)
# print("Digits:", dcount)
# print("Whitespace:", wcount)

#SUBTRACT_LIST------------------------------------
# def subtract_lists(minuend, subtrahend):
#     for value in subtrahend:
#         if value in minuend:
#             minuend.remove(value)

# def list_positives():
#     numbers = []
#     while True:
#         num = int(input("Enter a positive number: "))
#         if num > 0:
#             numbers.append(num)
#         elif num == 0:
#              break
#     return numbers

# print("Values for Minuend")
# minuend = list_positives()
# print("Values for Subtrahend")
# subtrahend = list_positives()

# subtract_lists(minuend, subtrahend)

# print(minuend)








