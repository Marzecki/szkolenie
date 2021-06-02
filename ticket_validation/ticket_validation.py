dict_strings = []
validation = {}
tickets = []
results = {}

with open('input.txt', 'r') as file:
    lines = file.readlines()

for iteration, line in enumerate(lines):
    if iteration < 20:
        dict_strings.append(line.strip())
    elif iteration == 22:
        my_ticket = line.strip().split(',')
    elif iteration not in [20, 21, 23, 24]:
        tickets.append(line.strip().split(','))

for iteration, line in enumerate(dict_strings):
    line = line.replace(': ', ',').replace(' or ', ',').replace('-', ',')
    line = line.split(',')
    validation[iteration] = [int(line[1]), int(line[2]), int(line[3]), int(line[4])]

sum = 0
for ticket in tickets:
    for number in ticket:
        success = False
        for key in validation:
            if  validation[key][0] <= int(number) <= validation[key][1] or validation[key][2] <= int(number) <= validation[key][3]:
                success = True
                break
        if not success:
            sum += int(number)


print(validation)
print(tickets)
print(sum)
