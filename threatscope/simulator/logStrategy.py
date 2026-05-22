# Design Pattern: Strategy Pattern
# Context is going to define the interface of interest to clients and maintains a reference to a strategy object.

from abc import ABC, abstractmethod
import random

class LogStrategy(ABC):
    @abstractmethod
    def generate_log_entry(self) -> dict:
        pass

class BruteForceStrategy(LogStrategy):
    ATTACKER_IPS = ["192.168.1.100", "10.0.0.50", "172.16.0.25"]
    
    def generate_log_entry(self) -> dict:
        return {
            "ip": random.choice(self.ATTACKER_IPS),
            "message": f"Failed SSH login for user: {random.choice(['admin', 'root'])}",
            "status": "FAILURE",
            "threat_type": "brute_force"
        }

class SQLInjectionStrategy(LogStrategy):
    ATTACKER_IPS = ["203.0.113.17", "91.108.4.77"]
    PAYLOADS = ["' OR 1=1--", "'; DROP TABLE users;--"]

    def generate_log_entry(self) -> dict:
        return {
            "ip": random.choice(self.ATTACKER_IPS),
            "message": f"SQL injection attempt: {random.choice(self.PAYLOADS)}",
            "status": "BLOCKED",
            "threat_type": "sql_injection"
        }

class NormalTrafficStrategy(LogStrategy):
    NORMAL_IPS = [f"192.168.1.{i}" for i in range(1, 20)]
    ENDPOINTS = ["/home", "/dashboard", "/api/data"]

    def generate_log_entry(self) -> dict:
        return {
            "ip": random.choice(self.NORMAL_IPS),
            "message": f"GET {random.choice(self.ENDPOINTS)} HTTP/1.1",
            "status": "200 OK",
            "threat_type": "normal"
        }