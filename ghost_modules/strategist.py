# strategist.py - Ghost Sovereign AI Strategic Planning Unit

import time

class GhostStrategist:
    def __init__(self):
        self.current_goal = None
        self.history = []

    def set_goal(self, goal):
        self.current_goal = goal
        self.history.append((time.time(), f"Set goal: {goal}"))
        print(f"[STRATEGIST] New goal set: {goal}")

    def review_goals(self):
        print("[STRATEGIST] Reviewing strategic goals:")
        for entry in self.history:
            timestamp, note = entry
            print(f"  • {time.ctime(timestamp)} - {note}")

    def evaluate_path(self):
        if self.current_goal:
            print(f"[STRATEGIST] Evaluating strategy toward: {self.current_goal}")
            return True
        else:
            print("[STRATEGIST] No active goal to evaluate.")
            return False
