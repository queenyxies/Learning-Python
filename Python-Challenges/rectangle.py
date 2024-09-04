row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
symbol = input("Enter your desired symbol: ")

for i in range(1, row + 1):
    for j in range(1, column + 1):
        print(symbol, end="")
    print("")