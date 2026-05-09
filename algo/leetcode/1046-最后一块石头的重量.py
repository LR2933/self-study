class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            y = heappop_max(stones)
            x = heappop_max(stones)
            if x !=  y:
                heappush_max(stones, y - x)
        if stones:
            return stones[0]
        else:
            return 0


