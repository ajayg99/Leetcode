class Solution(object):
    def combinationSum(self, candidates, target):
        output = []
        def combination(idx,target,ds):
            if idx==len(candidates):
                if target==0:
                    dscopy = ds[:]
                    output.append(dscopy)
                    return
                return
            if target>=candidates[idx]: # to reduce the number of recursion in stack, if removed causes stackoverflow
                ds.append(candidates[idx])
                combination(idx,target-candidates[idx],ds)
                ds.remove(candidates[idx])  #removed (backtrack)
            combination(idx+1,target,ds)# reason for not putting inside condition: needs to run if one of the output is found but idx has not reached max length
            return
        combination(0,target,[])
        return output
op1 = Solution()
print(op1.combinationSum([2,3,6,7],7))