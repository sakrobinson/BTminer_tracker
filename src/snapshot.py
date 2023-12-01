import os
import time
import bittensor as bt
import pandas as pd

def read_coldkey_address():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    file_path = os.path.join(script_dir, 'coldkey.txt')     # Path to the file
    with open(file_path, 'r') as file:
        return file.read().strip()

def fetch_data(subtensor, coldkey_address, block):
    # Retrieve the stake and neuron information here
    stake_info = subtensor.get_stake_info_for_coldkey(coldkey_ss58=coldkey_address, block=block)
    data = []

    if stake_info:
        for info in stake_info:
            neurons = subtensor.get_all_neurons_for_pubkey(hotkey_ss58=info.hotkey_ss58, block=block)
            for neuron in neurons:
                data_entry = {
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()),
                    'block': block,
                    'coldkey': coldkey_address,
                    'hotkey': neuron.hotkey,
                    'stake': neuron.stake,
                    'rank': neuron.rank,
                    'emission': neuron.emission
                    # Add more fields as needed
                }
                data.append(data_entry)
    return data

def append_to_log(data, filename):
    df = pd.DataFrame(data)
    if not df.empty:
        with open(filename, 'a') as file:
            df.to_csv(file, header=file.tell()==0, index=False)

def get_current_block_number(subtensor):
    try:
        current_block = subtensor.get_current_block()
        return current_block
    except Exception as e:
        print(f"Failed to get the current block number: {e}")
        return None

def main():
    config = bt.subtensor.config()
    config.subtensor.network = "local"
    config.subtensor.chain_endpoint = "ws://127.0.0.1:9944"
    sub = bt.subtensor(config=config)

    coldkey_address = read_coldkey_address()
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    filename = os.path.join(script_dir, 'hotkeys.log')  # Path to the log file

    last_reported_block = None
    report_every_n_blocks = 100

    while True:
        current_block = get_current_block_number(sub)
        if current_block is not None:
            if last_reported_block is None or current_block >= last_reported_block + report_every_n_blocks:
                data = fetch_data(sub, coldkey_address, current_block)
                append_to_log(data, filename)
                print(f"Snapshot taken at block {current_block} and written to {filename}")
                last_reported_block = current_block
        else:
            time.sleep(60)
            continue
        time.sleep(10)  # Adjust as needed for block timing

if __name__ == "__main__":
    main()
