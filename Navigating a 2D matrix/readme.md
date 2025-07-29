## Problem Statement
Given a 2D list called the “Map,” and a list of integers called “Instructions,” where

- 0 → Left
- 1 → Right
- 2 → Up
- 3 → Down

Write a program where:
- A virtual cursor begins from the **Top Left of the Map**, and moves according to the Instructions, pushing the value of any cell it lands on to an output list. 
- The program should allow the cursor to go beyond the Map and return to it if the instructions call for that, however it should not push any values while the cursor is outside the Map

Example:
```
Map = [
    [A, B, C, D],
    [E, F, G, H],
    [I, J, K, L],
    [M, N, O, P]
]
```

## Input Format:
```
121133
```
## Constraints:
- Map Contains UpperCase Letters (A-Z)
- Instructions string length ≤ 10⁴
- Cursor Starts at Map[0][0]

## Output Format:
A single line of space-seperated characters, representing the values visited while inside the map

## Sample Input:
```
121133
```

## Sample Output:
```
A B D H
```