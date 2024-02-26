#How to find average of N numbers in Python?

num = int(input("How many numbers? "))
sum = 0

for n in range (num):
    addend = int(input("Enter number: "))
    sum += addend

average = sum // num

print("The average is ", average)