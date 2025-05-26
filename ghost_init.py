# ghost_init.py - Ghost Sovereign AI Entry Point

import time
import threading
from ghost_modules.memory import GhostMemory
from ghost_modules.log import GhostLogger
from ghost_modules.core import GhostCore
from ghost_modules.update import GhostUpdater

class GhostSovereignAI:
    def __init__(self):
        self.logger = GhostLogger()
        self.memory = GhostMemory()
        self.core = GhostCore(self.memory, self.logger)
        self.updater = GhostUpdater(self.memory, self.logger)

    def start(self):
        self.logger.log("Ghost Sovereign AI Booting...")
        self.core.initialize()
        self.memory.load()
        threading.Thread(target=self._background_tasks).start()
        self.logger.log("Ghost Sovereign AI is now live.")

    def _background_tasks(self):
        while True:
            self.logger.log("Running scheduled tasks...")
            self.core.run_operations()
            self.updater.check_for_updates()
            time.sleep(5)

if __name__ == "__main__":
    ghost = GhostSovereignAI()
    ghost.start()
