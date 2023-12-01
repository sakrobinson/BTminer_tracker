
# BTminer_tracker

**BTminer_tracker**: A program built to track and visualize emission and stake for all your miners on a given coldkey.

## Description

BTminer_tracker is designed to monitor and visualize various metrics related to blockchain miners, particularly focusing on emission and stake associated with a specific coldkey on the subtensor blockchain. It provides functionality for logging real-time data, configuring miner identifiers (hotkeys), and generating detailed visualizations to analyze trends and performance metrics.

## Requirements

- **Python Version**: Latest version of Python 3
- **Dependencies**:
  - Bittensor
  - Subtensor Node
  - PM2 (Process Manager)
  - Pandas
  - Matplotlib
  - OS, Subprocess, Time (standard Python libraries)

## Installation

1. **Clone the Repository**:
   \```bash
   git clone [repository URL]
   \```
2. **Install Dependencies**:
   Navigate to the project directory and run:
   \```bash
   pip install -r requirements.txt
   \```
   This command will install all the required Python packages.

## Usage

To start the application:
1. Run `run.py`:
   \```bash
   python3 run.py
   \```
   This will launch the main menu of the program.

2. Follow the on-screen instructions to:
   - Log miner data.
   - Input/Edit hotkey names.
   - View graphs and analytics.

## Configuration

- **Coldkey Setup**: On the first run, you'll be prompted to enter your coldkey address. This is crucial for fetching and associating data with your specific blockchain account.

- **Hotkey Management**: Use the functionality to assign meaningful names to your hotkeys for easier identification in logs and visualizations.

## Contributing

[Guidelines for contributing to BTminer_tracker]

## Support

[Instructions on how to report issues or seek help]

## License

[License information or statement]

## Additional Information

[Any other relevant information or links]