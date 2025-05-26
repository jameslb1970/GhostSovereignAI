# task_queue.py - Handles Ghost Sovereign AI's task queueing and execution

import queue

class GhostTaskQueue:
    def __init__(self):
        self.tasks = queue.Queue()

    def add_task(self, task):
        self.tasks.put(task)
        print(f"[TASK QUEUE] Task added: {task}")

    def get_task(self):
        if not self.tasks.empty():
            task = self.tasks.get()
            print(f"[TASK QUEUE] Task retrieved: {task}")
            return task
        return None

    def is_empty(self):
        return self.tasks.empty()
