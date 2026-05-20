"""
Building a log generator for the ThreatScope simulator
Generates fake server logs and writes them to a local file for the backend

1. Brute Force Login Attempts: attacker submitting many possible keys or passwords with the hope of eventually guessing correctly
"""

import random, datetime

'''
Looking into generating a realistic looking text so that our detection logic has something to analyze

E.g. a log entry might look like this:
Our simulator (fake "attacker") → writes fake logs → we analyze logs'
[2026-05-20 14:32:01] 45.33.32.156 — Failed SSH login for user: admin
'''
def generate_log_entry():
    # Simulate a log entry with random data
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    event_type = random.choice(["Failed SSH login", "GET /admin HTTP/1.1", "SQL: ' OR 1=1--'"])
    status = random.choice(["success", "failure"])
    
    log_entry = f"[{timestamp}] {ip_address} — {event_type.capitalize()} - {status}\n"
    return log_entry

# Testing function
if __name__ == "__main__":
    for _ in range(10):
        print(generate_log_entry())
