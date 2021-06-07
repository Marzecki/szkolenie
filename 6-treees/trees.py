with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

trees = [line.strip() for line in lines]

x_iter, y_iter, count = 0, 0, 0

while y_iter < len(trees):
    if trees[y_iter][x_iter] == '#':
        count += 1
    y_iter += 1
    x_iter += 3
    x_iter = x_iter % len(trees[0])

print(count)
