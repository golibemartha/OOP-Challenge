class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        print(f"{self.name} munches happily 😋")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
       

    def sleep(self):
        print(f"{self.name} curls up and naps peacefully 😴")
        self.energy = min(10, self.energy + 5)
        self.happiness = max(0, self.happiness - 1)

    def play(self):
        if self.energy >= 2:
            print(f"{self.name} is playing happily 🐾😸🐾")
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else: 
            print(f"{self.name} is too tired to play. 😴")
    
    def train(self, trick):
        print(f"You are training {self.name} to do a trick 🐵")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} can do this trick: 🙊🙉🙈")
            for i, trick in enumerate(self.tricks):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet. 🐒")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"🍌 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"💖 Happiness: {self.happiness}/10")
        print(f"🎓 Tricks:{len(self.tricks)} learned\n")