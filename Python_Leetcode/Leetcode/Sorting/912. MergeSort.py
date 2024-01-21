url=https://leetcode.com/problems/sort-an-array/
class Solution(object):
    def sortArray(self, nums):
    

        def merge(arr, s, m, e):
            i,j,k=0,0,s
            L=arr[s:m+1]
            R=arr[m+1:e+1]

            while i<len(L) and j<len(R):
                if L[i]<=R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1
    
            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
        def mergeSort(arr, s ,e):
            if e<=s:
                return arr
    
            m=(s+e)//2
            mergeSort(arr, s, m)
            mergeSort(arr, m+1, e)
            merge(arr,s,m,e)
            return arr
        return mergeSort(nums,0, len(nums)-1)
      
