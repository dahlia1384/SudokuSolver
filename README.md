# Sudoku Solver

A full-stack web-based Sudoku Solver developed by:

- **Dahlia Mohammadi** – Computer Engineering Student (BASc) (Working on Frontend & 1/2 of Communication)
- **Camilla Cloutier** – Computer Science Student (BSc) (Working on Backend & 1/2 of Communication)

This project enables users to input a Sudoku puzzle and receive an instant solution using a backtracking algorithm, all through a clean and interactive interface.

---

## 1. Core Components

| Component     | Language                | Purpose                                                  |
|---------------|-------------------------|----------------------------------------------------------|
| Backend       | Python                  | Solves the Sudoku puzzle using a solving algorithm       |
| Frontend      | HTML, CSS, TypeScript   | User interface to input and display the puzzle           |
| Communication | REST API (Flask/FastAPI)| Sends puzzle data between frontend and backend           |

---

## 2. Tools and Technologies

### Python (Backend)
- Use Flask or FastAPI to serve a simple REST API
- Implements a Sudoku-solving algorithm (e.g., backtracking)
- Accepts JSON input and returns a JSON-formatted solution

### TypeScript (Frontend Logic)
- Handles dynamic creation of the 9x9 grid
- Validates user input
- Sends a POST request to the backend API with the puzzle data
- Displays the returned solution on the same grid

### CSS (Styling)
- Styles the Sudoku grid and button layout
- Ensures a clean and user-friendly design
- Optional: integrate a responsive framework like Tailwind or Bootstrap

### HTML (Structure)
- Builds the structure of the web interface
- Contains a 9x9 input grid for puzzle entry and a solve button

---

## 3. Workflow

### 3.1 Frontend
- Displays an editable 9x9 grid using HTML and CSS
- Users input known Sudoku numbers
- On clicking the Solve button:
  - The grid data is collected
  - A POST request is sent to the Python backend API
  - The response (solved puzzle) is rendered back into the grid
  - Solved cells are made read-only or styled differently

### 3.2 Backend (Python)
- Receives a 9x9 grid as a JSON object
- Solves the puzzle using a recursive backtracking algorithm
- Returns the completed puzzle as a JSON response

---

## Features

- Solves standard Sudoku puzzles using a well-tested algorithm
- Clean, responsive user interface
- Clear separation between backend logic and frontend presentation
- Fully customizable and extendable codebase

---

## File Structure (Frontend)

- `index.html` – Contains the main layout and structure of the app
- `styles.css` – Handles layout, styling, and responsiveness
- `script.ts` – Manages user interaction, API communication, and puzzle display

---

## Demo

Include a screenshot of the working interface or a link to a hosted demo.

---

## How to Run

### Frontend
1. Clone or download the repository
2. Open `index.html` in your web browser

### Backend
1. Navigate to the backend directory
2. Run the backend server using Flask or FastAPI:
   ```bash
   python app.py  # Flask
   # or
   uvicorn main:app --reload  # FastAPI
