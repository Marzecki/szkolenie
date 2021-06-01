with open('input.txt', 'r') as file:
    lines = file.readlines()

mem = {}
masks = []
for line in lines:
    if 'mask' in line:
        mask = line[-37:-1]
        mask = mask[::-1]
    else:
        index, number = line.replace('mem[', '').replace('] =', '').replace('\n', '').split()
        number = '{0:b}'.format(int(number))[::-1]
        while len(number) < 36:
            number += '0'

        new_number = ''
        for iteration, character in enumerate(number):
            if character == '1':
                new_number += '0' if mask[iteration] == '0' else '1'
            else:
                new_number += '1' if mask[iteration] == '1' else '0'
        mem[index] = int(new_number[::-1], 2)

sum = 0
for mem_key in mem:
    sum += mem[mem_key]
print(sum)
