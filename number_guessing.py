import random
print("welcome to NUMBER GUESSING ")
n=int(input("enter the max range: "))
random_guess=random.randint(1,n)
guesses=0
while True:
    guesses+=1
    user_guess=int(input("guess the number: "))
    if user_guess==random_guess:
        print("you won")
        print("you have guessed the number in {0}th time".format(guesses))
        break
    elif user_guess > random_guess:
        print("you are above the random_guess so please enter less one")
    else:
        print("you are below the random_guess so please enter high one")
        continue

