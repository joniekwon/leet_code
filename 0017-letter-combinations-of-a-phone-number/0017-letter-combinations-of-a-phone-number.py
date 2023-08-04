import string
class Solution:
    def letterCombinations(self, digits: str):
        alphabet = [string.ascii_lowercase[3*i:(3*i+3)] for i in range(5)] + ['pqrs', 'tuv', 'wxyz']
        alphabet = {str(i):x for i, x in enumerate(alphabet, start=2)}
        n = len(digits)
        answer = []
        def backtrack(i, curr):
            if i >= n:
                answer.append(curr)
                return
            for j in alphabet[digits[i]]:
                backtrack(i + 1, curr + j)
        if digits:
            backtrack(0, "")
        return answer