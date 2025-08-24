from random import choice
from verbsContainer import verbs

def Game():
    points = 0
    while True:
        chosenVerb = choice(list(verbs.keys()))
        userInput = input(f"What's the past simple of {chosenVerb}?: \n------------------------------------------ \n ->").lower().strip()

        #I use != instead of == to check wrong answers first
        if userInput != verbs[chosenVerb]:
            print(f" ❌ Opps, the correct answer is: {verbs[chosenVerb]}") 
            points -= 1
        else: 
            print("Correct! ☑️") #using emojis is not necessary, but it makes the game more fun
            points += 1

        if points < 0:
            points = 0 #this avoids negative points

        print(f"current points: {points}")

        if input("\n Do you want to continue? y/n: \n ->").lower().strip() != "y":
            break
    print(f"Your final score is: {points} points. Thanks for playing! 👋")
Game()