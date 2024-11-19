# Day 14 - Higher or Lower Game

## Overview
The **Higher or Lower Game** is a fun comparison game where players guess which of two Instagram accounts has more followers. The game continues as long as the player guesses correctly, with the score increasing for each correct answer. It ends when the player makes an incorrect guess.

## Key Features
- **Random Selection**: Uses `random.choice()` to select random Instagram profiles from a dataset.
- **Comparison Logic**: Compares the follower counts of two profiles based on user input ('A' or 'B').
- **Score Tracking**: Keeps track of the player's score and displays it after each correct guess.
- **Terminal Clearing**: Includes a function to clear the terminal screen for a cleaner user experience.

## Game Logic
1. **Profile Selection**:
   - Two random profiles are chosen from the dataset.
   - If the profiles are the same, a new profile is selected for comparison.
2. **Display Information**:
   - Shows details of "Account A" and "Account B" (name, description, country).
   - The player guesses which profile has more followers.
3. **Compare Followers**:
   - The `compare()` function checks if the player's guess is correct by comparing follower counts.
   - If the guess is correct, the score increases, and the player continues with a new comparison.
   - If the guess is incorrect, the game ends, and the final score is shown.
4. **Clearing Terminal**:
   - The `clear()` function is used to clear the terminal screen after each round for better readability.

## How to Play
1. Run the script.
2. Guess which profile has more followers by typing 'A' or 'B'.
3. Continue guessing correctly to increase your score.
4. The game ends when you make an incorrect guess, and your final score is displayed.

## Improvements
- **More Profiles**: Add additional data to enhance variety in comparisons.
- **Leaderboard**: Implement a feature to track and display high scores.
- **GUI Version**: Create a graphical version of the game for a better user experience.
