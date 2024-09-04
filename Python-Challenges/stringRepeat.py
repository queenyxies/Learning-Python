# 1. Make a new variable for the new string
# 2. Access the string (for in loop) .
# 3. *2 every char of the string
# 4. Store it to the new or empty variable the return*+
def stringRepeat(str):
    new_string = ""
    for char in str:
        new_string += char * 2
    return new_string
print(stringRepeat("talaga?"))