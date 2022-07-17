import collections
from typing import List


class Solution():
    def is_sudoku_valid(self, board: List[List[str]]) -> bool:
        '''
        << initialize sets that will contain the unique elements >>
        << rows are the first elements outputted devoid of a nested loop >>
        '''

        cols = collections.defaultdict(set)  # sets for columns
        rows = collections.defaultdict(set)  # sets for rows
        squares = collections.defaultdict(set)  # sets for the 3 x 3 grid

        # r as row & c as column.

        for r in range(len(board)):
            for c in range(len(board)):

                # skip all elements that have a "." or empty element
                if board[r][c] == ".":
                    continue

                # to get the collection of a 3 x 3 grid -> r // 3, c // 3
                # all grids -> [0,0], [0,1], [0,2]
                #              [1,0], [1,1], [1,2]
                #              [2,0], [2,1], [2,2]
                # for example -> suppose were r = 5, c = 7
                # :=>  (5 // 3),(7 // 3) = (1,2) -> will belong to the [1,2] grid
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False

                rows[r] = board[r][c]
                cols[c] = board[r][c]
                squares[(r // 3, c // 3)] = board[r][c]

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "8", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                      "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

instance_solution = Solution()

print(instance_solution.is_sudoku_valid(board))
