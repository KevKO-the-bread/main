url=https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest(object):

    def __init__(self, k, nums):
        self.k, self.minHeap=k, nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
