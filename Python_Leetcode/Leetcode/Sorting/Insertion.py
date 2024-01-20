liste=[4,5,7,1,2,3,9,8,4,2,4]
def insertion(nums):
    for i in range(len(nums)):
        j=i-1
        while j>=0 and nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
            j-=1
    return nums

print(insertion(liste))
