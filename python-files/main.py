from random import choice
from verbsContainer import verbs

class Game:
    def __init__(self, points):
        self.points = points

    def intro(self):
        print("Welcome to the Past Simple Verb Game! 🎉\n" 
            "the instructions are simple:" 
            "the game will give you a verb in its base form, and you have to type its past simple form.\n" 
            "For each correct answer, you earn a point. For each wrong answer, you lose a point.\n" 
            "For example, if the verb is 'go', you should type 'went'.\n" 
            "You can quit the game anytime by typing 'n' when asked if you want to continue.\n" 
            "Let's see how good is your knowledgement! Good luck! 🍀\n" 
            )
        if input("Do you want to start the game? y/n: \n ->").lower().strip() == "y":
            Game.mainGame(self)
            
    def mainGame(self): 
        while True:
            chosenVerb = choice(list(verbs.keys()))
            userInput = input(f"What's the past simple of {chosenVerb}?: \n------------------------------------------ \n ->").lower().strip()
            #I use != instead of == to check wrong answers first
            if userInput != verbs[chosenVerb]:
                print(f" ❌ Opps, the correct answer is: {verbs[chosenVerb]}") 
                self.points -= 1
            else: 
                print("Correct! ☑️") #using emojis is not necessary, but it makes the game more fun
                self.points += 1

            if self.points < 0:
                self.points = 0 #this avoids negative self.points

            print(f"current points: {self.points}")

            if input("\n Do you want to continue? y/n: \n ->").lower().strip() != "y":
                break
        print(f"Your final score is: {self.points} points. Thanks for playing! 👋")
#this is just the start, because I will implement more OOP concepts later.
player = Game(0)
player.intro()