"""Player actions manager"""


class ActionManager:
    """Manages the actions the player can take each day"""
    
    def __init__(self):
        self.actions = {
            "1": {
                "name": "🎣 Fish",
                "description": "Try to catch fish",
                "function": self.fish
            },
            "2": {
                "name": "💧 Search for water",
                "description": "Look for a water source",
                "function": self.search_water
            },
            "3": {
                "name": "😴 Sleep",
                "description": "Rest to recover energy",
                "function": self.sleep
            },
            "4": {
                "name": "🗺️ Explore",
                "description": "Explore the surroundings (random event)",
                "function": self.explore
            }
        }
    
    def fish(self, player, event_manager=None):
        """Fishing: reduces hunger but consumes energy."""
        print("\n🎣 You try to fish...")
        
        if player.energy < 15:
            print("❌ You're too exhausted to fish!")
            return
        
        player.consume_energy(15)
        
        import random
        if random.random() > 0.3:  # 70% success
            fish = random.randint(20, 35)
            player.eat(fish)
            print(f"✅ You catch a fish! (-{fish} hunger)")
        else:
            print("❌ No catch today. You spent energy.")
        
        print(f"⚡ Energy consumed: -15")
    
    def search_water(self, player, event_manager=None):
        """Search for water: reduces thirst, consumes energy."""
        print("\n💧 You search for water...")
        
        if player.energy < 10:
            print("❌ You're too exhausted to search for water!")
            return
        
        player.consume_energy(10)
        
        import random
        if random.random() > 0.2:  # 80% success
            water = random.randint(25, 40)
            player.drink(water)
            print(f"✅ You find water! (-{water} thirst)")
        else:
            print("❌ No water source found. You spent energy.")
        
        print(f"⚡ Energy consumed: -10")
    
    def sleep(self, player, event_manager=None):
        """Sleep: restores energy but increases hunger and thirst."""
        print("\n😴 You settle down to sleep...")
        
        energy_recovered = 50
        player.rest(energy_recovered)
        
        # Sleeping increases hunger and thirst
        player.hunger = min(100, player.hunger + 15)
        player.thirst = min(100, player.thirst + 20)
        
        print(f"✅ You rest well. (+{energy_recovered} energy)")
        print(f"⚠️  While sleeping: +15 hunger, +20 thirst")
    
    def explore(self, player, event_manager):
        """Explore: triggers a random event (beneficial or dangerous)."""
        print("\n🗺️ You go exploring the surroundings...")
        
        if player.energy < 10:
            print("❌ You're too exhausted to explore!")
            return
        
        player.consume_energy(10)
        print(f"⚡ Energy consumed: -10")
        
        # Trigger a random event
        if event_manager:
            event = event_manager.trigger_random_event(player)
            if event:
                input("\nPress Enter to continue...")
                event_manager.apply_event(event, player)
            else:
                print("\n🌲 You explore the area but find nothing particular.")
    
    def get_available_actions(self):
        """Return the list of available actions"""
        return self.actions
    
    def execute_action(self, choice, player, event_manager=None):
        """Execute the action chosen by the player"""
        if choice in self.actions:
            action = self.actions[choice]
            print("\n" + "="*60)
            print(f"⚡ ACTION: {action['name']}")
            print("="*60)
            action["function"](player, event_manager)
            print("="*60)
            return True
        else:
            print("\n❌ Invalid action. Please choose a valid number.")
            return False
