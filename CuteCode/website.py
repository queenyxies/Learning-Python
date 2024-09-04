# How can you replace string space with a given character in Python?

# Create a function with 2 arguments (str, char)
# 1. Inside the function, use replace str("", char)
# 2. Inside the function access the string using for in loop
#    If certain i == " ":  i = char 

def replace_space(str, char):
    return str.replace(" ", char)

print(replace_space("the quick brown fox", "-"))

def replace_space2(str, char):
    result = ''
    for i in str:
        if i == " ":
            i = char
        result += i
    return result


print(replace_space2("the quick brown fox", "-"))

def valid_square(num):
    square = int(num**0.5)
    check = square**2==num
    return check

print(valid_square(10))
print(valid_square(36))


def get_factorial(int):
    result = 1
    for number in range(1, int + 1):
        result *= number
    return result

print(get_factorial(7))
