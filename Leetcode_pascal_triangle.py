class Solution:
    def generate(self, numRows: int):
        ans = []
        for i in range(numRows):
            ans.append([1]*(i+1))
        if numRows <= 2:
            return ans
        else:
            for i in range(2, numRows):
                for j in range(1, i):
                    ans[i][j] = ans[i-1][j]+ans[i-1][j-1]
            return ans
