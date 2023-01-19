class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        output = []
        for i in range(0,len(nums)-3):
            if i>0 and nums[i]==nums[i-1]: #condition to avoid duplicates
                continue
            for j in range(i+1,len(nums)-2):
                if j!=i+1 and nums[j]==nums[j-1]: #j cant be i+1 since is j=i+1, when j gets away from i and its prev element is dup;icate continue
                    continue
                l = j+1              #rest same as 3sum
                r = len(nums)-1
                while l<r:
                    sums = nums[i] +nums[j]+nums[l] +nums[r]
                    if sums<target:
                        l+=1
                    elif sums>target:
                        r-=1
                    else:
                        output.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1


        return output
op1 = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(op1.fourSum(nums, target))