def is_palindrome(number):
    # Convert number to string to check for palindrome
    s = str(number)
    return s == s[::-1]

def reverse_number(number):
    # Convert number to string, reverse it, and convert back to int
    return int(str(number)[::-1])

def reverse_and_add(number):
    iterations = 0
    while not is_palindrome(number):
        reversed_number = reverse_number(number)
        number += reversed_number
        iterations += 1
    return iterations, number

# Example usage
number = 195
iterations, palindrome = reverse_and_add(number)
print(f"{iterations} {palindrome}")
