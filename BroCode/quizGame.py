questions = (("Which of the following is Paris favorite word? "),
             ("What is the name of Paris's daughter? "),
             ("What is Paris's birth year? "))

options = (("A. sleep", "B. eat", "C. out"),
           ("A. Barats", "B. Popol", "C. Kupa"),
           ("A. 2016", "B. 2015", "C. 204"))
answers = ("B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    for option in options:
        print(question)
        for letter in option:
            print(letter)