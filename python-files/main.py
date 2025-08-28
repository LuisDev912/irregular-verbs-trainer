from random import choice
from verbsContainer import verbs

class Game:
    def __init__(self, points = 0, incorrectAnswers = 0):
        self.points = points
        self.incorrectAnswers = incorrectAnswers

    def info(self):
        print("The list of the verbs and its answers are: \n", verbs) #this is just for testing purposes, to see the list of verbs
        print(f"\n you answered correctly {self.points} times and incorrectly {self.incorrectAnswers} times.\n")

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
                self.incorrectAnswers += 1
            else: 
                print("Correct! ☑️") #using emojis is not necessary, but it makes the game more fun
                self.points += 1

            if self.points < 0:
                self.points = 0 #this avoids negative points

            print(f"current points: {self.points}")

            match input("What do you want to do next?: ('y' for continue, 'n' for stop playing, 'info' for see the information, 'intro' for know how to play\n ->").lower().strip(): #this is similar to switch case in other languages or an if else statement
                case "y":
                    continue
                case "info":
                    Game.info(self)
                case "intro":
                    Game.intro(self)
                case "n":
                    break
        print(f"Your final score is: {self.points} points. Thanks for playing! 👋")
#this is just the start, because I will implement more OOP concepts later.

player = Game()
player.intro()