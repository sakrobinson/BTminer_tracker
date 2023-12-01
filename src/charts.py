import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import os

def load_hotkey_names(file_path):
    if os.path.exists(file_path):  # Use os.path.exists
        return pd.read_csv(file_path).set_index('hotkey').to_dict()['hotkey_name']
    return {}

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import os


def plot_combined_hotkeys(df, variable, hotkey_names):
    plt.figure(figsize=(15, 8))
    
    # Ensure the variable is numeric, stripping 'τ' if the variable is 'stake'
    if variable == 'stake':
        df[variable] = df[variable].str.replace('τ', '').astype(float)
    
    # Convert timestamps to datetime and sort
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values('timestamp', inplace=True)

    # Get unique hotkeys and sort by their names
    unique_hotkeys = df['hotkey'].unique()
    sorted_hotkeys = sorted(unique_hotkeys, key=lambda x: hotkey_names.get(x, 'Unknown'))

    # Plot each hotkey's data
    for hotkey in sorted_hotkeys:
        hotkey_data = df[df['hotkey'] == hotkey]
        if not hotkey_data.empty:
            plt.plot(hotkey_data['timestamp'], hotkey_data[variable], label=hotkey_names.get(hotkey, hotkey), marker='o', linestyle='-')

    # Formatting the plot
    plt.title(f'{variable.capitalize()} over time for all hotkeys')
    plt.xlabel('Time')
    plt.ylabel(variable.capitalize())
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_variable(filename, variable, hotkey):
    df = pd.read_csv(filename)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert timestamp column to datetime
    df_filtered = df[df['hotkey'] == hotkey]
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtered['timestamp'], df_filtered[variable], marker='o', markersize=3)
    plt.title(f'{variable} over time for {hotkey}')
    plt.xlabel('Time')
    plt.ylabel(variable)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def select_hotkey(df, hotkey_names):
    unique_hotkeys = df['hotkey'].unique()
    hotkeys_with_names = [(key, hotkey_names.get(key, 'Unknown')) for key in unique_hotkeys]
    hotkeys_with_names.sort(key=lambda x: x[1])  # Sort by hotkey name

    print("Available hotkeys:")
    for idx, (key, name) in enumerate(hotkeys_with_names, 1):
        print(f"{idx}. {key} ({name})")
    choice = input("Select a hotkey (number) or type 'exit' to quit: ")
    if choice.lower() == 'exit':
        return None
    try:
        selected_index = int(choice) - 1
        if 0 <= selected_index < len(unique_hotkeys):
            return hotkeys_with_names[selected_index][0]
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def main():
    # Get the directory where charts.py is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full paths to the data files
    filename = os.path.join(current_dir, 'hotkeys.log')
    hotkey_names_file = os.path.join(current_dir, 'hotkey_names.csv')

    # Load the hotkey names
    if not os.path.exists(hotkey_names_file):
        print(f"Error: The file {hotkey_names_file} was not found.")
        return  # Exit the function if the file is not found
    hotkey_names = load_hotkey_names(hotkey_names_file)

    # Load the data
    if not os.path.exists(filename):
        print(f"Error: The file {filename} was not found.")
        return  # Exit the function if the file is not found
    df = pd.read_csv(filename)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure timestamp is in datetime format for all functions

    while True:  # Main loop
        print("\nColumns in the DataFrame:", df.columns.tolist())

        print("\nSelect an action:")
        print("1. Plot variable for a single hotkey")
        print("2. Plot all hotkeys")
        print("3. Exit script")
        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            hotkey = select_hotkey(df, hotkey_names)
            if hotkey:
                while True:  # Variable selection loop for a single hotkey
                    print("\nSelect the variable to visualize:")
                    print("1. Emission")
                    print("2. Stake")
                    print("3. Exit to main menu")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        plot_variable(filename, 'emission', hotkey)
                    elif choice == '2':
                        plot_variable(filename, 'stake', hotkey)
                    elif choice == '3':
                        break  # Breaks the inner loop and goes back to action selection
                    else:
                        print("Invalid choice. Please try again.")

        elif main_choice == '2':
            print("\nSelect the variable for comparison across all hotkeys:")
            print("1. Emission")
            print("2. Stake")
            comp_choice = input("Enter your choice: ")
            variable = None
            if comp_choice == '1':
                variable = 'emission'
            elif comp_choice == '2':
                variable = 'stake'
    
            if variable:
                plot_combined_hotkeys(df, variable, hotkey_names)
            else:
                print("Invalid choice. Please try again.")

        elif main_choice == '3':
            break  # Exit the script
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
