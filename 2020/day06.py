def count_yeses(groups):
    counts = []
    for group in groups:
        yeses = set()
        for person in group:
            for yes in person:
                yeses.add(yes)
        counts.append(len(yeses))
    return counts

def count_common_yeses(groups):
    counts = []
    for group in groups:
        group = list(map(set, group))
        yeses = set(group[0]).intersection(*group)
        counts.append(len(yeses))
    return counts

def parse():
    with open('day6.txt') as f:
        raw_data = f.readlines()
    
    groups = []
    people = []
    for line in raw_data:
        if line is '\n':
            groups.append(people)
            people = []
        else:
            people.append(list(line.strip()))
    groups.append(people)

    return groups

groups = parse()
counts = count_yeses(groups)
print(sum(counts))
counts = count_common_yeses(groups)
print(sum(counts))