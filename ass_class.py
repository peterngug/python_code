class Superhero:
    def __init__(self, name, secret_identity, powers, base):
        self._name = name
        self._secret_identity = secret_identity
        self.powers = powers
        self.base = base
        self._health = 100
        self._energy = 100

    @property
    def name(self): return self._name

    @property
    def secret_identity(self):
        return "Classified" if self._health > 0 else self._secret_identity

    def use_power(self, index):
        if self._energy >= 10:
            self._energy -= 10
            return f"{self._name} uses {self.powers[index]}!"
        return f"{self._name} is too exhausted to use powers!"

    def take_damage(self, dmg):
        self._health = max(0, self._health - dmg)
        return f"{self._name} {'has been defeated!' if self._health == 0 else f'takes {dmg} damage! Health: {self._health}'}"

    def rest(self):
        self._energy = min(100, self._energy + 30)
        return f"{self._name} recovers energy! Energy: {self._energy}"

    def __str__(self):
        return f"Superhero: {self._name}\nBase: {self.base}\nPowers: {', '.join(self.powers)}"

    def call_for_backup(self):
        return f"{self._name} calls for backup from the Justice League!"


class Avenger(Superhero):
    def __init__(self, name, secret_id, powers, base, rank):
        super().__init__(name, secret_id, powers, base)
        self.avenger_rank = rank
        self._energy = 120

    def assemble(self):
        return f"{self._name} answers the call to assemble!"

    def call_for_backup(self):
        return f"{self._name} activates the Avengers beacon!"


class XMen(Superhero):
    def __init__(self, name, secret_id, powers, base, mutation_level):
        super().__init__(name, secret_id, powers, base)
        self.mutation_level = mutation_level

    def use_power(self, index):
        if self._energy >= 8:
            self._energy -= 8
            return f"{self._name} uses mutant power: {self.powers[index]}!"
        return f"{self._name} is too exhausted to use powers!"

    def call_for_backup(self):
        return f"{self._name} sends a psychic call to Professor X!"


# Demo
if __name__ == "__main__":
    superman = Superhero("Superman", "Clark Kent", ["Flight", "Strength", "Vision"], "Fortress")
    print(superman, superman.use_power(0), superman.take_damage(25), superman.secret_identity, superman.call_for_backup(), sep="\n")

    ironman = Avenger("Iron Man", "Tony Stark", ["Beams", "Flight"], "Avengers Tower", "Leader")
    print("\n", ironman, ironman.assemble(), ironman.use_power(1), ironman.call_for_backup(), sep="\n")

    wolverine = XMen("Wolverine", "Logan", ["Claws", "Healing"], "X-Mansion", "Omega")
    print("\n", wolverine, wolverine.use_power(1), wolverine.take_damage(40), wolverine.call_for_backup(), wolverine.take_damage(80), wolverine.secret_identity, sep="\n")
