'''
79. Word Search
Medium

2584

133

Add to List

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''
class Solution:

    def __init__(self):
        self.past_position = []
        self.len = 0
        self.high = 0

    def exist(self, board, word):
        self.len = len(board[0])-1
        self.high = len(board)-1

        start_position = []
        for row, n in enumerate(board):
            for col, m in enumerate(n):
                if m == word[0]:
                    start_position.append([row, col])

        A_flag = False

        for i in start_position:
            self.past_position = []
            A_flag = A_flag or self.aux_find_word(i, "", word, board)

        return A_flag

    def aux_find_word(self,current_position, current_word, word, board):
        flag = False
        current_word = current_word + board[current_position[0]][current_position[1]]

        if current_word != word[:len(current_word)]:
            return False

        if current_word == word:
            return True

        self.past_position.append(current_position)

        if current_position[0] - 1 >= 0:
            next_position = [current_position[0] - 1,current_position[1]]
            if next_position not in self.past_position:
                flag = flag or self.aux_find_word(next_position, current_word, word, board)

        if current_position[0] + 1 <= self.high:
            next_position = [current_position[0] + 1,current_position[1]]
            if next_position not in self.past_position:
                flag = flag or self.aux_find_word(next_position, current_word, word, board)

        if current_position[1] - 1 >= 0:
            next_position = [current_position[0],current_position[1] - 1]
            if next_position not in self.past_position:
                flag = flag or self.aux_find_word(next_position, current_word, word, board)

        if current_position[1] + 1 <= self.len:
            next_position = [current_position[0],current_position[1] + 1]
            if next_position not in self.past_position:
                flag = flag or self.aux_find_word(next_position, current_word, word, board)
        self.past_position.pop()
        return flag

class Solution1():

    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        if self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
              or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:]):
            return True
        board[i][j] = tmp
        return False

    def aux_exist(self, i, j, left_word, board):
        if len(left_word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        c_word = board[i][j]
        board[i][j] = '#'
        if self.aux_exist(i - 1, j, left_word[1:], board) or self.aux_exist(i + 1, j, left_word[1:],board) or self.aux_exist(i, j - 1,left_word[1:],board) or self.aux_exist(i, j + 1, left_word[1:], board):
            return True
        board[i][j] = c_word
        return False


class Solution2:

    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.aux_exist(i, j, word, board):
                    return True
        return False

    def aux_exist(self, i, j, left_word, board):
        if len(left_word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        c_word = board[i][j]
        board[i][j] = '#'
        if self.aux_exist(i - 1, j, left_word[1:], board) or self.aux_exist(i + 1, j, left_word[1:],board) or self.aux_exist(i, j - 1,left_word[1:],board) or self.aux_exist(i, j + 1, left_word[1:], board):
            return True
        board[i][j] = c_word
        return False

if __name__ == "__main__":
    solution = Solution2()
    board =[["A"]]
    word = "AB"

    print(solution.exist(board,word))