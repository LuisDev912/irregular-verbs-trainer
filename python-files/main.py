from random import choice
from verbsContainer import verbs

class Game:
    def intro(_):
        print("Welcome to the Past Simple Verb Game! 🎉\n" 
            "the instructions are simple:" 
            "the game will give you a verb in its base form, and you have to type its past simple form.\n" 
            "For each correct answer, you earn a point. For each wrong answer, you lose a point.\n" 
            "For example, if the verb is 'go', you should type 'went'.\n" 
            "You can quit the game anytime by typing 'n' when asked if you want to continue.\n" 
            "Let's see how good is your knowledgement! Good luck! 🍀\n" 
            )
        if input("Do you want to start the game? y/n: \n ->").lower().strip() == "y":
            Game.mainGame(_)
            
    def mainGame(_): #using _ as self because I don't use any parameters or attributes
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
#this is just the start, because I will implement more OOP concepts later.
player = Game()
player.intro()