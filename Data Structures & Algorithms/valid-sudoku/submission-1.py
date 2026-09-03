class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows ={}
        columns = {}
        grid = {
            0: {},
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {}
        }
        n = 0 
        for i in range(0, len(board)):
            rows ={}
            columns = {}
            
            for j in range(0, len(board[i])):
                box_row = i // 3
                box_column = j // 3
                box = (box_row) * 3 + (box_column)

                if board[i][j] in grid[box] and board[i][j] != ".":
                    return False
                elif board[i][j] not in grid[box] and board[i][j] != ".":
                    grid[box][board[i][j]] = 1

                if board[i][j] in rows and board[i][j] != ".":
                    return False
                elif board[i][j] not in rows:
                    rows[board[i][j]] = 1

                if board[j][i] in columns and board[j][i] != ".":
                    return False
                elif board[j][i] not in columns:
                    columns[board[j][i]] = 1

                




                
                





        return True #for test purpose