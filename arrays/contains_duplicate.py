# Problem: Contains Duplicate
# Difficulty: Easy
# Approach: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False