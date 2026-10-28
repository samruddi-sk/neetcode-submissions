class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = sorted(Counter(tasks).values())
        max_count = counts[-1]
        slots = (max_count - 1) * (n + 1)
        slots += counts.count(max_count)
        return max(len(tasks), slots)