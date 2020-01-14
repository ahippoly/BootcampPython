import random


print("This is an interactive guessing game!\n"
+ "You have to enter a number between 1 and 99 to find out the secret number.\n"
+ "Type 'exit' to end the game.\n"
+ "Good luck!")

num = random.randint(1,99)
guess = 0
count = 0
quit = 0
while guess != num :
    print("What's your guess between 1 and 99?")
    count += 1
    guess = input()
    if guess.isnumeric() == True :
        guess = int(guess)
        if guess == 42 :
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if guess > num :
            print("Too high!")
        elif guess < num :
            print("Too low!")
    elif guess == "exit" :
        quit = 1
        print("Goodbye!")
        break
    else :
        print ("That's not a number.")
if quit == 0 :
    if count == 1 :
        print("Congratulations! You got it on your first try!")
    else :
        print("Congratulations, you've got it!")
        print("You won in " + str(count) + " attempts!")
