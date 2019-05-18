# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def helper(self, matrix, start, res):
        row, col = len(matrix), len(matrix[0])
        if start * 2  >= row or start * 2 >= col:
            return res
        
        i, j = start, start
        
        
        for j in range(start, col-start):
            res.append(matrix[i][j])
        # import pdb; pdb.set_trace()  

        for i in range(start+1, row-start):
            res.append(matrix[i][j])
        # import pdb; pdb.set_trace()  

        if j > start and i > start:
            while j > start:
                j -= 1
                res.append(matrix[i][j])
            # import pdb; pdb.set_trace()

            while i > start + 1:
                i -= 1
                res.append(matrix[i][j])
            # import pdb; pdb.set_trace()
        res = self.helper(matrix, start+1, res)
        return res
    
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return 
        res = []
        return self.helper(matrix, 0, res)
                
s = Solution()
# a = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# a = [[1]]
# a = [[1,2,3,4,5]]
# a = [[1,2],[3,4]]
print(s.printMatrix(a))
