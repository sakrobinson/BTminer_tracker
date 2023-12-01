import os
import subprocess

def main_menu():
    # Get the directory where main.py is located
    src_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nMain Menu:")
        print("1. Log Miner Data")
        print("2. Input/Edit Hotkey Names")
        print("3. View Graphs")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Prompt for a PM2 process name
            process_name = input("Enter a name for the PM2 process: ")

            # Check if 'coldkey.txt' exists
            coldkey_path = os.path.join(src_dir, 'coldkey.txt')
            if not os.path.exists(coldkey_path):
                # Run 'prompt_coldkey.py' if 'coldkey.txt' does not exist
                subprocess.run(['python3', os.path.join(src_dir, 'prompt_coldkey.py')])
            
            # Then proceed to run 'snapshot.py' with PM2
            snapshot_script_path = os.path.join(src_dir, 'snapshot.py')
            pm2_command = ['pm2', 'start', snapshot_script_path, '--name', process_name, '--interpreter', 'python3']
            subprocess.run(pm2_command)

        elif choice == '2':
            # Run 'hotkey_ID.py'
            subprocess.run(['python3', os.path.join(src_dir, 'hotkey_ID.py')])

        elif choice == '3':
            # Run 'charts.py'
            subprocess.run(['python3', os.path.join(src_dir, 'charts.py')])

        elif choice == '4':
            # Exit the script
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
