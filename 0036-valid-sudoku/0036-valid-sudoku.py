class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        box = defaultdict(list)

        # check columns
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                # check rows
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].append(board[i][j])
                
                # check columns
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].append(board[i][j])

                # check boxes
                key = ( i // 3, j // 3 )
                if board[i][j] in box[key]:
                    return False
                else:
                    box[key].append(board[i][j])

        return True