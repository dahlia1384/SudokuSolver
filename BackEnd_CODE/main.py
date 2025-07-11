from sympy import solve
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#9x9 Sudoku grid
class SudokuPuzzle(BaseModel):
    board: List[List[int]]

@app.post("/solve")
def solve_sudoku(puzzle: SudokuPuzzle):
    board = puzzle.board

    if not is_valid_board(board):
        raise HTTPException(status_code=400, detail="Invalid board size")

    if solve(board):
        return {"solution": board}
    else:
        raise HTTPException(status_code=422, detail="No solution size")

def is_valid_board(board: List[List[int]]) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                    return False
                return True

def is_safe(board: List[List[int]], row: int, col: int, num:int) -> bool:
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True