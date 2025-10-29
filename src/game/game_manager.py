"""Main game manager"""

from src.entities.player import Player
from src.game.game_loop import GameLoop
from src.ui.display import Display
from src.utils.save_manager import SaveManager


class GameManager:
    """Coordinates the game and manages the main menu"""
    
    def __init__(self):
        self.display = Display()
        self.save_manager = SaveManager()
        self.player = None
        self.game_loop = None
    
    def run(self):
        """Main entry point to run the game"""
        while True:
            self.display.show_main_menu()
            
            choice = input("\nYour choice: ").strip()
            
            if choice == "1":
                self._new_game()
            elif choice == "2":
                self._load_game()
            elif choice == "3":
                print("\n👋 Thanks for playing! See you soon!")
                break
            else:
                print("\n❌ Invalid choice. Please enter 1, 2 or 3.")
    
    def _new_game(self):
        """Start a new game"""
        print("\n" + "="*60)
        print("              🆕 NEW GAME")
        print("="*60)
        
    # Ask for player's name
        name = input("\nEnter your name (or Enter for 'Adventurer'): ").strip()
        if not name:
            name = "Adventurer"
        
    # Create the player
        self.player = Player(name)
        
        print(f"\nWelcome {name}! 🏝️")
        print("You wake up on a deserted island...")
        print("You must survive by managing your vital resources.")
        
        # Start the game loop
        self.game_loop = GameLoop(self.player)
        self.game_loop.start()
    
    def _load_game(self):
        """Load a saved game"""
        print("\n" + "="*60)
        print("                       📂 LOADING")
        print("="*60)
        
        # Load data from disk
        data = self.save_manager.load()
        
        if data:
            # Create the player and load their state
            self.player = Player(data.get("name", "Adventurer"))
            self.player.load_state(data)
            
            print(f"\nWelcome back {self.player.name}!")
            print(f"📅 Day {self.player.day}")
            
            # Start the game loop
            self.game_loop = GameLoop(self.player)
            self.game_loop.start()
        else:
            print("\n⚠️  Unable to load game.")
            input("\nPress Enter to return to menu...")
