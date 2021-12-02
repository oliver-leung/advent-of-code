def isValid(lo, hi, char, password):
    num = 0
    for chr in password:
        if chr is char:
            num += 1
    
    if num >= lo and num <= hi:
        return True
    else:
        return False

def isValid2(lo, hi, char, password):
    return True if (password[lo-1] is char) is not (password[hi-1] is char) else False

def countValid(entries):
    count = 0
    for entry in entries:
        if isValid2(*entry):
            count += 1

    return count

def parseInput(filename):
    with open(filename, 'r') as f:
        data = f.readlines()

    parsed_data = []
    for line in data:
        words = line.strip().split()
        lo,hi = [int(x) for x in words[0].split('-')]
        ch_req = words[1][0]
        password = words[2]
        parsed_data.append((lo, hi, ch_req, password))

    print(countValid(parsed_data))

parseInput('day2.txt')