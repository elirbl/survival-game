"""Save manager for game state persistence"""

import json
import os
from datetime import datetime


class SaveManager:
    """Manages saving and loading game sessions to/from JSON"""
    
    SAVE_DIR = "saves"
    SAVE_FILE = "savegame.json"
    
    def __init__(self):
        # Create save directory if it doesn't exist
        if not os.path.exists(self.SAVE_DIR):
            os.makedirs(self.SAVE_DIR)
        
        self.save_path = os.path.join(self.SAVE_DIR, self.SAVE_FILE)
    
    def save(self, player):
        """
        Saves the player's state to a JSON file.
        Returns True on success, False otherwise.
        """
        try:
            data = {
                "name": player.name,
                "day": player.day,
                "hunger": player.hunger,
                "thirst": player.thirst,
                "energy": player.energy,
                "save_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            with open(self.save_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"\n✅ Game saved successfully!")
            print(f"📁 File: {self.save_path}")
            return True
        
        except Exception as e:
            print(f"\n❌ Error while saving: {e}")
            return False
    
    def load(self):
        """
        Loads the player's state from the JSON file.
        Returns a dictionary with the data, or None on failure.
        """
        if not os.path.exists(self.save_path):
            print(f"\n❌ No saved game found.")
            return None
        
        try:
            with open(self.save_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"\n✅ Game loaded successfully!")
            print(f"📅 Saved on: {data.get('save_date', 'Unknown')}")
            return data
        
        except Exception as e:
            print(f"\n❌ Error while loading: {e}")
            return None
    
    def save_exists(self):
        """Checks if a save file exists"""
        return os.path.exists(self.save_path)
    
    def delete_save(self):
        """Deletes the save file"""
        if os.path.exists(self.save_path):
            try:
                os.remove(self.save_path)
                return True
            except Exception as e:
                print(f"❌ Error while deleting: {e}")
                return False
        return False
