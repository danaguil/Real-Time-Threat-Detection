# simulator/log_gen.py
# This is the main entry point for the log generation process. It initializes the LogSimulator with the specified log file and starts the simulation loop. The simulator will continuously generate log entries based on different strategies, simulating both normal traffic and various attack patterns, and write them to the specified log file in a formatted manner.
'''
Road Map"
logFactory.py — Factory for generating log entries based on different strategies, including various attack patterns and normal traffic. 
    The factory uses a weighted random selection to simulate realistic log generation, where normal traffic is more common than attacks.
logStrategy.py — Defines different log generation strategies for various attack types and normal traffic. This allows us to easily extend
     our log generator with new attack patterns in the future without modifying existing code.
logSimulator.py — Responsible for running the simulation loop and writing formatted entries to file. The simulator uses the LogStrategyFactory 
    to generate log entries
'''
from threatscope.simulator.logSimulator import LogSimulator

if __name__ == "__main__":
    simulator = LogSimulator("simulated_logs.log")
    simulator.run()