
class Solution():
    def __init__(self) -> None:
        self.memo = {}

    def climbing_stairs(self, n: int):
        if (n == 0):
            return 1
        if (n < 0):
            return 0
        if (n in self.memo):
            return self.memo[n]
        self.memo[n] = self.climbing_stairs(
            n - 1) + self.climbing_stairs(n - 2)
        return self.memo[n]


n = 45
instance_solution = Solution()

print(instance_solution.climbing_stairs(n=n))
