import random

def guess_the_number():
    # Step 1: Generate a Random Number
    secret_number = random.randint(1, 100)
    
    # Step 4: Repeat Until Correct Guess
    while True:
        # Step 2: Get User Input
        guess = int(input("Guess the number (between 1 and 100): "))
        
        # Step 3: Compare Guess with Random Number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")
            break  # End the game

def ai_guess_number():
    # Step 1: Initialize the Search Range
    min_num = 1
    max_num = 100
    
    # Step 4: Repeat Until Correct Guess
    while True:
        # Step 2: Guessing Algorithm
        guess = (min_num + max_num) // 2
        
        # Step 3: Feedback
        print("AI guesses:", guess)
        feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").upper()
        
        if feedback == "H":
            max_num = guess - 1
        elif feedback == "L":
            min_num = guess + 1
        elif feedback == "C":
            print("AI wins!")
            break

if __name__ == "__main__":
    print("Welcome to the Guess the Number game!")
    print("1. Play against the computer (human vs. AI)")
    print("2. Let the computer play (AI vs. AI)")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        guess_the_number()
    elif choice == "2":
        ai_guess_number()
    else:
        print("Invalid choice. Please enter 1 or 2.")
