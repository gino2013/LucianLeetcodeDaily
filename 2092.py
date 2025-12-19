from typing import List
from collections import defaultdict, deque


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Initially, person 0 and firstPerson have the secret
        has_secret = {0, firstPerson}

        # Group meetings by time
        meetings_by_time = defaultdict(list)
        for x, y, time in meetings:
            meetings_by_time[time].append((x, y))

        # Process meetings in chronological order
        for time in sorted(meetings_by_time.keys()):
            # Build a graph for meetings at this time
            graph = defaultdict(list)
            people_at_meetings = set()

            for x, y in meetings_by_time[time]:
                graph[x].append(y)
                graph[y].append(x)
                people_at_meetings.add(x)
                people_at_meetings.add(y)

            # Find all people who have the secret at this time
            # and can attend meetings
            queue = deque()
            for person in people_at_meetings:
                if person in has_secret:
                    queue.append(person)

            # BFS to propagate the secret within this time frame
            newly_informed = set()
            while queue:
                person = queue.popleft()
                if person in newly_informed:
                    continue
                newly_informed.add(person)

                for neighbor in graph[person]:
                    if neighbor not in newly_informed and neighbor not in has_secret:
                        queue.append(neighbor)

            # Update has_secret with newly informed people
            has_secret.update(newly_informed)

        return sorted(has_secret)
