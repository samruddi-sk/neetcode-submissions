class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        min_heap = []
        counter = 0

        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next