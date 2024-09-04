collect_carrots = int(input("How many carrots should the bunny collect? "))
carrots = 0
for i in range(1, collect_carrots + 1):
    if i % 3 == 0 or i % 5 == 0:
        carrots += 1

print(carrots)
