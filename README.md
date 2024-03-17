### Hangman Game

This is a simple implementation of the classic game Hangman in Python. In this game, players try to guess a word by suggesting letters within a limited number of attempts. The word to be guessed is randomly selected from a predefined list based on the chosen difficulty level.

### How to Play

1. **Game Modes:**

    - Easy Mode (Level 1): Guess words with a maximum of 3 letters. You have 10 attempts to guess the word.
    - Medium Mode (Level 2): Guess words with a maximum of 8 letters. You have 8 attempts to guess the word.
    - Difficult Mode (Level 3): Guess words with more than 8 letters. You have 6 attempts to guess the word.

2. **Guess the Word**: The player attempts to guess the word by entering letters one at a time. If the letter is correct and part of the word, it will be revealed. Otherwise, the player loses one attempt.

3. **Win or Lose**: The player wins the game if they correctly guess all the letters of the word within the specified number of attempts. If the attempts run out before the word is guessed, the player loses the game.

4. **Scoring**: Players earn points based on the number of words they successfully guess. The game displays the final score at the end of each session.

5. **Play Again**: After each game, the player has the option to play again or quit. Their score accumulates across multiple games.

### Game Controls

- **Difficulty Selection**: Enter the corresponding number (1 for Easy, 2 for Medium, 3 for Difficult) to choose the difficulty level.
- **Guessing Letters**: Type a letter and press Enter to guess. Letters can be uppercase or lowercase.
- **Play Again Prompt**: Respond with 'Y' or 'N' to indicate whether you want to play again or quit.

### Files

- **my_dict.txt**: Contains a list of words used for the game. The words are categorized by difficulty level based on their length.

### How to Run

1. Ensure that `my_dict.txt` is located in the `python/hangman/` directory.
2. Run the Python script `hangman.py`.
3. Follow the on-screen instructions to play the game.

### Additional Notes
- The game keeps track of your score across multiple sessions.
- Customize `my_dict.txt` to include your own word list for more personalized gameplay.

Enjoy playing Hangman!
