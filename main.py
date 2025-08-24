from random import choice

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

Game()