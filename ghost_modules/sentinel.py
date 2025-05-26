# sentinel.py - Ghost Sovereign AI Sentinel Logic Layer

class GhostSentinel:
    def __init__(self):
        self.rules = {
            "user_login": "log",
            "error_log": "alert",
            "file_change": "log",
            "network_ping": "ignore",
        }

    def evaluate(self, event):
        action = self.rules.get(event, "ignore")
        print(f"[SENTINEL] Event '{event}' evaluated. Action: {action}")
        return action

    def add_rule(self, event, action):
        self.rules[event] = action
        print(f"[SENTINEL] New rule added: {event} -> {action}")
