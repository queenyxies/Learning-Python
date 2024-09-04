num_pad = (("1", "2", "3"), 
           ("4", "5", "6"),
           ("7", "8", "9"),
           ("*", "0", "#"))
for number in num_pad:
    for char in number:
        print(char, end=" ")
    print("")