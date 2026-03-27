questions=("What is the output of print(2 + 3 * 4) in Python?","Which data type is used to store True or False values in Python?", "What does SQL stand for?", "Which keyword is used to define a function in Python?", "Which of the following is a loop in Python?")

options=(("A) 20 ", "B) 14" , "C) 24" , "D) 10"), ("A) int" , "B) str" , "C) bool", "D) float"),("A) Structured Question Language" , "B) Simple Query Language" , "C) Structured Query Language" , "D) Standard Query Logic"),("A) function" , "B) def" , "C) fun" , "D) define"),("A) if" , "B) else" , "C) for" , "D) define"))
answers=("B","C","C","B","C")
guesses=[]
score=0
ques_num=0

for question in questions:
    print(question)
    for option in options[ques_num]:
        print(option)
    guess=input("Enter the option: ").upper()
    guesses.append(guess)
    if(answers[ques_num]== guesses[ques_num]):
        print("Correct")
        score+=1
    else:
        print("Incorrect")
        print(f"{answers[ques_num]} is correct answer")
    ques_num+=1
    print("-------------------------------------------------------")
print(f"Score: {score}")
