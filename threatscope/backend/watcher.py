'''
    Will monitor the log file for new entries in real time
        and will be sent to parser.py for processing.
'''

# read simulate_logs.log, using generator to get that real time data

import time

class LogWatcher:
    def watch(self, log_file: str):
        with open(log_file, "r") as f:
            while True: # infinite loop to continuously watch the log file for new entries
                # Move the cursor to the end of the file
                lines = f.readlines()
                for line in lines:
                    yield line.strip()
        return lines

# Testing using main
if __name__ == "__main__":
    # connecting to simulated logs
    watcher = LogWatcher()
    for log_entry in watcher.watch("simulated_logs.log"):
        print(log_entry)