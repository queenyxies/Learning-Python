# firstNum = int(input("Enter first num: "))
# secondNum = int(input("Enter second num: "))

# try:
#     print(firstNum / secondNum)
# except:
#     print("Cannot be done")
# print("THE END")

# def bad_function(n):
#     raise ZeroDivisionError

# try:
#     bad_function(0)
# except ArithmeticError:
#     print("Error!?")
# print("THE END")

# def bad_function(n):
#     try:
#         return n/0
#     except:
#         print("I did it again")
#         raise

# try:
#     bad_function(0)
# except ArithmeticError:
#     print("I see!")
# print("THE END")


#-------------------------INDEX ERROR-------------------------------
# the_list = [1, 2, 3, 4, 5]
# ix = 0
# do_it = True

# while do_it:
#     try:
#         print(the_list[ix])
#         ix+= 1
#     except IndexError:
#         do_it = False
# print('Done')