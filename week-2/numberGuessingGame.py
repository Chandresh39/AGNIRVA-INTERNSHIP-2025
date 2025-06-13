import random

def number_guessing_game():
    # Let the player choose a difficulty level
    print("Choose a difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    choice = int(input("Enter your choice: "))
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    if choice == 1:
        secret_number = random.randint(1, 50)
        range_max = 50
    elif choice == 2:
        secret_number = random.randint(1, 100)
        range_max = 100
    elif choice == 3:
        secret_number = random.randint(1, 500)
        range_max = 500
   
    attempts = 0
    max_attempts = 10

    print(f"I have selected a number between 1 and {range_max}. Can you guess it?")

    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
                print(f"You have {max_attempts - attempts} attempts left.")
            elif guess > secret_number:
                print("Too high! Try again.")
                print(f"You have {max_attempts - attempts} attempts left.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        if attempts == max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
            break

def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        number_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
