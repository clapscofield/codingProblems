"""
Leetcode Problem
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1

        while left < right:
            s = numbers[left] + numbers[right]
            if s > target: 
                right -= 1
            elif s < target:
                left += 1
            else:
                return [left+1, right+1]
            

        
