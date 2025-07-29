## Problem Statement
You are given a valid mathematical expression consisting of integers and the following operators:

- Division (/)
- Multiplication (*)
- Subtraction (-)
- Addition (+)

Each element in the expression is separated by a space. For example: 10 * 4 + 2
Normally, you'd evaluate this using standard BoDMAS rules. But in this challenge, we're flipping the script.

You must evaluate the expression using the following Reverse BoDMAS order:

- Addition
- Subtraction
- Multiplication
- Division

That means you first resolve all the +, then -, followed by *, and finally /, scanning left to right each time for each operation type.

Your job is to write a program that processes the expression and prints the result based on this reversed priority.

No brackets, no decimals — just clean, integer math.

## Input Format
A single line containing a valid mathematical expression. Each number and operator will be separated by exactly one space.

## Constraints
Expression contains only non-negative integers. Operators used: + - * / No brackets will be used. Length of the input expression ≤ 100 characters. All intermediate operations result in integers. Division will always be clean (no remainder or decimals).

## Output Format
Output a single integer: the final result after evaluating the expression using the Reverse BoDMAS order of operations.

## Sample Test Cases
1. Input:
   ``10 * 4 + 2``,
   Output:
   ``60``

2. Input:
   ``8 + 2 * 3 - 4 / 2``,
   Output:
   ``-5``
