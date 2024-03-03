class Heap:
    def __init__(self):
        self.heap=[0]
        
    def __str__(self):
        return "[" + ", ".join(map(str, self.heap[1:])) + "]"    
        
    def push(self, val):
        self.heap.append(val)
        i=len(self.heap)-1
    
        while self.heap[i]<self.heap[i//2]:
            temp=self.heap[i]
            self.heap[i]=self.heap[i//2]
            self.heap[i//2]=temp
            i=i//2
            
    def pop(self):
        if len(self.heap)==1:
            return None
        if len(self.heap)==2:
            return self.heap.pop()
        
        res=self.heap[1]
        self.heap[1]=self.heap.pop()
        i=1
        
        while 2*i<len(self.heap):
            if (2*i+1<len(self.heap) and
                self.heap[2*i]>self.heap[2*i+1] and
                self.heap[2*i+1]< self.heap[i]):
                
                temp=self.heap[2*i+1]
                self.heap[2*i+1]=self.heap[i]
                self.heap[i]=temp
                
            elif self.heap[2*i]< self.heap[i]:
                temp=self.heap[2*i]
                self.heap[2*i]=self.heap[i]
                self.heap[i]=temp
                
            else:
                break
        return res
