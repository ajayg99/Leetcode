class Solution(object):
    def singleNonDuplicate(self, nums):
        def bin():
            s = 0
            e = len(nums)-1
            while s<e:
                m = (s+e)//2
                if ((m%2==0 and nums[m]==nums[m-1]) or (m%2!=0 and nums[m]==nums[m+1])):
                    e = m-1
                elif ((m%2==0 and nums[m]==nums[m+1]) or (m%2!=0 and nums[m]==nums[m-1])):         
                    s = m+1
                else:
                    return nums[m]
            return nums[s]
        return bin()
    #optimized
    def singleNonDuplicate(self, nums):
        def bin(nums):
            s = 0
            e = len(nums)-2
            while s<=e:
                m = (s+e)//2
                if nums[m]==nums[m^1]:      
                    s = m+1
                else:
                    e=m-1
            return nums[s]
        return bin(nums)