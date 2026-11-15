# https://leetcode.com/problems/minimum-number-game/description/

class Solution(object):
    def numberGame(self, nums):
        a = sorted(nums)
        for i in range(0,len(a)-1,2):
            a[i],a[i+1] = a[i+1],a[i]
        return a