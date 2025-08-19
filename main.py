import random

verbs = {
    "run": "ran",
    "eat": "ate",
    "go": "went",
    "see": "saw",
    "take": "took",
    "come": "came",
    "give": "gave",
    "know": "knew",
    "find": "found",
    "think": "thought",
    "make": "made",
    "say": "said",
    "tell": "told",
    "write": "wrote",
    "read": "read",
    "speak": "spoke",
    "begin": "began",
    "choose": "chose",
    "feel": "felt",
    "leave": "left",
    "meet": "met",
    "put": "put",
    "bring": "brought",
    "build": "built",
    "catch": "caught",
    "cost": "cost",
    "cut": "cut",
    "draw": "drew",
    "drive": "drove",
    "fall": "fell",
    "hear": "heard",
    "hold": "held",
    "keep": "kept",
    "lose": "lost",
    "pay": "paid",
    "send": "sent",
    "sit": "sat",
    "stand": "stood",
    "swim": "swam",
    "teach": "taught",
    "understand": "understood",
    "wear": "wore",
    "win": "won",
    "write": "wrote",
    "arise": "arose",
    "awake": "awoke",
    "bear": "bore",
    "become": "became",
    "begin": "began",
    "bleed": "bled",
}

def Game():
    while True:
        chosenVerb = random.choice(list(verbs.keys()))
        userInput = input(f"What's the past simple of {chosenVerb}?: \n").lower().strip()

        #I use != instead of == to check wrong answers first
        if userInput != verbs[chosenVerb]:
            print(f"Opps, the correct answer is: {verbs[chosenVerb]}") 
        else: 
            print("Correct!")

        if input("Do you want to continue? y/n: ").lower().strip() != "y":
            break

Game()