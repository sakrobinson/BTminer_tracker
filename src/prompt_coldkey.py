import os

def get_coldkey_address():
    return input("Enter the coldkey address: ")

def main():
    coldkey_address = get_coldkey_address()
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    file_path = os.path.join(script_dir, 'coldkey.txt')     # Path to the file

    with open(file_path, 'w') as file:
        file.write(coldkey_address)

    print(f"Coldkey saved to {file_path}")

if __name__ == "__main__":
    main()
