"""Random events system"""

import random


class EventManager:
    """Manage random game events"""
    
    def __init__(self):
        self.events = [
            {
                "name": "🌧️ Rain",
                "description": "It's raining! You collect rainwater.",
                "effect": lambda player: player.drink(20),
                "probability": 0.2
            },
            {
                "name": "🐗 Wild boar encounter",
                "description": "A wild boar appears! What do you do?",
                "type": "choice",
                "choices": {
                    "1": {
                        "text": "Run away (costs energy)",
                        "effect": lambda player: player.consume_energy(15)
                    },
                    "2": {
                        "text": "Try to hunt (risky but food)",
                        "effect": self._hunt_boar
                    }
                },
                "probability": 0.15
            },
            {
                "name": "🍎 Wild fruits discovery",
                "description": "You find edible fruits!",
                "effect": lambda player: player.eat(25),
                "probability": 0.25
            },
            {
                "name": "💧 Water source",
                "description": "You discover a clear water source!",
                "effect": lambda player: player.drink(30),
                "probability": 0.2
            },
            {
                "name": "🦅 Peaceful observation",
                "description": "You watch an eagle soaring. Peaceful moment.",
                "effect": lambda player: player.rest(5),
                "probability": 0.15
            },
            {
                "name": "🐍 Snake!",
                "description": "A snake! You barely avoid it but are exhausted.",
                "effect": lambda player: player.consume_energy(20),
                "probability": 0.1
            }
        ]
    
    def _hunt_boar(self, player):
        """Handle wild boar hunting (random)"""
        player.consume_energy(25)
        
        if random.random() > 0.5:  # 50% success
            player.eat(40)
            return "\n✅ Successful hunt! You eat meat."
        else:
            return "\n❌ Hunt failed. You wasted energy."
    
    def trigger_random_event(self, player):
        """
        Trigger a random event based on probabilities.
        Return None if no event occurs.
        """
        # 60% chance that an event occurs
        if random.random() > 0.6:
            return None
        
        # Select an event based on probabilities
        event = random.choices(
            self.events,
            weights=[e["probability"] for e in self.events],
            k=1
        )[0]
        
        return event
    
    def apply_event(self, event, player):
        """
        Apply the event effect to the player.
        Return a result message if any.
        """
        print("\n" + "="*60)
        print(f"📢 EVENT: {event['name']}")
        print("="*60)
        print(event['description'])
        
        # Event with choices
        if event.get("type") == "choice":
            print("\nOptions:")
            for key, choice in event["choices"].items():
                print(f"  {key}. {choice['text']}")
            
            player_choice = input("\nYour choice: ").strip()
            
            if player_choice in event["choices"]:
                result = event["choices"][player_choice]["effect"](player)
                if result:
                    print(result)
            else:
                print("❌ Invalid choice. You run away by reflex.")
                event["choices"]["1"]["effect"](player)
        
        # Automatic event
        else:
            event["effect"](player)
        
        print("="*60)
        input("\nPress Enter to continue...")
