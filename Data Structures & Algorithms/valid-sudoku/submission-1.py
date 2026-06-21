class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        table = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col[i] or board[i][j] in row[j] or board[i][j] in table[(i//3,j//3)]:
                        return False
                    
                    col[i].add(board[i][j])
                    row[j].add(board[i][j])
                    table[(i//3,j//3)].add(board[i][j])
        
        return True
        
        