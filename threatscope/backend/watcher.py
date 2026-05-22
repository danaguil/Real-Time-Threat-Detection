'''
    Will monitor the log file for new entries in real time
        and will be sent to parser.py for processing.
    Open simulated_logs.log
    Jump to the end of the file
    Sit in a loop waiting for new lines to appear
    The moment a new line is written, grab it and pass it forward
'''

# read simulate_logs.log, using generator to get that real time data

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