#!/usr/bin/env python3
#print("Goodbye world 😈")
# TODO: Update the message

#print("*Explosion Sounds*")

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Start Game")
        print("2. Load Game")
        print("3. Options")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("Starting new game...")
            # Add your game-starting logic here
        elif choice == '2':
            print("Loading saved game...")
            # Add load logic
        elif choice == '3':
            print("Opening options...")
            # Add options logic
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
