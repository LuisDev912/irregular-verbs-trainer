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
        self.playing: bool = True

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
        
    def ask_question(self) -> None:
        chosen_verb = choice(list(verbs.keys()))
        user_input = input(f"\nWhat's the past simple of '{chosen_verb}'?\n -> ").strip().casefold()

        if user_input == verbs[chosen_verb].casefold():
            print("✅ Correct!")
            self.points += 1
        else:
            print(f"❌ Oops! The correct answer is: {verbs[chosen_verb]}")
            self.points = max(0, self.points - 1)  # prevents negative points
            self.incorrect_answers += 1

        print(f"Current score: {self.points}")


    def handle_action(self) -> None:
        action = input("\nChoose an option:\n"
                    "'y': Continue\n"
                    "'n': Stop playing\n"
                    "'info': See all verbs\n"
                    "'intro': See instructions again\n -> ").strip().lower()

        match action:
            case "y":
                pass
            case "info":
                self.show_info()
            case "intro":
                self.show_intro()
            case "n":
                self.playing = False
            case _:
                print("Invalid input. Continuing the game...")

    def start(self) -> None:
        self.playing = True
        self.show_intro()
        if input("Do you want to start the game? (y/n): ").strip().lower() == "y":
            while self.playing:
                self.ask_question()
                self.handle_action()
        print(f"\nGame Over! Your final score: {self.points} points. Thanks for playing! 👋")


player = Game()
player.show_intro()