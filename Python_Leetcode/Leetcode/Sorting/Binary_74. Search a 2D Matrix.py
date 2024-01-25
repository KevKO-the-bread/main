url=https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution(object):
    def searchMatrix(self, matrix, target):
        L,R=0,len(matrix)-1
    
        while L>=R:
            m=(L+R)//2
            if matrix[m[0]]>target:
                R=m-1
            elif matrix[m[-1]]<target:
                L=m+1
            else:
                targetList=matrix[m]
                L,R=0,len(targetList)-1
            
                while L>=R:
                    m=(L+R)//2
                    if  targetList[m]>target:
                        L=m+1
                    elif  targetList[m]<target:
                        R=m-1
                    else:
                        return True
        return False
