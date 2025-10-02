import random
import time
import os

# Normal Hangman Stages
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Sleeping Hangman ASCII
sleeping_hangman = """
   _____
  /     \\
 | () () |
  \\  ^  /
   |||||
   |||||
😴 The hangman is asleep...
"""

# Final Boss ASCII
final_boss_art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀
⠀⠀⣰⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⠀⠀⠀
⠀⢠⡇⠀⢸⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠈⠀⠀⡇⠀⠀
⠀⢸⡄⠀⠀⠢⣠⣴⡋⠉⠁⠀⠀⠀⠀⠀⠈⠻⣶⣄⡠⠃⠀⠀⡇⠀⠀
⡀⠈⣧⠀⠀⠀⠈⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⢠⠇⠀⡀
⣷⡀⠘⣆⠀⠀⠀⣿⠀⠀⠀⠀⠀⢀⣀⣠⡤⢾⣿⡁⠀⠀⢠⡟⠀⣴⡇
⡏⢻⣦⡘⣷⣦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠻⢷⣤⣴⡏⣠⡾⠃⠃
⢳⠀⠙⢿⣿⡏⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠣⡀⠀⠀⠀⢹⣿⠟⠀⢰⠀
⠈⢧⡀⢸⣿⣿⣀⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣀⠀⠈⣿⠀⢀⠌⠀
⠀⠀⠙⢾⣿⣿⣿⣿⡗⢄⡀⠀⡀⠀⡀⠀⡀⠔⡿⠀⠀⠀⣿⠔⠁⠀⠀
⠀⠀⠀⠀⢿⣿⡋⠉⠙⠒⠉⠙⡇⢀⡟⠉⠑⠊⠁⠀⠀⢠⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⡇⠀⠀⠀⢀⠀⠃⢸⣷⣀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣶⣶⣖⠛⠦⠀⠈⡿⠟⢑⣶⣶⣾⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣯⠉⢩⠧⠄⠓⠒⠁⣔⢵⠈⣡⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣧⠘⢜⣉⣁⣈⣉⣏⠄⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠐⠒⠒⠒⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⣀⣀⣀⣠⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Function to flash boss art
def show_final_boss():
    colors = ["\033[91m", "\033[93m", "\033[95m", "\033[94m", "\033[92m"]  # red, yellow, magenta, blue, green
    for i in range(8):  # flashes 8 times
        os.system("cls" if os.name == "nt" else "clear")
        print(colors[i % len(colors)] + final_boss_art + "\033[0m")
        time.sleep(0.3)


def final_boss(mode, lives, boss_appeared):
    """Handles Final Boss event. May change mode or grant lives."""
    show_final_boss()
    print("\n👹 Final Boss has appeared!")
    if mode == "asleep":
        lives = 3
        mode = "awake"  
        print("💖 The boss granted you 3 lives and woke the hangman!")
    elif mode == "awake":
        mode = "asleep"
        print("😈 The boss has put the hangman to sleep! You won't lose lives anymore.")
    boss_appeared = True
    return mode, lives, boss_appeared


win_streak = 0

# Main game loop
while True:
    print("\n" + "="*50)
    print(f"🔥 WIN STREAK: {win_streak}")
    if win_streak == 3:
        print("⚠️  WARNING: Final Boss will appear this game!")
    print("="*50)
    
    # Boss event: 20% random chance OR guaranteed on 4th win
    boss_event_enabled = (win_streak == 3) or (random.random() < 0.2)
    
    mode = input("Do you want the hangman to be asleep or awake? ").lower()

    if mode == "asleep":
        print(sleeping_hangman)
    elif mode == "awake":
        print(HANGMANPICS[0])  # Start with first stage of awake hangman
    else:
        print("Invalid choice, defaulting to asleep mode.")
        mode = "asleep"
        print(sleeping_hangman)

    word_list = [
    "pineapple", "yetti", "vampire", "ding",
    "castle", "dragon", "forest", "whisper", "shadow",
    "crystal", "river", "storm", "hunter",
    "galaxy", "sword", "phantom", "treasure", "oracle",
    "wizard", "dungeon", "raven", "serpent", "wanderer",
    "phoenix", "goblin", "troll", "mountain", "valley",
    "enchanted", "unicorn", "sapphire", "emerald", "diamond",
    "pirate", "brigand", "knight", "archer", "mystic",
    "thunder", "cyclone", "volcano", "tempest",
    "forest", "meadow", "jungle", "cavern", "oasis",
    "paladin", "necromancer", "assassin", "alchemist", "sorcerer",
    "lightning", "butterfly", "adventure", "mysterious", "hurricane"
    ]

    computer_choice = random.choice(word_list)
    hidden_word = ["_"] * len(computer_choice)
   
    print("Word:", " ".join(hidden_word))
    guessed_letters = set()                 
    wrong_guesses = set()                   
    max_lives = 5
    lives = max_lives
    boss_appeared = False  
    guess_count = 0 
    
    while "_" in hidden_word:
        # Asleep mode
        if mode == "asleep":        
            while "_" in hidden_word and mode == "asleep" :
                user = input("Enter a letter: ").lower()

                if len(user) != 1 or not user.isalpha():
                    print("❌ Please enter only a single letter (A-Z).")
                    continue

                if user in guessed_letters:
                    print("You have used this letter before, try again.")
                    continue   

                guessed_letters.add(user)
                
                if user in computer_choice:
                    for i, letter in enumerate(computer_choice):
                        if letter == user:
                            hidden_word[i] = user   
                    print("Correct:", " ".join(hidden_word))
                else:
                    print("Wrong guess! Try again.")
                guess_count += 1
                if boss_event_enabled and not boss_appeared and guess_count >= 4 and "_" in hidden_word:
                    mode, lives, boss_appeared = final_boss(mode, lives, boss_appeared)
        
        # Awake mode
        elif mode == "awake":
            while "_" in hidden_word and lives > 0 and mode == "awake":
                print(f"\nLives left: {'❤️' * lives}")
                print(HANGMANPICS[max_lives - lives])  # show hangman stage
                user = input("Enter a letter: ").lower()

                if len(user) != 1 or not user.isalpha():
                    print("❌ Please enter only a single letter (A-Z).")
                    continue

                if user in guessed_letters:
                    print("You have used this letter before, try again.")
                    continue

                guessed_letters.add(user)

                if user in computer_choice:
                    for i, letter in enumerate(computer_choice):
                        if letter == user:
                            hidden_word[i] = user
                    print("Correct:", " ".join(hidden_word))
                else:
                    print("Wrong guess!💔 Try again.")
                    wrong_guesses.add(user)
                    lives -= 1
                guess_count += 1
                if boss_event_enabled and not boss_appeared and guess_count >= 4 and "_" in hidden_word:
                    mode, lives, boss_appeared = final_boss(mode, lives, boss_appeared)
            
            if lives == 0:
                print(HANGMANPICS[-1])  # final stage if dead
                break

    # Final results and win streak update
    if "_" not in hidden_word:
        print("\n🎉 You guessed it! The word was:", computer_choice)
        win_streak += 1
        print(f"✨ WIN STREAK: {win_streak}")
    elif lives == 0:
        print("\n💀 Game over! The hangman got you. The word was:", computer_choice)
        print(f"💔 Win streak broken! You had {win_streak} wins.")
        win_streak = 0
    
    # Reset win streak if boss appeared on guaranteed 4th game
    if win_streak == 4 and boss_appeared:
        print("\n🏆 You survived the guaranteed boss encounter!")
        win_streak = 0
    
    # Ask to play again
    while True:
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again in ("yes", "y"):
            break  # continue to the next game
        elif play_again in ("no", "n"):
            print(f"\n👋 Thanks for playing! Final win streak: {win_streak}")
            exit()  # end the program
        else:
            print("❌ Invalid input. Please type 'yes' or 'no'.")
