# operations.py - Core Operations Hub for Ghost Sovereign AI

from ghost_modules.heartbeat import Heartbeat
from ghost_modules.logger import GhostLogger
from ghost_modules.strategist import GhostStrategist
from ghost_modules.comms import GhostComms

class GhostOperations:
    def __init__(self):
        self.heartbeat = Heartbeat()
        self.logger = GhostLogger()
        self.strategist = GhostStrategist()
        self.comms = GhostComms()
        self.modules = {
            "heartbeat": self.heartbeat,
            "logger": self.logger,
            "strategist": self.strategist,
            "comms": self.comms
        }

    def run_cycle(self):
        self.logger.log("Running core operational cycle.")
        self.heartbeat.beat()
        self.comms.speak("Operational cycle complete.")
        self.strategist.analyze("New data")
        self.strategist.evaluate_objectives()
        self.logger.log("Cycle complete.")

    def report_status(self):
        print("=== GHOST STATUS ===")
        for name, mod in self.modules.items():
            print(f"{name.upper()}: {mod.__class__.__name__}")
        print("====================")
