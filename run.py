import subprocess
import os

def run_main():
    # Get the current directory of the run.py script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # The relative path to main.py inside the src directory
    main_script_path = os.path.join(current_dir, 'src', 'main.py')

    # Run the main.py using the python3 interpreter
    subprocess.run(['python3', main_script_path])

if __name__ == "__main__":
    run_main()
