class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:  # LCS에 속하면
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])    # 여태까지 LCS에 속한 값 + s1스트링 현재 값 더함.
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 여태까지 LCS에 속한 값 중 max값 (나중에 뺄 값이어서 max)
        ascii_sum_str1 = sum(ord(c) for c in s1)
        ascii_sum_str2 = sum(ord(c) for c in s2)
        min_ascii_sum = ascii_sum_str1 + ascii_sum_str2 - 2 * dp[m][n]

        return min_ascii_sum