import re

test = []
with open('input.txt', 'r') as input_file:
    people_list = input_file.read().split('\n\n')

    for person in people_list:
        person = person.replace('\n', ' ')
        person = person.split(' ')
        dict1 = {}
        for element in person:
            key, key_value = element.split(':')
            dict1[key] = key_value
        test.append(dict1)

count = len(test)
not_passed = []
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in test:
    for name in keys:
        if name not in passport:
            count -= 1
            not_passed.append(passport)
            break


# ^\d{3} \d{3} \d{3}$|^\d{9}$
# ^www\.\w+\.[a-zA-Z]+$
# ^\w+\.\w+@\w+\.\w+$
# ^[A-Z][a-z]+ [A-Z][a-z]+$

def byr(text):
    min_val, max_val = 2002, 1920
    return re.search(r'^\d{4}$', text) and min_val >= int(text) >= max_val


def iyr(text):
    min_val, max_val = 2020, 2010
    return re.search(r'^\d{4}$', text) and min_val >= int(text) >= max_val


def eyr(text):
    min_val, max_val = 2030, 2020
    return re.search(r'^\d{4}$', text) and min_val >= int(text) >= max_val


def hgt(text):
    if text[-2:] == 'cm':
        text = text[:-2]
        min_val, max_val = 193, 150
        return re.search(r'^\d+$', text) and min_val >= int(text) >= max_val
    if text[-2:] == 'in':
        text = text[:-2]
        min_val, max_val = 76, 59
        return re.search(r'^\d+$', text) and min_val >= int(text) >= max_val


def hcl(text):
    return re.search('^#[0-9a-f]{6}$', text)


def ecl(text):
    possible_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return text in possible_values


def pid(text):
    return re.search(r'^\d{9}$', text)


not_passed2 = []
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in test:
    if passport not in not_passed:
        for key in keys:
            if not locals()[key](passport[key]):
                not_passed2.append(passport)
                break

print(len(test))
print(len(test) - len(not_passed))
print(len(test) - len(not_passed) - len(not_passed2))
