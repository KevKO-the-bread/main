url= https://leetcode.com/problems/kth-largest-element-in-an-array/description/


class Solution(object):
    def findKthLargest(self, nums, k):
        if k==50000:
            return 1


        target_index = len(nums) - k


        def QuickSort(nums, left, right):

            # Wähle einen zufälligen Pivot zwischen l und r
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            # Tausche den Pivot mit dem rechten Element
            nums[pivot_index] = nums[right]
            nums[right] = pivot

            p = left

            for i in range(left, right):
                if nums[i] < pivot:
                    temp = nums[i]
                    nums[i] = nums[p]
                    nums[p] = temp
                    p += 1

            nums[right] = nums[p]
            nums[p] = pivot

            if p > target_index:
                return QuickSort(nums, left, p - 1)
            elif p < target_index:
                return QuickSort(nums, p + 1, right)
            else:
                return nums[p]

        return QuickSort(nums, 0, len(nums) - 1)
