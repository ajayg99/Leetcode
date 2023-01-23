class Solution(object):
    def generateParenthesis(self, n):
        output = []
        def parenthesis(counto,countc,n,ds):
            if n==counto==countc:
                output.append("".join(ds))
                return
            if counto<n:
                ds.append("(")
                parenthesis(counto+1,countc,n,ds)
                ds.pop()
            if countc<counto and countc<n:
                ds.append(")")
                parenthesis(counto,countc+1,n,ds)
                ds.pop()
            return
        parenthesis(0,0,n,[])
        return output
op1 = Solution()
op = op1.generateParenthesis(5)
print(op)

