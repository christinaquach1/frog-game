# Frog Puzzle Game

A classic leap frog puzzle game where two teams must swap positions.

## Objective

Swap the positions of the red team (🔴) and blue team (🔵). The game starts with:

```
🔴 🔴 🔴 🔴 ⚫ 🔵 🔵 🔵 🔵
```

And you win when the board looks like:

```
🔵 🔵 🔵 🔵 ⚫ 🔴 🔴 🔴 🔴
```

## How to Play

1. The board has 9 positions numbered 1-9
2. Enter a number to select which piece to move
3. Red pieces (🔴) can only move right, blue pieces (🔵) can only move left
4. You can move 1 space into an empty spot
5. You can jump over 1 piece into an empty spot 2 spaces away

## Rules

- You cannot move a piece onto an occupied space
- You cannot move a piece if there's no valid move available
- The empty space (⚫) is where pieces can move to

## Running the Game

```bash
python main.py
```

## Strategy Tip

Don't let pieces of the same color get stuck behind each other with no room to jump!
