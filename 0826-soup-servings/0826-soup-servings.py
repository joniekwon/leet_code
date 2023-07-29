from functools import cache

class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dfs(a, b):
            if a <= 0: # 남은 a 수프가 없을 경우
                if b <= 0: # b와 동시에 먹은 경우
                    return 0.5
                else: 
                    return 1
            else:
                if b <= 0: # b를 먼저 먹은 경우
                    return 0
            return 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) +  dfs(a - 25, b - 75))
        return 1 if n > 4450 else dfs(n, n) # 4450이상은 1로 수렴