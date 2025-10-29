"""Terminal user interface rendering"""


class Display:
    """Handles terminal output and simple UI rendering"""
    
    @staticmethod
    def clear_screen():
        """Clear the screen (optional; comment out if inconvenient)"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def show_gauges(player):
        """Show player's gauges with visual bars"""
        print("\n" + "="*60)
        print(f"📅 DAY {player.day} - {player.name}")
        print("="*60)
        
        # All gauges now work the same: 100 = full/good, 0 = empty/death
        # Hunger bar (100 = full, 0 = starving)
        hunger_bar = Display._create_bar(player.hunger, inverse=False)
        hunger_emoji = Display._get_hunger_emoji(player.hunger)
        print(f"{hunger_emoji} Hunger: {hunger_bar} {player.hunger}/100")
        
        # Thirst bar (100 = hydrated, 0 = dehydrated)
        thirst_bar = Display._create_bar(player.thirst, inverse=False)
        thirst_emoji = Display._get_thirst_emoji(player.thirst)
        print(f"{thirst_emoji} Thirst: {thirst_bar} {player.thirst}/100")
        
        # Energy bar (100 = rested, 0 = exhausted)
        energy_bar = Display._create_bar(player.energy, inverse=False)
        energy_emoji = Display._get_energy_emoji(player.energy)
        print(f"{energy_emoji} Energy: {energy_bar} {player.energy}/100")
        
        print("="*60)
        
        # Show alerts if gauges are in critical zones
        Display._show_alerts(player)
    
    @staticmethod
    def _create_bar(value, length=20, inverse=False):
        """
        Create a visual progress bar that empties as value decreases.
        All gauges now work the same way: 100 = full bar, 0 = empty bar.
        Color changes based on danger level (red < 20, orange < 50, green >= 50).
        """
        filled = int((value / 100) * length)
        empty = length - filled
        
        # Choose character color based on danger level
        """if value <= 20:"""
        char = "█"  # Red (critical)
        """
        elif value <= 50:
            char = "▓"  # Orange (medium)
        else:
            char = "░"  # Green (good)
        """
        
        # Bar empties from right to left as value decreases
        return f"[{char * filled}{'·' * empty}]"
    
    @staticmethod
    def _get_hunger_emoji(value):
        """Return an emoji matching hunger level (100 = full, 0 = starving)"""
        if value <= 20:
            return "🍖"  # Starving
        elif value <= 50:
            return "🍞"  # Hungry
        else:
            return "✅"  # Full
    
    @staticmethod
    def _get_thirst_emoji(value):
        """Return an emoji matching thirst level (100 = hydrated, 0 = dehydrated)"""
        if value <= 20:
            return "💧"  # Dehydrated
        elif value <= 50:
            return "🚰"  # Thirsty
        else:
            return "✅"  # Hydrated
    
    @staticmethod
    def _get_energy_emoji(value):
        """Return an emoji matching energy level (100 = rested, 0 = exhausted)"""
        if value <= 20:
            return "😴"  # Exhausted
        elif value <= 50:
            return "😐"  # Tired
        else:
            return "⚡"  # Energized
    
    @staticmethod
    def _show_alerts(player):
        """Show alerts if gauges are critical"""
        alerts = []
        
        if player.hunger <= 20:
            alerts.append("⚠️  DANGER: You're starving!")
        if player.thirst <= 20:
            alerts.append("⚠️  DANGER: You're dying of thirst!")
        if player.energy <= 20:
            alerts.append("⚠️  DANGER: You're exhausted!")
        
        if alerts:
            print("\n" + "\n".join(alerts))
            print()
    
    @staticmethod
    def show_action_menu(actions):
        """Display the available actions menu"""
        print("\n🎮 WHAT DO YOU WANT TO DO?")
        print("-"*60)
        
        for key, action in actions.items():
            print(f"  {key}. {action['name']} - {action['description']}")
        
        print("\n  S. 💾 Save game")
        print("  Q. 🚪 Quit")
        print("-"*60)
    
    @staticmethod
    def show_game_over(player, target_days):
        """Display the game over screen"""
        print("\n\n" + "="*60)
        print("                    ⚰️  GAME OVER  ⚰️")
        print("="*60)
        print(f"\n{player.get_death_cause()}")
        print(f"\n📅 You survived {player.day} day(s).")
        print(f"🎯 Goal: {target_days} days")
        print("\n" + "="*60)
    
    @staticmethod
    def show_victory(player, target_days):
        """Display the victory screen"""
        print("\n\n" + "="*60)
        print("                      🎉 VICTORY! 🎉")
        print("="*60)
        print(f"\n🏆 Congratulations {player.name}!")
        print(f"📅 You survived {target_days} full days!")
        print("\n✨ You are a true survivor!")
        print("\n" + "="*60)
    
    @staticmethod
    def show_main_menu():
        """Display the main menu"""
        print("\n" + "="*60)
        print("                        MAIN MENU")
        print("="*60)
        print("\n1. 🆕 New game")
        print("2. 📂 Load game")
        print("3. 🚪 Quit")
        print("\n" + "="*60)
