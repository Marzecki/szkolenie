test = []
with open('input.txt', 'r') as input_file:
    people_list = input_file.read().split('\n\n')

    for person in people_list:
        person = person.replace('\n', ' ')
        person = person.split(' ')
        print(person)
        dict1 = {}
        for element in person:
            key, value = element.split(':')
            dict1[key] = value
        test.append(dict1)

print(test)
