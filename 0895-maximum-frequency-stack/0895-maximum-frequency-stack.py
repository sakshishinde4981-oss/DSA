class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1

        f = self.freq[val]
        if f not in self.group:
            self.group[f] = []

        self.group[f].append(val)

        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        stack = self.group[self.max_freq]

        val = stack.pop()

        self.freq[val] -= 1
        
        if not stack:
            self.max_freq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()