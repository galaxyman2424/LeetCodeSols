class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rrnum = len(matrix) - 1
        lrnum = 0
        
        rcnum = len(matrix[0]) - 1
        lcnum = 0

        while lrnum <= rrnum:
            rmid = (rrnum + lrnum) // 2
            print(lrnum, rmid, rrnum)
            if (matrix[rmid][rcnum] >= target and matrix[rmid][0] <= target) or lrnum == rrnum:
                break
            elif matrix[rmid][rcnum] > target:
                rrnum = rmid - 1
            elif matrix[rmid][0] < target:
                lrnum = rmid + 1
            print(lrnum, rmid, rrnum)

        print("FINDING COLUMN NUMBER")

        while lcnum <= rcnum:
            cmid = (rcnum + lcnum) // 2
            print(lcnum, cmid, lcnum)
            if matrix[rmid][cmid] == target:
                return True
            elif matrix[rmid][cmid] > target:
                rcnum = cmid - 1
            elif matrix[rmid][cmid] < target:
                lcnum = cmid + 1
            print(lcnum, cmid, lcnum)
        
        return False