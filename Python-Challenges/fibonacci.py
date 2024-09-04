#LOOP depending on the desired fibonacci term
#Store 2 variable old and new sum
# F(0) = 0
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))  # Output will be 5

# def getFibonacci(term):
#     prevsum = 0
#     newSum = 1
#     sum = 0
#     for number in range(0, term + 1 ):
#         sum = prevsum + newSum

#     return sum
# print(getFibonacci(5))


def getFibonacci(term):
    fibo_seq = [0, 1]

    while len(fibo_seq) < term:
        next_term = fibo_seq[-2] + fibo_seq[-1]
        fibo_seq.append(next_term)
    return fibo_seq

print(getFibonacci(10))