from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:        
        return combinations([x + 1 for x in range(n)], k)