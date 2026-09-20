# 🐍 Snake Water Gun Game

A simple command-line Snake-Water-Gun game developed using Python.

The player chooses Snake, Water, or Gun, while the computer randomly selects one of the three choices. The winner is determined using a 2D decision matrix.

## 🎮 Game Rules

| Player | Computer | Result |
|--------|----------|--------|
| Snake 🐍 | Water 💧 | Win |
| Water 💧 | Gun 🔫 | Win |
| Gun 🔫 | Snake 🐍 | Win |
| Snake 🐍 | Gun 🔫 | Lose |
| Water 💧 | Snake 🐍 | Lose |
| Gun 🔫 | Water 💧 | Lose |
| Same choice | Same choice | Draw |

## 🛠️ Technologies Used

- Python 3
- `random` module
- `sys` module
- 2D List / Matrix
- Conditional Statements
- User Input

## ⚙️ How It Works

1. The computer randomly selects a number between `0` and `2`.
2. The player enters Snake, Water, or Gun.
3. The player's choice is converted into a number:
   - Snake → `0`
   - Water → `1`
   - Gun → `2`
4. The player's number represents the **row** of the decision matrix.
5. The computer's number represents the **column**.
6. The result is obtained using the matrix lookup.
7. The program displays Win, Lose, or Draw.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python snake_water_gun.py
