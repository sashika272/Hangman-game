import random

def load_words():
    try:
        with open("words.txt", "r") as file:
            return [word.strip() for word in file.readlines()]
    except FileNotFoundError:
        return ["python", "hangman", "developer", "programming", "github"]

def display_hangman(tries):
    stages = []
    try:
        with open("assets/hangman_stages.txt", "r") as file:
            stages = file.read().split("===")
    except FileNotFoundError:
        stages = ["[ASCII not available]"]
    return stages[6 - tries] if 0 <= tries <= 6 else "[Invalid stage]"

def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def hangman():
    word = random.choice(load_words()).lower()
    guessed = []
    tries = 6

    print("🎮 Welcome to Hangman!")
    print(display_hangman(tries))
    print(display_word(word, guessed))

    while tries > 0:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed:
            print("You've already guessed that.")
        elif guess in word:
            guessed.append(guess)
            print("Correct!")
        else:
            guessed.append(guess)
            tries -= 1
            print("Wrong!")
        
        print(display_hangman(tries))
        print(display_word(word, guessed))

        if "_" not in display_word(word, guessed):
            print("\n🎉 You won!")
            break
    else:
        print(f"\n💀 You lost! The word was: {word}")

if __name__ == "__main__":
    hangman()
