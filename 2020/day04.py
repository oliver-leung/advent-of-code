import re

def subset(lst1, lst2):
    for elt in lst1:
        if elt not in lst2:
            return False

    return True

digits = lambda x, y : len(str(x)) is y

def verify_passports(passports):
    count = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        if not subset(required_fields, list(passport.keys())):
            continue
        byr = passport['byr']
        if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
            continue
        iyr = passport['iyr']
        if len(iyr) !=4 or int(iyr) < 2010 or int(iyr) > 2020:
            continue
        eyr = passport['eyr']
        if len(eyr) !=4 or int(eyr) < 2020 or int(eyr) > 2030:
            continue
        hgt = passport['hgt']
        if 'cm' in hgt:
            cm = int(re.findall(r"-?\d+",hgt)[0])
            if cm < 150 or cm > 193: 
                continue
        elif 'in' in hgt:
            cm = int(re.findall(r"-?\d+",hgt)[0])
            if cm < 59 or cm > 76: 
                continue
        else:
            continue
        hcl = passport['hcl']
        if not re.match('#[0-9a-f]{6}',hcl):
            continue
        ecl = passport['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        pid = passport['pid']
        print(pid)
        if len(pid) is not 9:
            continue
        count += 1
        
    return count


def parse_data(filename):
    passports = []

    with open(filename) as f:
        lines = f.readlines()
        passport = {}
        for line in lines:
            if line is '\n':
                passports.append(passport)
                passport = {}
            else:
                for entry in line.split(' '):
                    key, value = entry.split(':')
                    passport[key] = value
        passports.append(passport)

    return passports

passports = parse_data('day4.txt')
print(verify_passports(passports))