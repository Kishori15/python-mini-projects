import random

low=0
high=100

answer=random.randint(low,high)
print(f"Enter a number between {low} and {high}")
guesses=0
is_running=True

while is_running:
    guess=input("Enter the number: ")
    
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess>high or guess<low:
            print(f"Please enter a number between {low} and {high}")
        elif guess>answer:
            print("The guess is too high")
        elif guess<answer:
            print("The guess is too low")
        else:
            print("Correct!")
            print(f"Total guesses: {guesses}")
            is_running=False
    else:
        print("The guess should be a number.")
        

        
