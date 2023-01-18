class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        op = sum(nums[:3])   #storing the sum of initial 3 values as the output 
        for i in range(0,len(nums)-2): #nums-2 because of l and r pointers
            l = i+1
            r = len(nums)-1
            while l<r:
                sums = nums[i] + nums[r] + nums[l]
                if abs(sums-target)<abs(op-target):
                    op = sums
                if sums>target:
                    r-=1
                elif sums<target:
                    l+=1
                else:
                    return sums
        return op
out = Solution()
print(out.threeSumClosest([-1,2,1,-4],1))