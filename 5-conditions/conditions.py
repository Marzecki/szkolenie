with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

lines = [line.strip() for line in lines]

commands = {}
for iteration, line in enumerate(lines):
    commands[iteration] = line.split()

acc = 0
pointer = 0
commands_done = []
jumps = 0
while pointer not in commands_done:
    jumps += 1
    commands_done.append(pointer)
    if commands[pointer][0] == 'acc':
        if commands[pointer][1][0] == '+':
            acc += int(commands[pointer][1][1:])
        else:
            acc -= int(commands[pointer][1][1:])
        pointer += 1
    if commands[pointer][0] == 'nop':
        pointer += 1
    if commands[pointer][0] == 'jmp':
        if commands[pointer][1][0] == '+':
            pointer += int(commands[pointer][1][1:])
        else:
            pointer -= int(commands[pointer][1][1:])

print(acc)
print(jumps)
