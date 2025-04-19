class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5   # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
        self.tricks = []  # For bonus feature

    def eat(self):
        """Reduces hunger by 3 (min 0) and increases happiness by 1 (max 10)"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")

    def sleep(self):
        """Increases energy by 5 (max 10)"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play. Maybe it's time to sleep?")

    def get_status(self):
        """Prints the current state of the pet"""
        print("\n--- Pet Status ---")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10 ({self._get_hunger_description()})")
        print(f"Energy: {self.energy}/10 ({self._get_energy_description()})")
        print(f"Happiness: {self.happiness}/10 ({self._get_happiness_description()})")
        
        if self.tricks:  # Only show tricks if any exist
            print(f"\n{self.name} knows these tricks: {', '.join(self.tricks)}")

    def _get_hunger_description(self):
        if self.hunger <= 2:
            return "Full"
        elif self.hunger <= 5:
            return "Peckish"
        elif self.hunger <= 8:
            return "Hungry"
        else:
            return "Starving!"

    def _get_energy_description(self):
        if self.energy <= 2:
            return "Exhausted"
        elif self.energy <= 5:
            return "Tired"
        elif self.energy <= 8:
            return "Energetic"
        else:
            return "Full of energy!"

    def _get_happiness_description(self):
        if self.happiness <= 2:
            return "Miserable"
        elif self.happiness <= 5:
            return "Content"
        elif self.happiness <= 8:
            return "Happy"
        else:
            return "Ecstatic!"

    # Bonus methods
    def train(self, trick):
        """Teaches the pet a new trick"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        """Prints all learned tricks"""
        if self.tricks:
            print(f"\n{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
