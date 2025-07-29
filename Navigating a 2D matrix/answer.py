grid = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

# Reading the instructions as a string of digits
instructions = input("Input the instructions").strip()

# Mapping the Coordinates: 0 = Left, 1 = Right, 2 = Up, 3 = Down
moves = {
    '0': (0, -1),
    '1': (0, 1),
    '2': (-1, 0),
    '3': (1, 0)
}

# Initial Cursor Start Position
x, y = 0, 0
output = []

if 0 <= x < 4 and 0 <= y < 4:
    output.append(grid[x][y])

for i in instructions:
    if i in moves:
        dx, dy = moves[i]
        x += dx
        y += dy
        if 0 <= x < 4 and 0 <= y < 4:
            output.append(grid[x][y])
    # Invalid directions like '4', '5', etc. are ignored

print(' '.join(output))
