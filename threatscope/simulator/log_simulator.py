# simulator/logSimulator.py
import random
import datetime
import time
from logStrategy import BruteForceStrategy
from logFactory import LogStrategyFactory

# This module defines the LogSimulator class, which is responsible for running the simulation loop and writing formatted log entries to a file. The simulator uses the LogStrategyFactory to generate log entries based on different strategies, including various attack patterns and normal traffic. The _format_entry method formats the log data into a string that mimics real log entries, while the _generate_burst method simulates a burst of brute force login attempts from a single IP address.
class LogSimulator:
    """
    Responsible for one thing only:
    running the simulation loop and writing formatted entries to file.
    """

# Initialize the simulator with the log file path
    def __init__(self, log_file: str):
        self.log_file = log_file

    # Main simulation loop
    def _format_entry(self, data: dict) -> str:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return (
            f"[{timestamp}] "
            f"{data['ip']} — "
            f"{data['message']} | "
            f"STATUS: {data['status']} | "
            f"TYPE: {data['threat_type']}\n"
        )

    # Simulate a burst of brute force login attempts from a single IP address
    def _generate_burst(self) -> list:
        strategy = BruteForceStrategy()
        ip = random.choice(BruteForceStrategy.ATTACKER_IPS)
        burst = [] # list to hold the generated log entries for the burst

        for _ in range(random.randint(10, 30)):
            data = strategy.generate()
            data["ip"] = ip
            burst.append(self._format_entry(data)) # adding the formatted log entry to the burst list

        return burst
    def run(self):
        with open(self.log_file, "a") as f:
            while True:
                # Generate a burst of brute force login attempts
                burst = self._generate_burst()
                for entry in burst:
                    f.write(entry) # write the log entry to the file
                    f.flush() # flush the file buffer to ensure the entry is written immediately
                    time.sleep(0.7)
                                        