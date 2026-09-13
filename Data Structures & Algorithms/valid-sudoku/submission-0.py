class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen=set()
            for column in range(len(board)):
                num=board[row][column]
                if num==".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        for column in range(len(board)):
            seen=set()
            for row in range(len(board)):
                num=board[row][column]
                if num==".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        

        for box_row in range(0, 9, 3):
            for box_column in range(0, 9, 3):

                seen = set()

                for row in range(box_row, box_row + 3):
                    for column in range(box_column, box_column + 3):

                        num = board[row][column]

                        if num == ".":
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True
                    