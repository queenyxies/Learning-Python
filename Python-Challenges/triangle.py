# LEFT TRIANGLE

# number = int(input("How many number? "))

# for i in range(1, number + 1):
#     print("*" * i)

# RIGHT TRIANGLE

def makeLeftTriangle(rows):
    for row in range(1, rows + 1):
        print(" " * (rows - row) + "*" * row)
    

makeLeftTriangle(10)






# NORMAL TRIANGLE
# def makeBormalTriangle(num):
#     for i in range(1, num + 1):
#         print(" " * (num-i), end="")

#         print("*" * (2 * i - 1))
# makeBormalTriangle(5)

# DIAMOND
def makeDiamond(num):
    # Top half of the diamond (including the middle)
    for i in range(1, num + 1):
        # Print leading spaces
        print(" " * (num - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

    # Bottom half of the diamond (excluding the middle)
    for i in range(num - 1, 0, -1):
        # Print leading spaces
        print(" " * (num - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Example usage:
makeDiamond(5)




# PYRAMID
# make for in loop from 1 to number of desired rows
# print space first === number of row - i (increment)
# add end="" to continue
# print asterisk then then((2 * i -1))
def makePyramid(row):
    for i in range(1, row + 1):
        print(" " * (row - i), end="")
        print("*" * (2 * i -1))

makePyramid(10)

    

    