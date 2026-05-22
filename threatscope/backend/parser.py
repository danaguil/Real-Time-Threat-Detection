'''
    Regex, turns raw lines into dictions
    {
        EXAMPLE:
        "timestamp": "2026-05-20 14:32:01",
        "ip":        "45.33.32.156",
        "message":   "Failed SSH login for user: admin",
        "status":    "FAILURE",
        "type":      "brute_force"
    }
'''

import re

class LogParser:
    def parse(self, log_line: str) -> dict:
        pattern = re.compile(
            r"\[(?P<timestamp>.*?)\]\s+"
            r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+—\s+"
            r"(?P<message>.*?)\s+\|\s+"
            r"STATUS:\s+(?P<status>.*?)\s+\|\s+"
            r"TYPE:\s+(?P<threat_type>.*)"
        )
        match = pattern.match(log_line)

        return match.groupdict()