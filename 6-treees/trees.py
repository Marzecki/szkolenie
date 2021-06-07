with open('input.txt', 'r') as file:
    lines = file.readlines()

trees = [line.strip() for line in lines]

x, y, sum = 0, 0, 0

while y < len(trees):
    if trees[y][x] == '#':
        sum += 1
    y += 1
    x += 3
    x = x % len(trees[0])

print(sum)
