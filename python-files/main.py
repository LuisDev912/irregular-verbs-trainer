from random import choice
from verbsContainer import verbs
from time import sleep

class Game:
    def __init__(self, points = 0, incorrectAnswers = 0):
        self.points = points
        self.incorrectAnswers = incorrectAnswers

    def info(self):
        for verb, past in verbs.items():
            print(f"the {verb} verb in the past is: {past}")
            sleep(0.75)
        #this shows every verb with its past simple form with a line break
        
        print(f"\n you answered correctly {self.points} times and incorrectly {self.incorrectAnswers} times.\n")

    def intro(self):
        print("Welcome to the Past Simple Verb Game! 🎉")
        sleep(1.00)
        print("the instructions are simple:" )
        sleep(0.60)
        print("the game will give you a verb in its base form, and you have to type its past simple form.\n" )
        sleep(1.80)
        print("For each correct answer, you earn a point. For each wrong answer, you lose a point.\n" )
        sleep(1.80)
        print("For example, if the verb is 'go', you should type 'went'.\n" )
        sleep(1.80)
        print("You can quit the game anytime by typing 'n' when asked if you want to continue.\n" )
        sleep(1.80)
        print("Let's see how good is your knowledgement! Good luck! 🍀\n") 
            
        if input("Do you want to start the game? y/n: \n ->").lower().strip() == "y":
            self.mainGame()
            
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

            action = input("\n What do you want to do next?, here are the options: \n'y' for continue, \n'n' for stop playing, \n'info' for see the information, \n'intro' for know how to play\n ->").lower().strip()
            if action not in {"y", "n", "info", "intro"}:
                print("not valid input. Returning to the game.")
                continue
            match action: #this is similar to switch case in other languages or an if else statement
                case "y":
                    continue
                case "info":
                    Game.info(self)
                case "intro":
                    Game.intro(self)
                case "n":
                    break
            
        print(f"Your final score is: {self.points} points. Thanks for playing! 👋")


player = Game()
player.intro()