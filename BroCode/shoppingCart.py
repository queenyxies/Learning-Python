foods = []
prices = []
total = 0
while True:
    food = input("Enter food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = int(input(f"Enter price of {food} (q to quit): P "))
        prices.append(price)
        total += price

print("========== SHOPPING CART =============")
for food in foods:
    print(food, end="  ")

for price in prices:
    print(price)

print(f"The total price is: {total}")