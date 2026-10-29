class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following.get(userId, set()) | {userId}
        feed = []

        for uid in users:
            for timestamp, tweetId in self.tweets.get(uid, []):
                feed.append((timestamp, tweetId))

        feed.sort(reverse=True)

        return [tweetId for timestamp, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)