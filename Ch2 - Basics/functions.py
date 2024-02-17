
#------------------FUNCTIONS-----------------------

# hi()
# def hi():
#     print("hi")

#An exception is thrown (the NameError exception to be more precise)

# def hi():
#     print("hi")
# hi(5)

#exception will be thrown (the TypeError exception to be more precise) - the hi() function doesn't take any arguments

# def adding(a, b, c):
#      print(a, "+", b, "+", c, "=", a + b + c)

# adding(1,2,3)


# def hi_all(name_1, name_2):
#      print("Hi,", name_2)
#      print("Hi,", name_1)

# hi_all("Shun", "Kei-Zyh")

# def intro(a="James Bond", b="Bond"):
#      print("My name is", b + ".", a + ".") 
# intro(b="Sean Connery")

# def intro(a, b="Bond"):
#     print("My name is", b + ".", a + ".") 
# intro("Susan")

# def intro(a="James Bond", b="Bond"):
#     print("My name is", b + ".", a + ".") 
# intro()


# def minus():
#     return 10-5
# print(minus())


# -----POSITIONAL ARGUMENTS------------------
# def multiply(x, y):
#     return x * y
# print(multiply(5, 5))


# -----KEYWORD ARGUMENTS-----------------
# def subt(x=10, y=5):
#     return x-y
# print(subt(x=9, y=1))

# -----MIXED TYPE ARGUMENTS-----------------
# def add(a, b=10, c=2):
#     return a + b + c
# print((add(a="5", c="1", b="2"))) #HINDI MAGERROR BASTA MAY KEYWORD
#  DAT MAUUNA LAGI SI POSITIONAL ARGUMENT! ERROR OTHERWISE

# -----*ARGS-----------------
# def add(*nums):
#     sum=0
#     for ar in nums:
#         sum+=ar
#     return sum
# print(add(2,3,4,5,6,7,6,8))

# def add(*names):
#     for ar in names:
#         print(ar)
# add("queen", "tifa", "dolphon")

# -----*KWARGS-----------------
# def info(**data):
#     return f"Hello {data['fname']} {data['lname']}!"
# print(info(fname="Benj", lname="Fox"))
# print(info(fname="Quek", lname="Quek"))



# -----Using a normal parameter and *args-----------------
# def subjects(name, *subjects):
#     print(f"Name: {name}")
#     i=1
#     for subject in subjects:
#         print(f"Subject {i}: {subject}")
#         i+=1

# subjects(
#     input("Enter Name: "),
#     input("Subject 1: "),
#     input("Subject 2: "),
#     input("Subject 3 :"),
# )



# def getGrades(*grades, name):
#     print(f"Name: {name}")
#     i = 1
#     for grade in grades:
#         print(f"Grade {i}: {grade}")
#         i+=1
# getGrades(
#     input("Enter Grade 1: "),
#     input("Enter Grade 2: "),
#     input("Enter Grade 3: "),
#     input("Enter Grade 4: "),
#     name = input("Enter Name: "),
# )




# -----Using a normal parameter and **kwargs-----------------
# def computeAverage(name,**grades):
#     sum = 0
#     for v in grades.values(): #values of the dict
#         sum += v #nside the loop, each grade (value) is added to the sum variable to calculate the total sum of grades.
#     print(f"\n{name}'s grades ({', '.join([f'{k}={v}' for k,v in grades.items()])}) and the average is {sum/len(grades):.2f}")
#     #creates a string that lists all the grade-key pairs in the grades dictionary in the format "key=value." 


# computeAverage(
#     input("Enter name: "),
#     Math=int(input("Math grade: ")),
#     Science=int(input("Science grade: ")),
#     English=int(input("English grade: ")),
#     Music=int(input("Music grade: ")),
#     Arts=int(input("Arts grade: ")),
# )


# def computeAverage(**grades,name):
#     sum = 0
#     for v in grades.values():
#         sum += v
#     print(f"\n{name}'s grades ({', '.join([f'{k}={v}' for k,v in grades.items()])}) and the average is {sum/len(grades):.2f}")

# # highlighted in green are the **kwargs
# computeAverage(
#     Math=int(input("Math grade: ")),
#     Science=int(input("Science grade: ")),
#     English=int(input("English grade: ")),
#     Music=int(input("Music grade: ")),
#     Arts=int(input("Arts grade: ")),
#     name=input("Enter name: "),
# )




# -----Using *args and **kwargs-----------------
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


# def subjectsEnrolled(name,*subjects,**descriptions):
#     print(f"\nName: {name}")
#     i = 1
#     for subject in subjects:
#         print(f"Subject {i}: {subject}")
#         i+=1
#     for k,v in descriptions.items():
#         print(f"{k} => {v}")

# # highlighted in yellow are *args
# # highlighted in green are *kwargs
# # highlighted in blue is a normal parameter
# subjectsEnrolled(
#     input("Enter Name: "),
#     input("Subject 1: "),
#     input("Subject 2: "),
#     input("Subject 3: "),
#     IT401=input("Enter Description for IT 401: "),
#     IT402=input("Enter Description for IT 402: "),
#     IT403=input("Enter Description for IT 403: "),
# )





# -----LAMBDA FUNCTION-----------------
#lambda param_list : expression

# add = lambda x,y : x+y
# print(add(10,9))



# -----MAP() FUNCTIOM-----------------
# a = map(lambda s: s.lower() if s in 'aeiou' else s.upper(), "shunate")

# print(tuple(a)) #need convert to tuple, list, iterable kasi value ni map ay object

# numbers = [1,2,3,4,5]
# squared = map(lambda num: num**2, numbers)

# print(list(squared))


# -----FILTER() FUNCTIOM----------------- 

nums = [2, 4, 6, 9, 10]
even = filter(lambda n: n%2==0, nums)

print(list(even))