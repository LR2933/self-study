class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapify_max(nums)
        ans = 0
        for _ in range(k):
            max_num = heappop_max(nums)
            ans += max_num
            heappush_max(nums, ceil(max_num / 3))
        return ans
