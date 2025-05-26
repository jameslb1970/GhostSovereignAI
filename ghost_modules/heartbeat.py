# heartbeat.py - Ghost Sovereign AI Heartbeat Manager

import time
import threading

class Heartbeat:
    def __init__(self, interval=10, logger=None):
        self.interval = interval
        self.logger = logger
        self.running = False
        self.thread = None
        self.tick_count = 0

    def _pulse(self):
        while self.running:
            self.tick_count += 1
            if self.logger:
                self.logger.log(f"Heartbeat tick #{self.tick_count}")
            # Ghost can plug in routines here later (e.g., check status, scan for tasks)
            time.sleep(self.interval)

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._pulse, daemon=True)
            self.thread.start()
            if self.logger:
                self.logger.log("Heartbeat started.")

    def stop(self):
        self.running = False
        if self.logger:
            self.logger.log("Heartbeat stopped.")
