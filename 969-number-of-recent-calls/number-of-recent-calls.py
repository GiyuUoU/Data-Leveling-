from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:

        # Add current request
        self.queue.append(t)

        # Remove requests older than t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # Remaining requests are in [t - 3000, t]
        return len(self.queue)