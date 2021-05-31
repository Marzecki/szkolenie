import re

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
print(len(test))
count = len(test)
not_passed = []
for passport in test:
    for name in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if name not in passport:
            count -= 1
            not_passed.append(passport)
            break


# ^\d{3} \d{3} \d{3}$|^\d{9}$
# ^www\.\w+\.[a-zA-Z]+$
# ^\w+\.\w+@\w+\.\w+$
# ^[A-Z][a-z]+ [A-Z][a-z]+$

def byr(text):
    return True if re.search("^\d{4}$", text) and 2002 >= int(text) >= 1920 else False


def iyr(text):
    return True if re.search("^\d{4}$", text) and 2020 >= int(text) >= 2010 else False


def eyr(text):
    return True if re.search("^\d{4}$", text) and 2030 >= int(text) >= 2020 else False


def hgt(text):
    if text[-2:] =='cm':
        text = text[:-2]
        return True if re.search("^\d$", text) and 193 >= int(text) >= 150 else False
    if text[-2:] =='in':
        text = text[:-2]
        return True if re.search("^\d$", text) and 76 >= int(text) >= 59 else False

not_passed2 = []

for passport in test:
    if passport not in not_passed:
        # for key in passport.keys():
        for key in ['byr', 'iyr', 'eyr', 'hgt']:
            if locals()[key](passport[key]):
                print(passport)
                not_passed2.append(passport)
                break

print(len(test))
print(len(test) - len(not_passed))
print(len(not_passed2))


