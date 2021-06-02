def create_empty_cube(x_size, y_size, z_size):
    return [[['.' for _ in range(x_size)] for _ in range(y_size)] for _ in range(z_size)]

with open('input.txt') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

initial_layer = [[element for element in line] for line in lines]

cycles = 6
xy_size = cycles * 2 + len(initial_layer[0])
z_size = cycles * 2 + 1

unit_vector = [-1, 0, 2]

new_cube = create_empty_cube(xy_size, xy_size, z_size)
copy_cube = create_empty_cube(xy_size, xy_size, z_size)

for y in range(len(initial_layer[0])):
    for x in range(len(initial_layer[0][0])):
        new_cube[cycles][cycles + y][cycles + x] = initial_layer[y][x]

# unfinished