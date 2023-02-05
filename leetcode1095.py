class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        length = mountain_arr.length()-1
        def peak():
            s = 0
            e = length
            while s<e:
                m = (s+e)/2
                if mountain_arr.get(m)<mountain_arr.get(m+1):
                   s = m+1 
                else:
                    e = m
            return s
        def left():
            s = 0
            e = limit
            while s<=e:
                m = (s+e)//2
                if mountain_arr.get(m)==target: 
                    return m
                elif mountain_arr.get(m)>target:
                    e = m-1
                else:
                    s = m+1
            return -1
        def right():
            s = 0
            e = length
            while s<=e:
                m = (s+e)//2
                if mountain_arr.get(m)==target:
                    return m
                elif mountain_arr.get(m)>target:
                    s = m+1
                else:
                    e = m-1
            return -1
        limit = peak()
        op = left()
        if op>-1:
            return op
        return right()