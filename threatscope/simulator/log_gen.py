# simulator/log_gen.py
from log_simulator import LogSimulator

if __name__ == "__main__":
    simulator = LogSimulator("simulated_logs.log")
    simulator.run()