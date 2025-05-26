# logger.py - Activity Logger for Ghost Sovereign AI

import time

class GhostLogger:
    def __init__(self, log_to_console=True):
        self.log_to_console = log_to_console
        self.logs = []

    def log(self, message, level="INFO"):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(entry)
        if self.log_to_console:
            print(entry)

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs = []
