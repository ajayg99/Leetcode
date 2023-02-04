class Solution(object):
    def searchRange(self, nums, target):
        def binl():
            s = 0
            e = len(nums)-1
            ans = -1
            while s<=e:
                m = (s+e)//2
                if nums[m]<target:
                    s = m+1
                elif nums[m]>target:
                    e = m -1 
                else:
                    ans = m
                    e = m-1
            return ans
        def binr():
            s = 0
            e = len(nums)-1
            ans = -1
            while s<=e:
                m = (s+e)//2

                if nums[m]<target:
                    s = m+1
                elif nums[m]>target:
                    e = m -1 
                else:
                    ans = m
                    s = m+1   
            return ans
        return [binl(),binr()]