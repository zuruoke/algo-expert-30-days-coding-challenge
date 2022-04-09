from math import remainder
from typing import Any, Dict, List
from unittest import result


class Solution():
    def __init__(self) -> None:
        self.memo: Dict = {}

    def coin_change(self, coins: List[int], amount: int):
        result = self.evaluate_prob(coins, amount)
        print(result)
        if (result == None):
            return -1
        return len(result)

    def evaluate_prob(self, coins: List[int], amount: int):

        # check if it is memo
        if (amount in self.memo):
            return self.memo[amount]

        # declare all base cases
        if (amount == 0):
            return []
        if (amount < 0):
            return None

        shortestCombination = None

        for coin in coins:
            remainder: int = amount - coin
            remainderCombination = self.evaluate_prob(
                coins=coins, amount=remainder)
            if (remainderCombination != None):
                combination = [*remainderCombination, coin]
                if ((shortestCombination == None) or (len(shortestCombination) > len(combination))):
                    shortestCombination = combination
            self.memo[amount] = shortestCombination

        return shortestCombination


instance_solution = Solution()
print(instance_solution.coin_change([186, 419, 83, 408], 6249))
