import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequencies
        count = Counter(tasks)

        # Convert it into max heap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Calculate number of cycles
        time = 0
        q = deque()

        while q or maxHeap:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # we increase the negative value by 1 to reduce the respective postive value
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time



