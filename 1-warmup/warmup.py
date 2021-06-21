def read_input(filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()

    test_list = []
    for line in lines:
        test_list.append(int(line))

    return test_list


def get_result(test_list):
    year = 2020
    for number1 in test_list:
        for number2 in test_list:
            if number1 != number2 and number1 + number2 == year:
                print(str(number1))
                print(str(number2))
                print(number1 * number2)
                return number1, number2


read_input('input.txt')
print(get_result(read_input('input.txt')))

print('sourcetree test')
print('sourcetree test2')
