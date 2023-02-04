class Solution(object):
    def nextGreatestLetter(self, letters, target):
        s = 0
        e = len(letters)-1
        while s<=e:
            m = (s+e)//2
            if letters[m]>target:
                e = m-1
            elif letters[m]<target:
                s = m+1
            else:
                s = m+1
        return letters[s%len(letters)]