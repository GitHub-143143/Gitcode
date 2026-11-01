class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]],count=0) -> bool:
        if mat == target:
            return True
        if count == 3:
            return False
        for i in range(len(mat)):
            for j in range(i+1, len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        mat.reverse()
        return self.findRotation(mat, target, count+1)