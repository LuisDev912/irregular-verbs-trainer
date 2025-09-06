from random import choice
from verbsContainer import verbs
from time import sleep

DEFAULT_SLEEP = 1.0

def print_pause(text: str, delay: float = DEFAULT_SLEEP) -> None:
    print(text)
    sleep(delay)

class Game:
    def __init__(self) -> None:
        self.points: int = 0
        self.incorrect_answers: int = 0

    def show_info(self):
        print("\nList of verbs and their past forms:\n")
        for verb, past in verbs.items():
            print(f"{verb} → {past}")
            sleep(0.5)
        #this shows every verb with its past simple form with a line break
        
        print(f"\n you answered correctly {self.points} times and incorrectly {self.incorrect_answers} times.\n")

    def show_intro(self) -> None:
        instructions = [
            "Welcome to the Past Simple Verb Game! 🎉",
            "The instructions are simple:",
            "1. The game will give you a verb in its base form, and you have to type its past simple form.",
            "2. Each correct answer earns you 1 point, each wrong answer deducts 1 point.",
            "3. Example: if the verb is 'go', you should type 'went'.",
            "4. You can quit anytime by typing 'n' when asked if you want to continue.",
            "Good luck! 🍀\n"
        ]
        for line in instructions:
            print_pause(line, 1.2)
        
        if input("Do you want to start the game? y/n: \n ->").lower().strip() == "y":
            self.main_game()
            
    def main_game(self) -> None: 
        while True:
            chosen_verb = choice(list(verbs.keys()))
            user_input = input(f"What's the past simple of {chosen_verb}?: \n------------------------------------------ \n ->").lower().strip()
            #I use != instead of == to check wrong answers first
            if user_input != verbs[chosen_verb]:
                print(f" ❌ Opps, the correct answer is: {verbs[chosen_verb]}") 
                self.points -= 1
                self.incorrect_answers += 1
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
                    Game.show_info(self)
                case "intro":
                    Game.show_intro(self)
                case "n":
                    break
            
        print(f"Your final score is: {self.points} points. Thanks for playing! 👋")


player = Game()
player.show_intro()