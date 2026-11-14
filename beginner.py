#https://leetcode.com/problems/find-if-digit-game-can-be-won/
class Solution(object):
    def canAliceWin(self, nums):
        a = 0
        b = 0
        for i in nums:
            if i<=9:
                a += i
            else:
                b += i
        if a==b:
            return False
        else:
            return True
