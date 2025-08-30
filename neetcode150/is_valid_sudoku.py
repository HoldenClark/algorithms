#==========================================================================================
# https://neetcode.io/problems/valid-sudoku?list=neetcode150
#
# this problem asks us too check if any 3x3 square, row, or column contain duplicate \
# numbers within them. to check if there are any duplicates in those three categories \
# we have to check every value in the given board and check to see if it exists already \
# in a col, row, or 3x3 square. to keep track of what we have all checked we need to store \
# the previous values. we need to check against row, col, and 3x3 so we have separate \
# storage for each category. we index the rows and cols easily but for the board we index \
# by row // 3, col // 3 since each board has len 3 in either direction. we do the check in\
# the same way. if at any point we find a duplicate return false otherwise return true.
#==========================================================================================

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        hash_row = {key: [] for key in range(9)}
        hash_col = {key: [] for key in range(9)}
        hash_board = {(i, j): [] for i in range(3) for j in range(3)}
        
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    # check and add to row
                    if board[row][col] in hash_row[row]:
                        return False
                    else:
                        hash_row[row].append(board[row][col])

                    # check and add to col
                    if board[row][col] in hash_col[col]:
                        return False
                    else:
                        hash_col[col].append(board[row][col])

                    # check and add to board
                    if board[row][col] in hash_board[(row // 3), (col // 3)]:
                        return False
                    else:
                        hash_board[(row // 3), (col // 3)].append(board[row][col])

        return True
    
test_board_pass = [["1","2",".",".","3",".",".",".","."],
                   ["4",".",".","5",".",".",".",".","."],
                   [".","9","8",".",".",".",".",".","3"],
                   ["5",".",".",".","6",".",".",".","4"],
                   [".",".",".","8",".","3",".",".","5"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".",".",".",".",".",".","2",".","."],
                   [".",".",".","4","1","9",".",".","8"],
                   [".",".",".",".","8",".",".","7","9"]]

test_board_fail = [["1","2",".",".","3",".",".",".","."],
                   ["4",".",".","5",".",".",".",".","."],
                   [".","9","1",".",".",".",".",".","3"],
                   ["5",".",".",".","6",".",".",".","4"],
                   [".",".",".","8",".","3",".",".","5"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".",".",".",".",".",".","2",".","."],
                   [".",".",".","4","1","9",".",".","8"],
                   [".",".",".",".","8",".",".","7","9"]]

test = Solution()

print("should output true: ", test.isValidSudoku(test_board_pass))
print("should output false: ", test.isValidSudoku(test_board_fail))