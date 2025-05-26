# comms.py - Communications Core for Ghost Sovereign AI

class GhostComms:
    def __init__(self):
        self.transcript = []

    def speak(self, message):
        print(f"[GHOST] {message}")
        self.transcript.append(("OUT", message))

    def listen(self, input_message):
        print(f"[INPUT] {input_message}")
        self.transcript.append(("IN", input_message))

    def get_transcript(self):
        return self.transcript

    def escalate(self, level, reason):
        print(f"[COMMS] Escalation Level {level} triggered - Reason: {reason}")
        self.transcript.append(("ESCALATE", f"Level {level} - {reason}"))
