def reverseString(str):
    return str[::-1]
print(reverseString("queen"))

def isPalindrome(str):
    return "Is palindrome" if str == str[::-1] else "Not a palindorme"

print(isPalindrome("racecar"))