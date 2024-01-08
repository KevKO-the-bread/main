url= https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        self.curr = ListNode(homepage)

    def visit(self, url):
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps):
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps):
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

/Stack

class BrowserHistory(object):
    def __init__(self, homepage):
        self.i=0
        self.len=1
        self.history=[homepage]
        

    def visit(self, url):

        if len(self.history)<self.i+2:
            self.history.append(url)
        else:
            self.history[self.i+1]= url
        self.i+=1
        self.len=self.i+1
        

    def back(self, steps):
        self.i=max(self.i-steps, 0)
        return self.history[self.i]
        
        

    def forward(self, steps):
        self.i=min(self.i+steps, self.len-1)
        return self.history[self.i]
