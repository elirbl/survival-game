#!/usr/bin/env python3
"""
Terminal Survival Game
Main entry point of the game
"""

from src.game.game_manager import GameManager


def main():
    """Launch the survival game"""
    print("="*60)
    print("SURVIVAL GAME - TERMINAL EDITION")
    print("="*60)
    print("\nGoal: Survive as long as possible!")
    print("⚠️  Manage your hunger, thirst and energy to stay alive.\n")
    
    game = GameManager()
    game.run()


if __name__ == "__main__":
    main()