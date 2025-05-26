# memory.py - Temporary Memory System for Ghost Sovereign AI

class GhostMemory:
    def __init__(self):
        self._memory_store = {}

    def store(self, key, value):
        self._memory_store[key] = value

    def retrieve(self, key):
        return self._memory_store.get(key, None)

    def clear(self):
        self._memory_store.clear()

    def all(self):
        return self._memory_store
