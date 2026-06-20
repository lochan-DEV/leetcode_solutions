# Problem: Two Sum (LeetCode #1)
# Difficulty: Easy
# Topic: Arrays

# Approach:
# Check every pair of elements
# If sum equals target → return indices

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
