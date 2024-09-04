#1 Counting Sweet Cookies 🍪
def getSweetCookies(arr):
    sweet_cookies = 0
    for i in arr:
        if i > 5:
            sweet_cookies += 1
    return sweet_cookies

print(getSweetCookies([1, 3, 8, 10, 6, 2]))

#2 Reverse the Bunny's Path 🐰
def reversedStep(arr):
    return arr[::-1]

print(reversedStep([3, 5, 8, 2]))

#3 Find the Smallest Bunny 🌸
def smallestBunny(arr):
    arr.sort()
    return arr[0]
    # return min(arr)

print(smallestBunny([4, 7, 1, 9, 3]))

#4. Bunny's Favorite Numbers 💖
def count_favorite_number(arr):
    count = 0
    for number in arr:
        if number == 4:
            count += 1
    return count

print(count_favorite_number([1, 4, 7, 4, 4, 9]))

#5. Bunny's Flower Collection 🌷
def count_flower(arr):
    return sum(arr)

def count_flower2(arr):
    flowers = 0
    for flower in arr:
        flowers += flower
    return flowers

print("Sum of flowers: ", count_flower([3, 7, 2, 5]))
print("Sum of flowers (V2): ", count_flower2([3, 7, 2, 5]))

#6. 6. Bunny's Carrot Stack 🥕

def tallest_stack(arr):
    return max(arr)

def tallest_stack2(arr):
    arr.sort()
    return arr[-1]

print("Tallest Stack: ", tallest_stack([10, 5, 12, 7]))
print("Tallest Stack: ", tallest_stack2([10, 5, 12, 7]))

# 7. Bunny's Hop Sequence 🌼
def includesNumber(arr, num):
    for i in arr:
        if i == num:
            return i

def includesNumber2(arr, num):
    return num in arr
    
print("Hope Sequence: ", includesNumber([3, 7, 1, 9, 5], 7))
print("Hope Sequence V2: ", includesNumber2([3, 7, 1, 9, 5], 7))

# 8.  Bunny's Carrot Feast 🐇🥕
def even_sized_carrots(arr):
    return [i for i in arr if i  % 2 == 0]

print(even_sized_carrots([2, 5, 8, 11, 4]))

#9. Bunny's Carrot Divider 🥕🔢
def can_divide_equally(carrots: int, bunnies: int):
    return carrots % bunnies == 0

print("Divide qually? ", can_divide_equally(12, 3))

#10. Bunny's Carrot Pairs (Even Numbers in List) 🥕🥕
def get_carrot_pairs(arr):
    counter = 0
    for i in arr:
        if i % 2 == 0:
            counter += 1
    return counter

print("Number of Even numbers: ", get_carrot_pairs( [2, 5, 6, 8, 10]))
