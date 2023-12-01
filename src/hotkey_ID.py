import pandas as pd
import os

def load_hotkeys_from_snapshot(log_file):
    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        return set(df['hotkey'].unique())
    else:
        print(f"Log file {log_file} not found.")
        return set()

def load_existing_hotkeys(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=['hotkey', 'hotkey_name'])

def display_existing_hotkeys(df):
    if not df.empty:
        sorted_df = df.sort_values(by='hotkey_name')
        print("Current Hotkeys and Their Names:")
        print(sorted_df)
    else:
        print("No existing hotkeys found.")

def rename_hotkeys(df):
    edit = input("Would you like to edit a hotkey name? (yes/no): ").strip().lower()
    while edit == 'yes':
        hotkey_to_edit = input("Enter the hotkey you want to rename: ").strip()
        if hotkey_to_edit in df['hotkey'].values:
            new_name = input(f"Enter a new name for hotkey {hotkey_to_edit}: ").strip()
            if new_name:
                df.loc[df['hotkey'] == hotkey_to_edit, 'hotkey_name'] = new_name
        else:
            print("Hotkey not found. Please enter a valid hotkey.")

        edit = input("Would you like to edit another hotkey name? (yes/no): ").strip().lower()

    return df

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, 'bittensor_snapshot.log')
    hotkey_file_path = os.path.join(script_dir, 'hotkey_names.csv')

    unique_hotkeys = load_hotkeys_from_snapshot(log_file_path)
    hotkey_df = load_existing_hotkeys(hotkey_file_path)

    # Display existing hotkeys if the file exists, sorted by hotkey_name
    display_existing_hotkeys(hotkey_df)

    existing_hotkeys = set(hotkey_df['hotkey'])
    new_hotkeys = unique_hotkeys - existing_hotkeys
    for hotkey in new_hotkeys:
        name = input(f"Enter a name for new hotkey {hotkey} (press Enter to skip): ").strip() or hotkey
        hotkey_df = hotkey_df._append({'hotkey': hotkey, 'hotkey_name': name}, ignore_index=True)

    hotkey_df = rename_hotkeys(hotkey_df)
    hotkey_df.to_csv(hotkey_file_path, index=False)

    print(f"Updated hotkey names saved to {hotkey_file_path}")

if __name__ == "__main__":
    main()
