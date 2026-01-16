# Link: https://leetcode.com/problems/contains-duplicate/description/


"""Problem Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques=set()
        for i in range(len(nums)):
            if (nums[i] in uniques):
                return True
            uniques.add(nums[i])
        return False
