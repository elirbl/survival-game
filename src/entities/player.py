"""Player class with vital gauges management"""


class Player:
    """
    Represents the player with vital gauges.
    
    Gauges:
    - Hunger: 0 (full) -> 100 (starving) -> game over
    - Thirst: 0 (hydrated) -> 100 (dehydrated) -> game over
    - Energy: 100 (rested) -> 0 (exhausted) -> game over
    """
    
    # Critical thresholds for game over
    MAX_HUNGER = 100
    MAX_THIRST = 100
    MIN_ENERGY = 0
    
    def __init__(self, name="Adventurer"):
        self.name = name
        self.day = 1
        
        # Vital gauges (as per specifications)
        self.hunger = 30      # 0 = full, 100 = starving
        self.thirst = 30      # 0 = hydrated, 100 = dehydrated
        self.energy = 100     # 100 = rested, 0 = exhausted
    
    def is_alive(self):
        """Check if the player is still alive"""
        return (self.hunger < self.MAX_HUNGER and 
                self.thirst < self.MAX_THIRST and 
                self.energy > self.MIN_ENERGY)
    
    def natural_evolution(self):
        """
        Natural evolution of gauges each day.
        Hunger and thirst increase, energy slightly decreases.
        """
        self.hunger = min(100, self.hunger + 10)
        self.thirst = min(100, self.thirst + 15)
        self.energy = max(0, self.energy - 5)
    
    def eat(self, amount):
        """Decrease hunger (0 = full)"""
        self.hunger = max(0, self.hunger - amount)
    
    def drink(self, amount):
        """Decrease thirst (0 = hydrated)"""
        self.thirst = max(0, self.thirst - amount)
    
    def rest(self, amount):
        """Increase energy"""
        self.energy = min(100, self.energy + amount)
    
    def consume_energy(self, amount):
        """Consume energy when performing an action"""
        self.energy = max(0, self.energy - amount)
    
    def increment_day(self):
        """Advance to the next day"""
        self.day += 1
    
    def get_state(self):
        """Return the player's current state as a dictionary"""
        return {
            "name": self.name,
            "day": self.day,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "energy": self.energy
        }
    
    def load_state(self, state):
        """Load a saved state"""
        self.name = state.get("name", self.name)
        self.day = state.get("day", 1)
        self.hunger = state.get("hunger", 30)
        self.thirst = state.get("thirst", 30)
        self.energy = state.get("energy", 100)
    
    def get_death_cause(self):
        """Return the cause of death"""
        if self.hunger >= self.MAX_HUNGER:
            return "Died of starvation..."
        elif self.thirst >= self.MAX_THIRST:
            return "Died of dehydration..."
        elif self.energy <= self.MIN_ENERGY:
            return "Died of exhaustion..."
        return "Death"
