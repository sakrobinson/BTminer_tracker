import os
import subprocess

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Log Miner Data")
        print("2. Input/Edit Hotkey Names")
        print("3. View Graphs")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Check if 'coldkey.txt' exists
            if not os.path.exists('coldkey.txt'):
                # Run 'prompt_coldkey.py' if 'coldkey.txt' does not exist
                subprocess.run(['/bin/python3', 'prompt_coldkey.py'])
            # Then proceed to run 'snapshot.py'
            subprocess.run(['/bin/python3', 'snapshot.py'])

        elif choice == '2':
            # Run 'hotkey_ID.py'
            subprocess.run(['/bin/python3', 'hotkey_ID.py'])

        elif choice == '3':
            # Run 'charts.py'
            subprocess.run(['/bin/python3', 'charts.py'])

        elif choice == '4':
            # Exit the script
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
