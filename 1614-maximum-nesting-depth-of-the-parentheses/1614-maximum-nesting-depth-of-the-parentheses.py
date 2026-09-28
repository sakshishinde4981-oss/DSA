class Solution:
    def maxDepth(self, s: str) -> int:
        dept = 0
        max_dept = 0

        for ch in s:
            if ch == '(':
                dept += 1
                max_dept = max(dept, max_dept)
            
            elif ch == ')':
                dept -= 1

        return max_dept