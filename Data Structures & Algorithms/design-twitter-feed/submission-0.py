class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> [count, tweetId]
        self.followMap = defaultdict(set) # userId -> followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    # Don't understand this part of the code yet
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:    
            self.followMap[followerId].remove(followeeId)
        
