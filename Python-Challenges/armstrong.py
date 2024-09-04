def isArmstrong(number):
    num_string = str(number)
    num_length = len(num_string)
    armstrong_num = sum(pow(int(i), num_length) for i in num_string)
    return armstrong_num == number
    

print(isArmstrong(153))