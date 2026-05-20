"""
Building a log generator for the ThreatScope simulator
Generates fake server logs and writes them to a local file for the backend

1. Brute Force Login Attempts: attacker submitting many possible keys or passwords with the hope of eventually guessing correctly
"""

import random, datetime, time

'''
Looking into generating a realistic looking text so that our detection logic has something to analyze

E.g. a log entry might look like this:
Our simulator (fake "attacker") → writes fake logs → we analyze logs'
[2026-05-20 14:32:01] 45.33.32.156 — Failed SSH login for user: admin
'''

# creating arrays with both IPs of attacker and normal users
attacker_ips = ["192.168.1.100", "10.0.0.50", "172.16.0.25"]
normal_user_ips = ["192.168.1.50", "10.0.0.100", "172.16.0.50"]

# Event types with some common attack patterns and normal activities
def make_event_types():
    event_type = random.choice({
        "brute_force",
        "sql_injection",
        "port_scan",
        "normal_login",
        "normal_request"
    })

    # scenario-based event generation
    if event_type == "brute_force": # simulating a brute force attack
        ip_address = random.choice(attacker_ips) 
        user = random.choice(["admin", "root", "user"])
        message = f"Failed SSH login for user: {user}"
        status = "failure"
    elif event_type == "sql_injection": # simulating a SQL injection attack
        ip_address = random.choice(attacker_ips)
        
        # common SQL injection payloads; 
        # OR 1=1-- is a classic payload that always evaluates to true, allowing attackers to bypass authentication
        # drop table users; -- is a destructive payload that attempts to delete the users table from the database
        # union select * from users; -- is a payload that tries to extract data from the users
        
        payload = random.choice(["' OR 1=1--", "'; DROP TABLE users; --", "' UNION SELECT * FROM users; --"])
        message = f"SQL Injection attempt with payload: {payload}" # f-string to create a log message that includes the randomly selected SQL injection payload
        status = "BLOCKED" # indicating that the attack was blocked by the system
    # port scanning is a technique used by attackers to identify open ports and services on a target system, which can then be exploited for further attacks.
    elif event_type == "port_scan": # simulating a port scan attack. 
        ip_address = random.choice(attacker_ips)
        port = random.choice([22, 80, 443, 3306, 8080]) # common ports for SSH, HTTP, HTTPS, MySQL, and alternative HTTP
        message = f"Port scan detected on port: {port}" # f-string to create a log message that indicates a port scan was detected on a specific port
        status = "BLOCKED"
    elif event_type == "normal_login": # simulating a normal login attempt
        ip_address = random.choice(normal_user_ips)
        user = random.choice(["alice", "bob", "charlie"])
        message = f"Successful login for user: {user}"
        status = "SUCCESS"
    else:
        ip_address = random.choice(normal_user_ips)
        endpoint = random.choice(["/index.html", "/home", "/dashboard"])
        message = f"GET {endpoint} HTTP/1.1"
        status = "200 OK"
    return ip_address, message, status



# Function to generate a log entry
def generate_log_entry():
    # Simulate a log entry with random data
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address, event_type, status = make_event_types()
    return f"[{timestamp}] {ip_address} — {event_type} - {status}\n"
    

"""
To simulate a burst of brute force login attempts, we can create a function that 
    generates multiple log entries in quick succession, all originating from the 
    same IP address. This will mimic the behavior of an attacker trying to guess 
    passwords rapidly.
"""
def generate_brute_force_burst(ip=None):
    ip = ip or random.choice(attacker_ips)
    burst = [] # list to hold the generated log entries for the burst
    for _ in range(random.randint(10, 30)):  # 10–30 rapid failures
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = random.choice(["admin", "root"])
        entry = f"[{timestamp}] {ip} — Failed SSH login for user: {user} | STATUS: FAILURE\n"
        burst.append(entry) # adding the generated log entry to the burst list
    return burst

# Testing function
if __name__ == "__main__":
    print("Started log simulation...\n")
    # Generate a burst of brute force login attempts
    brute_force_logs = generate_brute_force_burst()
    for log in brute_force_logs:
        print(log, end="")
        time.sleep(.7)  # Simulate rapid log generation with a short delay
