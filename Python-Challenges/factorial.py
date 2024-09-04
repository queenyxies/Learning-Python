# FACTORIAL
# 4 = 4 * 3 * 2 * 1
def getFactorial(num):
    factorial = 1
    for number in range(1, num + 1):
        factorial *= number
    return factorial

print(getFactorial(7))