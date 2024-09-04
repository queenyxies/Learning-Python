def getEven(arr):
    evenNumbers = [number for number in arr if number % 2 == 0 ]
    return evenNumbers
print(getEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))