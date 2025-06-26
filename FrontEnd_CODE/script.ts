const gridContainer = document.getElementById("sudoku-grid") as HTMLElement;
const solveButton = document.getElementById("solve-btn") as HTMLButtonElement;

/**
 * Dynamically creates a 9x9 Sudoku grid using <input> elements
 * and appends them to the grid container.
 */
function createGrid(){
    for(let row =0; row < 9; row++){
        for(let col = 0; col < 9; col++){
            const input = document.createElement("input");

            //Configuring the input attrtibutes: only digits 1-9 are allowed
            input.setAttribute("type", "number");
            input.setAttribute("min", "1");
            input.setAttribute("max", "9");

            //Storing the cell location in custom attributes for later access
            input.setAttribute("data-row", row.toString());
            input.setAttribute("data-col", col.toString());

            //ADD INPUT TO GRID CONTAINER
            gridContainer.appendChild(input);
            
        }
    }
}
/**
 * Reads the values from the grid and converts them into a 2D array.
 * Empty cells are represented as 0.
 */
function getBoard(): number[][] {
    const board: number[][] = [];
  
    for (let row = 0; row < 9; row++) {
      const rowData: number[] = [];
  
      for (let col = 0; col < 9; col++) {
        const cell = document.querySelector(
          `input[data-row="${row}"][data-col="${col}"]`
        ) as HTMLInputElement;
  
        // Parse input value, use 0 if empty
        const val = parseInt(cell.value);
        rowData.push(isNaN(val) ? 0 : val);
      }
  
      board.push(rowData);
    }
  
    return board;
  }
  
  /**
   * Fills the grid with the solved Sudoku board and disables editing.
   * @param solution - A 2D array representing the solved board
   */
  function setBoard(solution: number[][]) {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        const cell = document.querySelector(
          `input[data-row="${row}"][data-col="${col}"]`
        ) as HTMLInputElement;
  
        // Set value and disable cell
        cell.value = solution[row][col].toString();
        cell.disabled = true;
      }
    }
  }

  /**
 * Sends the current board to the backend API for solving,
 * and updates the UI with the solution if successful.
 */
async function solveSudoku() {
    const board = getBoard();

    try{
        const response = await fetch("http://localhost:5000/solve", {
            method: "POST",
            headers: { "Content-Type" : "application/json" },
            body: JSON.stringify({ board }), 
        });

        if (response.ok) {
            const data = await response.json();
            setBoard(data.solution); // Update UI with solution
          } else {
            alert("Error solving Sudoku. Check server logs or board input.");
          }
        } catch (error) {
          alert("Unable to reach the backend. Is the server running?");
        }
      }

      createGrid();

      solveButton.addEventListener("click", solveSudoku);
        
    