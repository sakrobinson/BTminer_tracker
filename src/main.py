import os
import subprocess


def main_menu():
    src_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nMain Menu:")
        print("1. Log Miner Data")
        print("2. Input/Edit Hotkey Names")
        print("3. View Graphs")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # New code: Prompt for local or remote subtensor
            subtensor_choice = input("Choose subtensor type (local/remote): ").strip().lower()

            # New code: Handle the choice
            if subtensor_choice == 'local':
                endpoint = "ws://127.0.0.1:9944"  # Local endpoint
            elif subtensor_choice == 'remote':
                endpoint = input("Enter the remote endpoint: ")
            else:
                print("Invalid subtensor type. Please choose 'local' or 'remote'.")
                continue

            process_name = input("Enter a name for the PM2 process: ")

            coldkey_path = os.path.join(src_dir, 'coldkey.txt')
            if not os.path.exists(coldkey_path):
                subprocess.run(['python3', os.path.join(src_dir, 'prompt_coldkey.py')])

            snapshot_script_path = os.path.join(src_dir, 'snapshot.py')
            pm2_command = ['pm2', 'start', snapshot_script_path, '--name', process_name, '--interpreter', 'python3', '--', endpoint]
            subprocess.run(pm2_command)

        elif choice == '2':
            subprocess.run(['python3', os.path.join(src_dir, 'hotkey_ID.py')])

        elif choice == '3':
            subprocess.run(['python3', os.path.join(src_dir, 'charts.py')])

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
