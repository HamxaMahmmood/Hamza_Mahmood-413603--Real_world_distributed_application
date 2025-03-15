class VectorClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = {}

    def increment(self):
        self.clock[self.process_id] = self.clock.get(self.process_id, 0) + 1

    def update(self, received_clock):
        for pid, timestamp in received_clock.items():
            self.clock[pid] = max(self.clock.get(pid, 0), timestamp)

    def get_clock(self):
        return self.clock
