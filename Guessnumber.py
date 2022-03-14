from random import randint

def Guess_number():
    i = randint(0,5)
    attempts= 5

    while attempts != 0:
        question = int(input(f"Guess a number between 1 and 5: "))
        attempts -= 1

        if question == i:
            print ("Correct! You win! Try again!")
            attempts = 5
            break
             
        elif question == None:
            print("You didn't enter a number. Try one!") 
            attempts += 1

        elif attempts == 0:
            print(f"You lost... The number was { i } btw. Thank you for playing!")
            break

        elif question > 5 or question < 0 :
            print("Out of range!")   
            attempts += 1

        else:
            print(f"Wrong... You have {attempts} more attempts so guess again")

    
Guess_number()

replay = input("Try again? y/n ")

while replay == "y":
    Guess_number()
    replay = input("Try again? y/n ")

print("Ok, Bye! And thanks for playing!")




