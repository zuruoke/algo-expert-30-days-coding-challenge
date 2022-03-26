from typing import List


class Solution():
    def __init__(self, prices_list: List[int]) -> None:
        self.prices_list = prices_list
        self.buy_index: int = 0
        self.sell_index: int = 1
        self.maxProfit: int = 0

    def sliding_window(self):

        while (self.sell_index < len(self.prices_list)):
            if (self.prices_list[self.buy_index] > self.prices_list[self.sell_index]):
                self.buy_index = self.sell_index
            else:
                profit = self.prices_list[self.sell_index] - \
                    self.prices_list[self.buy_index]
                self.maxProfit = max(self.maxProfit, profit)
            self.sell_index += 1

        return self.maxProfit


list_prices = \
    [10, 3, 8, 5, 6, 4, 2]
solution_instance = Solution(prices_list=list_prices)

print(solution_instance.sliding_window())
