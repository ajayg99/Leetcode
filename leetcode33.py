class Solution(object):
    def search(self, nums, target):
        def bin():
            s = 0
            e = len(nums)-1
            while s<=e:
                m = (s+e)//2
                if target == nums[m]:
                    return m
                elif (nums[s]<=nums[m]):
                    if ((nums[s]<=target<=nums[m]) ):
                        e = m-1
                    else:
                        s = m+1
                else:
                    if ((nums[m]<=target<=nums[e]) ):
                        s = m+1
                    else:
                        e = m-1

            return -1
        return bin()