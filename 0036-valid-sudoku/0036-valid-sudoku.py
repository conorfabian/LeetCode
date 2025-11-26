class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                    
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])

                box = (i // 3, j // 3)
                if board[i][j] in cols[box]:
                    return False
                cols[box].add(board[i][j])

        return True