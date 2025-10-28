"""Main game loop"""

import random
from src.entities.player import Player
from src.systems.actions import ActionManager
from src.systems.events import EventManager
from src.ui.display import Display
from src.utils.save_manager import SaveManager


class GameLoop:
    """Manages the main game loop with day cycles"""
    
    # Number of days to survive to win
    TARGET_DAYS = 7
    
    def __init__(self, player):
        self.player = player
        self.action_manager = ActionManager()
        self.event_manager = EventManager()
        self.display = Display()
        self.save_manager = SaveManager()
        self.running = False
    
    def start(self):
        """Start the main game loop"""
        self.running = True
        
        print(f"\n🎯 Goal: Survive {self.TARGET_DAYS} days!")
        print("📋 Manage your vital resources each day.")
        input("\nPress Enter to start...")
        
        while self.running and self.player.is_alive():
            # Display player's status
            self.display.show_gauges(self.player)
            
            # Random events at the start of the day
            self._handle_random_events()
            
            # Show actions menu
            actions = self.action_manager.get_available_actions()
            self.display.show_action_menu(actions)
            
            # Player's choice
            choice = input("\nYour choice: ").strip().lower()
            
            # Handle player's choice
            if choice == 'q':
                if self._confirm_quit():
                    self.running = False
                    break
            elif choice == 's':
                self.save_manager.save(self.player)
                input("\nPress Enter to continue...")
            else:
                # Execute chosen action
                if self.action_manager.execute_action(choice, self.player, self.event_manager):
                    # Natural evolution of gauges
                    self.player.natural_evolution()
                    
                    # Advance to the next day
                    self.player.increment_day()
                    
                    # Check for victory
                    if self.player.day > self.TARGET_DAYS:
                        self._victory()
                        break
                
                input("\nPress Enter to continue...")
        
        # End of game
        if not self.player.is_alive():
            self._game_over()
    
    def _handle_random_events(self):
        """Handle random events at the start of the day"""
        # 40% chance an event occurs
        if random.random() < 0.4:
            event = self.event_manager.trigger_random_event(self.player)
            if event:
                self.event_manager.apply_event(event, self.player)
    
    def _game_over(self):
        """Show the game over screen"""
        self.display.show_game_over(self.player, self.TARGET_DAYS)
        
        # Delete save after game over
        self.save_manager.delete_save()
    
    def _victory(self):
        """Show the victory screen"""
        self.display.show_victory(self.player, self.TARGET_DAYS)
        
        # Delete save after victory
        self.save_manager.delete_save()
    
    def _confirm_quit(self):
        """Ask for confirmation before quitting"""
        print("\n⚠️  Do you want to save before quitting?")
        print("1. Yes, save and quit")
        print("2. No, quit without saving")
        print("3. Cancel")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "1":
            self.save_manager.save(self.player)
            return True
        elif choice == "2":
            print("\n👋 See you soon!")
            return True
        else:
            return False
