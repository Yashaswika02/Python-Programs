#LEETCODE-1342:
##class Solution(object):
##    def numberOfSteps(n):
##        c=0
##        while (n>0):
##            if n%2==0:
##                n=n//2
##            else:
##                n=n-1
##            c+=1
##        print(c)
##
##
##Solution().numberOfSteps(8)

#LEETCODE-231:
##class Solution(object):
##    def isPowerOfTwo(self, n):
##        x = 0
##        while pow(2, x) <= n:
##            if n == pow(2, x):
##                return True
##            x += 1
##
##        return False
##
##print(Solution().isPowerOfTwo(16))

#LEETCODE-283:
##class Solution(object):
##    def moveZeroes(self, nums):
##        count=nums.count(0)
##        for i in range(count):
##            nums.remove(0)
##            nums.append(0)
##        return nums
##Solution().moveZeroes([0,1,0,3,12])



        




































































       
        
       
