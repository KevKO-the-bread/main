list1=[2, 1, 5, 3]

target=4
#Brute_Force

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        summe=list1[j]+list1[i]
        if summe==target:
            print(i,j)
            
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                summe=nums[j]+nums[i]
                if summe==target:
                    return i,j
                
#Smart

class Solution(object):
    def twoSum(self, nums, target):
        prevMap={} #val: index
        for i in range(len(nums)): #enumerate
            diff=target-nums[i]    #if element double then prevMap hier einfügen 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[1]]= i   #storeValue in prevMap
