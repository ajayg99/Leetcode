class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        s = 0
        e = len(nums1)-1  
        iseven = False
        length1 = len(nums1)
        length2 = len(nums2)
        length = length1+length2
        half = length//2
        if length%2==0:
            iseven=True
        while True:
            m1 = (s+e)//2
            m2 = half-m1-2
            num1L = nums1[m1] if m1>=0 else -10**6
            num1R =  nums1[m1+1] if (m1+1)<length1 else 10**6
            num2L = nums2[m2] if m2>=0 else -10**6
            num2R =  nums2[m2+1] if (m2+1)<length2 else 10**6
            if num1L <= num2R and num2L <= num1R:
                if iseven:
                    temp = float(max(num1L,num2L)+min(num1R,num2R))
                    return temp/2
                else:
                    return min(num1R,num2R)
            elif num1L>num2R:
                e = m1-1
            else:
                s = m1+1