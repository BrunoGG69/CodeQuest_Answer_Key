# Mini Sudoku Solver
## Problem Statement
1. Given a 4x4 unsolved sudoku (in the form of a 2D list), which has 4 subsections of size 2x2, write a program that solves the sudoku 
2. Zeroes in the list represent empty spaces
3. A solved sudoku is such that each number only appears once in its row, column and subsection, and each row, column, and subsection has every number 1 through 4 (usually 9 but in this case 4)

## Example:

![image](https://s3.amazonaws.com/hr-assets/0/1753813858-06bd5f0f16-Screenshot2025-07-29235916.png)

## Input format
A 4x4 2D list where each element is an integer between 0 and 4 inclusive. 0 represents an empty cell.

## Constraints
- Input is always a 4x4 grid.
- 0 ≤ grid[i][j] ≤ 4

## Output format
- If solvable, print the completed 4x4 Sudoku as a list of lists.
- If unsolvable, just print 0.