## Survival Game (Terminal)

A Python Command Line Interface (CLI) application simulating the survival of an adventurer stranded on a deserted island. Manage your vital ressources, make strategic choices, and try to survive for several days.

## Features
- Simple terminal UI with clear gauges for Hunger, Thirst, and Energy
- Daily actions: Fish, Search water, Sleep, Explore
- Random events with choices and consequences
- Win condition: Survive 7 days; Lose if any gauge drops to 0
- Save/Load system using a JSON file in `saves/`
- Clean, modular Python code (no external dependencies)

## Requirements
- Python 3.8+ (standard library only)
- Windows, macOS, or Linux terminal

## Installation and startup
Clone the repository
    git clone https://github.com/elirbl/survival-game
Starting the game
    python main.py
Follow the on-screen instructions.

## How to play
1. Start a New Game or Load an existing save from the main menu.
2. Each day you can perform one action:
   - Fish: Chance to gain food, reduces thirst and energy a bit.
   - Search Water: Chance to find water, reduces hunger and energy a bit.
   - Sleep: Restores energy, but increases hunger and thirst slightly.
   - Explore: Discover items or trigger events, costs energy.
3. Random events can occur after your action. Make a choice and face the outcome.
4. End of day: Your gauges naturally degrade. If Hunger, Thirst, or Energy hits 0, it’s game over.
5. Survive 7 days to win!

Tips:
- Keep an eye on all three gauges—don’t tunnel on just one.
- Sleep before Energy gets too low to avoid a sudden loss.
- Exploring is risky but can pay off.

## Save and Load
- Saves are stored at `saves/savegame.json`.
- From the main menu, choose Load Game to continue.

## Project structure
```
.
├── main.py                 # Entry point: launches the game manager
├── saves/                  # Save files (JSON)
└── src/
	├── entities/
	│   └── player.py       # Player model: gauges, daily evolution, state I/O
	├── systems/
	│   ├── actions.py      # Actions you can take each day
	│   └── events.py       # Random events and outcomes
	├── ui/
	│   └── display.py      # Terminal UI helpers (menus, gauges)
	├── game/
	│   ├── game_loop.py    # Main loop: days, actions, events, win/lose
	│   └── game_manager.py # Main menu, new/load game flow
	└── utils/
		└── save_manager.py # JSON save/load utilities
```

## License
This project is released under the MIT License.

## Contributing
Project made by Elisabeth Robl
