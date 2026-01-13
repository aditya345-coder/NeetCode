# Link: https://leetcode.com/problems/concatenation-of-array/description/

"""Problem Description:
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

## Solution:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

## Alternate Solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)*2
        j=0
        for i in range(0, len(nums)):
            ans[j]=nums[i]
            j+=1

        for i in range(0, len(nums)):
            ans[j]=nums[i]
            j+=1
        return ans
