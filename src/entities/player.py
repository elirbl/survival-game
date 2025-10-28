"""Player class with vital gauges management"""


class Player:
    """
    Represents the player with vital gauges.
    
    Gauges:
    - Hunger: 100 (full) -> 0 (starving) -> game over
    - Thirst: 100 (hydrated) -> 0 (dehydrated) -> game over
    - Energy: 100 (rested) -> 0 (exhausted) -> game over
    """
    
    # Critical thresholds for game over
    MIN_HUNGER = 0
    MIN_THIRST = 0
    MIN_ENERGY = 0
    
    def __init__(self, name="Adventurer"):
        self.name = name
        self.day = 1
        
        # Vital gauges (as per specifications)
        self.hunger = 70      # 100 = full, 0 = starving
        self.thirst = 70      # 100 = hydrated, 0 = dehydrated
        self.energy = 100     # 100 = rested, 0 = exhausted
    
    def is_alive(self):
        """Check if the player is still alive"""
        return (self.hunger > self.MIN_HUNGER and 
                self.thirst > self.MIN_THIRST and 
                self.energy > self.MIN_ENERGY)
    
    def natural_evolution(self):
        """
        Natural evolution of gauges each day.
        All gauges decrease naturally over time.
        """
        self.hunger = max(0, self.hunger - 10)
        self.thirst = max(0, self.thirst - 15)
        self.energy = max(0, self.energy - 5)
    
    def eat(self, amount):
        """Increase fullness (100 = full)"""
        self.hunger = min(100, self.hunger + amount)
    
    def drink(self, amount):
        """Increase hydration (100 = hydrated)"""
        self.thirst = min(100, self.thirst + amount)
    
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
        self.hunger = state.get("hunger", 70)
        self.thirst = state.get("thirst", 70)
        self.energy = state.get("energy", 100)
    
    def get_death_cause(self):
        """Return the cause of death"""
        if self.hunger >= self.MIN_HUNGER:
            return "Died of starvation..."
        elif self.thirst >= self.MIN_THIRST:
            return "Died of dehydration..."
        elif self.energy <= self.MIN_ENERGY:
            return "Died of exhaustion..."
        return "Death"
