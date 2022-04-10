class Solution():
    def common_longest_subsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for col in range(len(text2) + 1)]
              for row in range(len(text1) + 1)]

        for row in range(len(text1) - 1, -1, -1):
            for col in range(len(text2) - 1, -1, -1):
                if (text1[row] == text2[col]):
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]


text1 = "abcftykdsuyewsa"
text2 = "aceydueydggs"

instace_solution = Solution()

print(instace_solution.common_longest_subsequence(text1=text1, text2=text2))
