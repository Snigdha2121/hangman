import random

def choose_word(choice):
    with open("python/hangman/my_dict.txt", "r") as file:
        word_list = file.readlines()
        if choice == 1:
            easy_words = [word.strip() for word in word_list if len(word.strip()) <= 3]
            return random.choice(easy_words)
        elif choice == 2:
            medium_words = [word.strip() for word in word_list if 4 < len(word.strip()) <= 8]
            return random.choice(medium_words)
        elif choice == 3:
            hard_words = [word.strip() for word in word_list if len(word.strip()) > 8]
            return random.choice(hard_words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print('*******************************')
    print("Welcome to the game of Hangman!\n")
    print("Instruction\n")
    print("Game Modes:\nEasy Mode (Level 1): Guess words with a maximum of 3 letters. You have 10 attempts to guess the word.\nMedium Mode (Level 2): Guess words with a maximum of 8 letters. You have 8 attempts to guess the word.\nDifficult Mode (Level 3): Guess words with more than 8 letters. You have 6 attempts to guess the word.")
    print("")
    point = 0
    while True:
        print("\nSelect the difficulty level of your game")
        print("Press 1 for easy!\nPress 2 for medium!\nPress 3 for difficult!\nPress 4 to quit the game!")
        choice = input("Enter your Choice: ")
        choice = int(choice)
        if choice == 4:
            print("Thank you for playing!")
            print("Your score is: ", point)            
            break
        elif choice not in [1, 2, 3]:
            print("Invalid choice! Please select 1, 2, 3, or 4.")
        else:
            word = choose_word(choice)
            guessed_letters = set()
            if(choice == 1):
                wrong_attempts = 10
            if(choice == 2):
                wrong_attempts = 8                
            if(choice == 3):
                wrong_attempts = 6

            print("\n \nThe word has", len(word), "letters.")

            while wrong_attempts > 0:
                print("\nWord:", display_word(word, guessed_letters))
                guess = input("Guess a letter: ").lower()

                if guess in guessed_letters:
                    print("You already guessed that letter.")
                else:
                    guessed_letters.add(guess)
                    if guess in word:
                        print("Correct guess!")
                        if set(word) <= guessed_letters:
                            print("\nCongratulations! You guessed the word:", word)
                            point += 1
                            break

                    else:
                        print("Wrong guess!")
                        wrong_attempts -= 1
                        print("You have", wrong_attempts, "attempts left.")

            if wrong_attempts == 0:
                print("\nGame over! The word was:", word)
            ans = input("\nDo you want to play again? (Y/N): ").strip().upper()
            if ans == 'N':
                print("\nThanks For playing")
                print("Your score is: ", point)
                break

hangman()
