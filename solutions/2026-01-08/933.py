from collections import deque

class RecentCounter:
    def __init__(self):
        """
        Initialize the RecentCounter with an empty queue to store request timestamps.
        """
        self.requests = deque()

    def ping(self, t: int) -> int:
        """
        Add a new request at time t and return the count of requests
        in the range [t - 3000, t].

        Args:
            t: Current time in milliseconds (strictly increasing)

        Returns:
            Number of requests in the past 3000 milliseconds
        """
        # Add the new request timestamp
        self.requests.append(t)

        # Remove all requests older than t - 3000
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the count of requests in the valid time range
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
