class Stack:
    def __init__(self):
        self.stack = []
        self.start = 0
        self.end = 0

    def __str__(self):
        ans = ""

        for obj in self.stack:
            ans += str(obj) + ","

        return ans[0:-1]
    
    def push(self, obj, idx):
        if self.stack == []:
            self.start = idx 

        self.stack.append(obj)

    def pop(self, obj, idx):
        self.stack.reverse()
        self.stack.remove(obj)
        self.stack.reverse()

        if self.stack == []:
            self.end = idx

    def final_obj(self, obj, idx):
        ans = False

        if self.stack != [] and self.stack[-1] == obj:
            self.pop(obj, idx)
            ans = self.stack == []
        
        else:
            self.push(obj, idx)

        return ans
    
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
    def is_empty(self):
        return self.stack == []

