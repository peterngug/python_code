class Superhero:
    """Base class representing a superhero"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations):
        self._name = name  # Encapsulated attribute
        self._secret_identity = secret_identity  # Encapsulated attribute
        self.powers = powers
        self.base_of_operations = base_of_operations
        self._health = 100  # Private attribute
        self._energy = 100  # Private attribute
    
    @property
    def name(self):
        """Getter for name with proper encapsulation"""
        return self._name
    
    @property
    def secret_identity(self):
        """Getter for secret identity"""
        return "Classified" if self._health > 0 else self._secret_identity
    
    def use_power(self, power_index):
        """Method to use a specific power"""
        if self._energy >= 10:
            power = self.powers[power_index]
            self._energy -= 10
            return f"{self._name} uses {power}!"
        return f"{self._name} is too exhausted to use powers!"
    
    def take_damage(self, amount):
        """Method to take damage"""
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            return f"{self._name} has been defeated!"
        return f"{self._name} takes {amount} damage! Health: {self._health}"
    
    def rest(self):
        """Method to restore energy"""
        self._energy = min(100, self._energy + 30)
        return f"{self._name} rests and recovers energy! Energy: {self._energy}"
    
    def __str__(self):
        """String representation of the superhero"""
        return (f"Superhero: {self._name}\n"
                f"Base: {self.base_of_operations}\n"
                f"Powers: {', '.join(self.powers)}")
    
    def call_for_backup(self):
        """Polymorphic method to be overridden by subclasses"""
        return f"{self._name} calls for backup from the Justice League!"


class Avenger(Superhero):
    """Subclass representing an Avenger"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations, avenger_rank):
        super().__init__(name, secret_identity, powers, base_of_operations)
        self.avenger_rank = avenger_rank
        self._energy = 120  # Avengers have more energy
    
    def assemble(self):
        """Special method for Avengers"""
        return f"Avenger {self._name} answers the call to assemble!"
    
    def call_for_backup(self):
        """Override parent method with Avenger-specific behavior"""
        return f"{self._name} activates the Avengers emergency beacon!"


class XMen(Superhero):
    """Subclass representing an X-Men member"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations, mutation_level):
        super().__init__(name, secret_identity, powers, base_of_operations)
        self.mutation_level = mutation_level
    
    def use_power(self, power_index):
        """Override with X-Men specific power usage"""
        if self._energy >= 8:  # X-Men use less energy
            power = self.powers[power_index]
            self._energy -= 8
            return f"{self._name} activates mutant power: {power}!"
        return f"{self._name} is too exhausted to use mutant abilities!"
    
    def call_for_backup(self):
        """Override parent method with X-Men-specific behavior"""
        return f"{self._name} sends a psychic distress call to Professor X!"


# Example usage
if __name__ == "__main__":
    print("=== Superhero Class Demonstration ===")
    
    # Create a generic superhero
    superman = Superhero(
        name="Superman",
        secret_identity="Clark Kent",
        powers=["Flight", "Super Strength", "Heat Vision", "Freeze Breath"],
        base_of_operations="Fortress of Solitude"
    )
    print(superman)
    print(superman.use_power(0))
    print(superman.take_damage(25))
    print(superman.secret_identity)
    print(superman.call_for_backup())
    print()
    
    # Create an Avenger
    iron_man = Avenger(
        name="Iron Man",
        secret_identity="Tony Stark",
        powers=["Repulsor Beams", "Flight", "AI Assistance", "Missiles"],
        base_of_operations="Avengers Tower",
        avenger_rank="Founding Member"
    )
    print(iron_man)
    print(iron_man.assemble())
    print(iron_man.use_power(1))
    print(iron_man.call_for_backup())
    print()
    
    # Create an X-Men
    wolverine = XMen(
        name="Wolverine",
        secret_identity="Logan",
        powers=["Regeneration", "Adamantium Claws", "Enhanced Senses"],
        base_of_operations="X-Mansion",
        mutation_level="Omega"
    )
    print(wolverine)
    print(wolverine.use_power(1))
    print(wolverine.take_damage(40))
    print(wolverine.call_for_backup())
    print(wolverine.take_damage(80))  # Defeated
    print(wolverine.secret_identity)  # Revealed when defeated