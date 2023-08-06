class Solution: 
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        answer = ['' for _ in range(numRows)]
        d = 1  # forward
        curr = 0
        for sub in s:
            answer[curr] += sub
            if d:
                curr += 1
            else:
                curr -= 1
            if curr == 0:
                d = 1
            elif curr == numRows - 1:
                d = 0
            
        return ''.join(answer)