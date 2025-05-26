# executor.py - Ghost Sovereign AI Executor Core

import subprocess

class Executor:
    def __init__(self, logger=None):
        self.logger = logger

    def run_command(self, command):
        if self.logger:
            self.logger.log(f"Executing command: {command}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.strip()
            error = result.stderr.strip()
            if result.returncode == 0:
                if self.logger:
                    self.logger.log(f"Command output: {output}")
                return output
            else:
                if self.logger:
                    self.logger.log(f"Command failed: {error}")
                return f"Error: {error}"
        except Exception as e:
            if self.logger:
                self.logger.log(f"Execution error: {e}")
            return f"Exception: {str(e)}"
