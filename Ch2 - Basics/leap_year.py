


#temp= float(input("Enter the temperature: "))
#formula = str(input("Enter the action: "))

#if formula == "F":
###celsius= temp * (9/8) + 32
#    round= celsius ** 2
#    print(celsius)
#elif formula == "C":
#    faren= temp - 32 + (5/9)
#    round= faren ** 2
#    print: round
#else:
#    print("Invalid Formula")

#len = int(input("Enter length: "))
#sum= 0
#for i in range(0, len, 2):
#    sum += i

#print(sum)

#num= int(input("Enter a number: "))
#print("Multiplication Table of ", num)
#for i in range(1, 11):
#   product= i * num
#    print(num, " x " ,i, " = ", product)

#print("Multiplication Table")

#for i in range (1, 11):
#    for x in range (1, 11):
#        product= x * i
#        print(i, "x" , x, "=", product, end=",")
#    print()

#x = 10 
#if x == 10:
#   print(x == 10) 
#if x > 5:
#   print(x > 5) 
#if x < 10:
#    print(x < 10) 
#else:
#    print("else")


#x = 1 
#y = 1.0 
#z = "1" 
#if x == y:
#   print("one") 
#if y == int(z): 
#   print("two") 
#elif x == y: 
#   print("three") 
#else: 
#   print("four") 

#for i in range(1,5):
#    print(i * str(i),end="")

num = 100

while num >= 0:
   if num%2 == 0:
      num -= 8
   elif num %2 !=0:
      num -= 5
      print("Yo", end=",")
   if num < 80 and num > 20:
      continue
   elif num > 0 and num < 8:
      break
   num -= 1


