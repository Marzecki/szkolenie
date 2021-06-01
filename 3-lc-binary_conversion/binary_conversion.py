with open('input.txt', 'r') as file:
    lines = file.readlines()

results = []
lines = [line.strip() for line in lines]

for line in lines:
    binary = ''.join(['1' if character == 'B' else '0' for character in line[:7]])
    number1 = int(binary, 2)

    binary = ''.join(['1' if character == 'R' else '0' for character in line[-3:]])
    number2 = int(binary, 2)

    results.append(number1 * 8 + number2)

print(max(results))

for iter in range(min(results), max(results)):
    if iter not in results:
        print(iter)
