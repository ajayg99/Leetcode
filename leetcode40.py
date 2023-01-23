class Solution(object):
    def combinationSum2(self, candidates, target):
        output = []
        candidates.sort()
        def combination2(idx,target,ds):
            if target==0:
                dscopy = ds[:]
                output.append(dscopy)
                return
            for i in range(idx,len(candidates)):
                if target<candidates[i]:
                    break
                if i>idx and candidates[i-1]==candidates[i]:
                    continue
                ds.append(candidates[i])
                combination2(i+1,target-candidates[i],ds)
                ds.remove(candidates[i])
        combination2(0,target,[])
        return output
op1 = Solution()
print(op1.combinationSum([2,3,6,7],7))