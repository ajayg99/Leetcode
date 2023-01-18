#brute force
class Solution(object):
    def swap(self,nums,a,b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
    def quick(self,nums,lo,hi): #sorting the array to avoid duplicates keeping track of prev elements
        if lo>=hi:
            return 
        s = lo
        e = hi
        m = int((s+e)/2)
        p = nums[m]
        while s<=e:
            while nums[s]< p:
                s+=1
            while nums[e]>p:
                e-=1
            if s<=e:
                self.swap(nums,s,e)
                s+=1
                e-=1
        self.quick(nums,lo,e)
        self.quick(nums,s,hi)
        return nums
    def threeSum(self, nums):        
        output = []
        prev,prevj = 100,100            #intital fake values for the prev
        nums = self.quick(nums,0,len(nums)-1)
        for i in range(0,len(nums)-2):          #3 loops for each element
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if (nums[i]+nums[j]+nums[k]==0) and (nums[i]!=prev) and(prevj != nums[j]):
                        output.append([nums[i],nums[j],nums[k]])
                        break     #when the answer is found break the k loop since only one possible value for k if i and j are found for eg:(if i=0 and j=-1, k can be only -1)
                prevj = nums[j]
            prev = nums[i]
        return output

#optimized
    def opthreeSum(self, nums):
        nums.sort()
        output = []
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return output
p1 = Solution()
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(p1.threeSum(nums))
print(p1.opthreeSum(nums))
