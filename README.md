# Dungeon Chef

## About the Game

**Dungeon Chef** is a 2D top-down survival and cooking game built with **Python** and **Pygame**. Players explore a dangerous dungeon, avoid monsters, manage their health, and gather resources while working toward becoming the ultimate dungeon chef.

This project began as a way to learn game development and has grown into a larger game featuring enemy AI, health systems, collision detection, inventory mechanics, and camera movement.

---

## Current Features

* **Player Movement**

  * Move freely around the dungeon.

* **Enemy AI**

  * Monsters actively chase the player.

* **Health System**

  * Color-changing health bar that updates in real time.

* **Collision Detection**

  * Prevents players from walking through walls and objects.

* **Inventory Slots**

  * Foundation for future item and ingredient storage.

* **World Boundaries**

  * Keeps the player within the playable area.

* **Monster Spawning**

  * Enemies appear over time to increase difficulty.

* **Camera System**

  * Large world that follows the player as they explore.

* **Game Over Effects**

  * Visual effects when the player runs out of health.

---

## Controls

| Key             | Action     |
| --------------- | ---------- |
| W / Up Arrow    | Move Up    |
| A / Left Arrow  | Move Left  |
| S / Down Arrow  | Move Down  |
| D / Right Arrow | Move Right |

---

## Technologies Used

* **Python**
* **Pygame**
* **Object-Oriented Programming (OOP)**

---

## Planned Features

* **Cooking Recipes**
* **Ingredient Collection**
* **Inventory Management**
* **Magic Abilities**
* **Additional Enemy Types**
* **Quests and Objectives**
* **Dungeon Expansion**
* **Sound Effects and Music**
* **Story and Lore**
* **Save System**

---

## Learning from Dungeon Chef 

While developing Dungeon Chef, I learned how to:

* Design games using classes and objects
* Create collision systems
* Build enemy AI behavior
* Create health bars and UI elements
* Work with game loops and event handling
* Implement camera systems
* Organize larger Python projects
* Debug and improve gameplay systems

---

## Installation

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

During installation, make sure to enable **"Add Python to PATH"**.

### 2. Download the Project

Clone the repository:

```bash
git clone <repository-url>
```

Or download the project as a ZIP file and extract it.

### 3. Install Pygame

Open a terminal in the project folder and run:

```bash
pip install pygame
```

### 4. Verify the Installation

Check that Pygame was installed correctly:

```bash
python -m pygame.examples.aliens
```

If a small demo game opens, Pygame is installed successfully.

### 5. Run the Game

Navigate to the project folder and run:

```bash
python main.py
```

The game window should launch automatically.

---

## Troubleshooting

### Pygame Not Found

If you receive a message saying that Pygame is not installed:

```bash
pip install --upgrade pygame
```

### Missing Images

Make sure all required image files are located in the project folder and that their filenames match those used in the code.

### Game Will Not Start

Check that:

* Python is installed correctly.
* Pygame is installed.
* All project files are present.
* You are running the correct Python version.

---

## Project Status

**Dungeon Chef** is currently in active development. New mechanics, enemies, cooking systems, and gameplay features are being added as the project continues to grow.
