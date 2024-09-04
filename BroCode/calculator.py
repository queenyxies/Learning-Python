operator = input("What operator do you want to use? ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0

if operator == "+":
    result = num1 + num2 
elif operator == "-":
    result = num1 - num2
    
print(result)