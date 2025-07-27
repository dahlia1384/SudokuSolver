from flask import Flask, request, jsonify #flask is a simple micro web framework designed for building web applications
#the request object is a global object that provides access to incoming request data from the client.
# the jsonify function in flask is used to serialize python data structures like lists into JSON format and return them as HTTP response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend 

@app.route('/solve', methods=['POST'])
def solve_sudoku():
    data = request.get_json()

    if not data or 'board' not in data:
        return jsonify({"error": "Missing board in request"}), 400

    board = data['board']

    if not is_valid_board(board):
        return jsonify({"error": "Invalid board size"}), 400

    if solve(board):
        return jsonify({"solution": board})
    else:
        return jsonify({"error": "No solution exists for this puzzle"}), 422

def is_valid_board(board):
    return isinstance(board, list) and len(board) == 9 and all(isinstance(row, list) and len(row) == 9 for row in board)

# Backtracking Sudoku solver
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0  # backtrack
                return False
    return True

def is_safe(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

if __name__ == '__main__':
    app.run(debug=True)
